from db import *
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import plotly.graph_objects as go # type: ignore


def get_networth_by_year(year=None):
    """
    Get networth data grouped by year.
    
    Args:
        year: Optional year filter (string or int)
    
    Returns:
        Dictionary with year totals or single year total
    """
    
    if year:
        # Get networth for specific year
        query = """
            SELECT EXTRACT(YEAR FROM source_date) as year, SUM(amount) as total
            FROM net_worth 
            WHERE EXTRACT(YEAR FROM source_date) = %s
            GROUP BY EXTRACT(YEAR FROM source_date)
        """
        results = run_query(query, (int(year),))
        
        if results and len(results) > 0:
            return float(results[0][1])
        else:
            return 0.0
    else:
        # Get networth for all years
        query = """
            SELECT EXTRACT(YEAR FROM source_date) as year, SUM(amount) as total
            FROM net_worth 
            GROUP BY EXTRACT(YEAR FROM source_date)
            ORDER BY year
        """
        results = run_query(query)
        
        year_totals = {}
        if results:
            for row in results:
                year_val = int(row[0])
                total = float(row[1])
                year_totals[year_val] = total
        
        return year_totals


def get_networth_progress_data(target_years=None, target_amounts=None):
    """
    Get networth progress data for specified years with target amounts.
    
    Args:
        target_years: List of years to include
        target_amounts: Dictionary of year -> target amount 
    
    Returns:
        List of dictionaries with year, amount, target, and progress percentage data
    """
    
    if target_years is None:
        target_years = [2024, 2025, 2026, 2027, 2028]
    
    if target_amounts is None:# Default to $1,000,000 target for each year
        target_amounts = {
            2024: 1000000, 
            2025: 1000000, 
            2026: 1000000,
            2027: 1000000,
            2028: 1000000
        }
    
    # Get all networth data by year
    year_totals = get_networth_by_year()
    
    # Calculate progress data
    progress_data = []
    
    for year in target_years:
        amount = year_totals.get(year, year_totals.get(2025,0))
        target = target_amounts.get(year, 0)
        
        # Calculate percentage based on target amount
        percentage = (amount / target * 100) if target > 0 else 0
        
        progress_data.append({
            'year': year,
            'amount': amount,
            'target': target,
            'percentage': percentage,
            'formatted_amount': f"${amount:,.0f}" if amount > 0 else "$0",
            'formatted_target': f"${target:,.0f}",
            'is_achieved': amount >= target
        })
    
    return progress_data


def get_networth_summary():
    """
    Get overall networth summary statistics.
    
    Returns:
        Dictionary with summary statistics
    """
    
    # Get latest networth entry
    latest_query = """
        SELECT source_date, SUM(amount) as total
        FROM net_worth 
        GROUP BY source_date
        ORDER BY source_date DESC
        LIMIT 1
    """
    latest_results = run_query(latest_query)
    
    # Get year-over-year growth
    yoy_query = """
        SELECT 
            EXTRACT(YEAR FROM source_date) as year,
            SUM(amount) as total
        FROM net_worth 
        GROUP BY EXTRACT(YEAR FROM source_date)
        ORDER BY year DESC
        LIMIT 2
    """
    yoy_results = run_query(yoy_query)
    
    summary = {
        'latest_amount': 0,
        'latest_date': None,
        'yoy_growth': 0,
        'yoy_growth_percentage': 0
    }
    
    if latest_results and len(latest_results) > 0:
        summary['latest_amount'] = float(latest_results[0][1])
        summary['latest_date'] = latest_results[0][0]
    
    if yoy_results and len(yoy_results) >= 2:
        current_year_amount = float(yoy_results[0][1])
        previous_year_amount = float(yoy_results[1][1])
        
        summary['yoy_growth'] = current_year_amount - previous_year_amount
        if previous_year_amount > 0:
            summary['yoy_growth_percentage'] = (summary['yoy_growth'] / previous_year_amount) * 100
    
    return summary


def get_networth_by_category(year=None):
    """
    Get networth breakdown by category, summing all entries within the latest year and calculating YoY growth.
    
    Args:
        year: Optional year filter (if provided, uses that year; otherwise uses latest year with data)
    
    Returns:
        List of dictionaries with category breakdowns including YoY growth for the latest year
    """
    
    if year:
        # Use the specified year
        target_year = int(year)
    else:
        # Find the latest year with networth data
        latest_year_query = """
            SELECT EXTRACT(YEAR FROM source_date) as year
            FROM net_worth 
            ORDER BY source_date DESC
            LIMIT 1
        """
        latest_year_results = run_query(latest_year_query)
        
        if not latest_year_results or len(latest_year_results) == 0:
            return []  # No data available
        
        target_year = int(latest_year_results[0][0])
    
    previous_year = target_year - 1
    
    # Get data for both current and previous year
    current_year_query = """
        SELECT 
            category, 
            SUM(amount) as total,
            MAX(source_date) as latest_date
        FROM net_worth 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        GROUP BY category
        ORDER BY total DESC
    """
    current_results = run_query(current_year_query, (target_year,))
    
    previous_year_query = """
        SELECT 
            category, 
            SUM(amount) as total
        FROM net_worth 
        WHERE EXTRACT(YEAR FROM source_date) = %s
        GROUP BY category
    """
    previous_results = run_query(previous_year_query, (previous_year,))
    
    # Create a dictionary for previous year amounts
    previous_amounts = {}
    if previous_results:
        for row in previous_results:
            previous_amounts[row[0]] = float(row[1])
    
    categories = []
    if current_results:
        for row in current_results:
            category = row[0]
            current_amount = float(row[1])
            latest_date = row[2]
            
            # Calculate YoY growth
            previous_amount = previous_amounts.get(category, 0)
            yoy_growth = current_amount - previous_amount
            yoy_growth_percentage = 0
            
            if previous_amount > 0:
                yoy_growth_percentage = (yoy_growth / previous_amount) * 100
            elif current_amount > 0 and previous_amount == 0:
                # New category (100% growth isn't meaningful, so we'll show it differently)
                yoy_growth_percentage = float('inf')
            
            categories.append({
                'category': category,
                'amount': current_amount,
                'formatted_amount': f"${current_amount:,.0f}",
                'latest_date': latest_date,
                'year': target_year,
                'previous_year': previous_year,
                'previous_amount': previous_amount,
                'yoy_growth': yoy_growth,
                'yoy_growth_percentage': yoy_growth_percentage,
                'formatted_yoy_growth': f"${yoy_growth:+,.0f}" if yoy_growth != 0 else "$0",
                'is_new_category': previous_amount == 0 and current_amount > 0
            })
    
    return categories


def get_passive_income_by_year(year=None):
    """
    Get passive income data grouped by year from the income table.
    
    Args:
        year: Optional year filter (string or int)
    
    Returns:
        Dictionary with year totals or single year total
    """
    
    if year:
        # Get passive income for specific year
        query = """
            SELECT EXTRACT(YEAR FROM source_date) as year, SUM(amount) as total
            FROM income 
            WHERE category = 'passive_income' AND EXTRACT(YEAR FROM source_date) = %s
            GROUP BY EXTRACT(YEAR FROM source_date)
        """
        results = run_query(query, (int(year),))
        
        if results and len(results) > 0:
            return float(results[0][1])
        else:
            return 0.0
    else:
        # Get passive income for all years
        query = """
            SELECT EXTRACT(YEAR FROM source_date) as year, SUM(amount) as total
            FROM income 
            WHERE category = 'passive_income'
            GROUP BY EXTRACT(YEAR FROM source_date)
            ORDER BY year
        """
        results = run_query(query)
        
        year_totals = {}
        if results:
            for row in results:
                year_val = int(row[0])
                total = float(row[1])
                year_totals[year_val] = total
        
        return year_totals


def get_passive_income_progress_data(target_years=None, target_amounts=None):
    """
    Get passive income progress data for specified years with target amounts.
    
    Args:
        target_years: List of years to include
        target_amounts: Dictionary of year -> target amount 
    
    Returns:
        List of dictionaries with year, amount, target, and progress percentage data
    """
    
    if target_years is None:
        target_years = [2024, 2025, 2026, 2027, 2028]
    
    if target_amounts is None:
        # Default passive income targets
        target_amounts = {
            2024: 10500,
            2025: 11000, 
            2026: 11500,
            2027: 12000,
            2028: 12500
        }
    
    # Get all passive income data by year
    year_totals = get_passive_income_by_year()
    
    # Calculate progress data
    progress_data = []
    
    for year in target_years:
        amount = year_totals.get(year, 0)
        target = target_amounts.get(year, 0)
        
        # Calculate percentage based on target amount
        percentage = (amount / target * 100) if target > 0 else 0
        
        progress_data.append({
            'year': year,
            'amount': amount,
            'target': target,
            'percentage': percentage,
            'formatted_amount': f"${amount:,.0f}" if amount > 0 else "$0",
            'formatted_target': f"${target:,.0f}",
            'is_achieved': amount >= target
        })
    
    return progress_data
