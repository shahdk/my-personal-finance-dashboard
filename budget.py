from db import *
import pandas as pd # type: ignore
import plotly.graph_objects as go # type: ignore
import streamlit as st # type: ignore
from income import get_income_categories
from expense import get_expense_categories
import calendar
import time


def get_yearly_budget(years=None, categories=None):
    """
    Create a yearly budget table with years as columns and income/expense sources as rows.
    Groups data by category with header rows for each category.
    
    Args:
        years: Optional year filter (string, int, or list of years)
        categories: Optional list of categories to filter
    
    Returns:
        Plotly table figure for Streamlit
    """
    
    # Build base queries
    income_query = """
        SELECT 
            'Income' as type,
            source, 
            category, 
            EXTRACT(YEAR FROM source_date) as year,
            SUM(amount) as total 
        FROM income 
        GROUP BY source, category, EXTRACT(YEAR FROM source_date)
        ORDER BY category, source, year
    """
    
    expense_query = """
        SELECT 
            'Expense' as type,
            source, 
            category, 
            EXTRACT(YEAR FROM source_date) as year,
            SUM(amount) as total 
        FROM expense 
        GROUP BY source, category, EXTRACT(YEAR FROM source_date)
        ORDER BY category, source, year
    """
    
    # Apply year filter if specified
    if years and len(years) > 0:
        # Convert single year to list for consistent handling
        if isinstance(years, (str, int)):
            year_list = [years]
        else:
            year_list = years
        
        # Create IN clause for SQL
        year_values = ','.join(str(y) for y in year_list)
        
        income_query = f"""
            SELECT 
                'Income' as type,
                source, 
                category, 
                EXTRACT(YEAR FROM source_date) as year,
                SUM(amount) as total 
            FROM income 
            WHERE EXTRACT(YEAR FROM source_date) IN ({year_values})
            GROUP BY source, category, EXTRACT(YEAR FROM source_date)
            ORDER BY category, source, year
        """
        expense_query = f"""
            SELECT 
                'Expense' as type,
                source, 
                category, 
                EXTRACT(YEAR FROM source_date) as year,
                SUM(amount) as total 
            FROM expense 
            WHERE EXTRACT(YEAR FROM source_date) IN ({year_values})
            GROUP BY source, category, EXTRACT(YEAR FROM source_date)
            ORDER BY category, source, year
        """
    
    # Execute queries
    income_results = run_query(income_query)
    expense_results = run_query(expense_query)
    
    # Combine results
    all_data = []
    
    # Process income data
    for row in income_results:
        type_val, source, category, year_val, total = row
        if not categories or category in categories:
            all_data.append({
                'type': type_val,
                'source': source,
                'category': category,
                'year': int(year_val),
                'amount': float(total)
            })
    
    # Process expense data
    for row in expense_results:
        type_val, source, category, year_val, total = row
        if not categories or category in categories:
            all_data.append({
                'type': type_val,
                'source': source,
                'category': category,
                'year': int(year_val),
                'amount': float(total)
            })
    
    if not all_data:
        # Return empty table
        fig = go.Figure(data=[go.Table(
            header=dict(values=['No data available'],
                       fill_color='lightgray',
                       align='left'),
            cells=dict(values=[['No data to display']],
                      fill_color='white',
                      align='left')
        )])
        return fig
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Get all unique years and sort them in descending order
    available_years = sorted(df['year'].unique(), reverse=True)
    
    # Pivot data to have years as columns
    pivot_df = df.pivot_table(
        index=['type', 'category', 'source'], 
        columns='year', 
        values='amount', 
        fill_value=0,
        aggfunc='sum'
    ).reset_index()
    
    # Calculate total amount for each source (sum across all years) for sorting
    pivot_df['total_amount'] = pivot_df[available_years].sum(axis=1)
    
    # Sort to show Income first, then Expense, and sort sources by amount for earned/passive income
    def custom_sort_key(series):
        if series.name == 'type':
            return series.map({'Income': 0, 'Expense': 1})
        elif series.name == 'category':
            # Custom category ordering for expenses: taxes, needs, wants, investments
            expense_category_order = {
                'taxes': 0,
                'needs': 1, 
                'wants': 2,
                'investments': 3
            }
            sort_values = []
            for idx, category in enumerate(series):
                row = pivot_df.iloc[idx]
                if row['type'] == 'Expense' and category in expense_category_order:
                    sort_values.append(expense_category_order[category])
                else:
                    sort_values.append(category)  # Keep original order for income categories
            return sort_values
        elif series.name == 'source':
            # For sources, sort by negative total_amount for earned_income and passive_income categories
            # This will give descending order by amount
            sort_values = []
            for idx, source in enumerate(series):
                row = pivot_df.iloc[idx]
                if row['category'] in ['earned_income', 'passive_income']:
                    sort_values.append(-row['total_amount'])  # Negative for descending
                elif row['category'] == 'wants':
                    # For wants category: subscriptions first, then alphabetical
                    if 'subscription' in source.lower():
                        sort_values.append(f"0_{source}")  # Prefix with 0 to sort first
                    else:
                        sort_values.append(f"1_{source}")  # Prefix with 1 to sort after subscriptions
                else:
                    sort_values.append(source)  # Alphabetical for other categories
            return sort_values
        else:
            return series
    
    pivot_df = pivot_df.sort_values(['type', 'category', 'source'], key=custom_sort_key)
    
    # Remove the temporary total_amount column
    pivot_df = pivot_df.drop('total_amount', axis=1)
    
    # Create table data - simpler approach
    table_rows = []
    
    # Group by type and category for better organization
    current_type = None
    current_category = None
    
    for _, row in pivot_df.iterrows():
        row_type = row['type']
        row_category = row['category']
        row_source = row['source']
        
        # Add type header if it's a new type
        if row_type != current_type:
            current_type = row_type
            current_category = None  # Reset category when type changes
            # Add a separator row for type
            type_header = [row_type] + [''] * len(available_years)
            table_rows.append(type_header)
        
        # Add category header if it's a new category
        if row_category != current_category:
            current_category = row_category
            # Add category header row
            category_display = row_category.replace('_', ' ').title()
            category_header = [f"{category_display}"] + [''] * len(available_years)
            table_rows.append(category_header)
        
        # Add the actual data row
        source_display = row_source.replace('_', ' ').title()
        data_row = [source_display]  # source name
        
        # Add amounts for each year
        for year_col in available_years:
            amount = row[year_col] if year_col in row.index else 0
            if amount != 0:
                # Format as USD currency without decimals
                rounded_amount = round(amount)
                data_row.append(f"${rounded_amount:,}")
            else:
                data_row.append('-')
        
        table_rows.append(data_row)
    
    # Prepare data for plotly table
    if table_rows:
        # Create column headers
        headers = ['Source/Category'] + [str(year) for year in available_years]
        
        # Transpose table_rows for plotly (each column should be a list)
        num_cols = len(headers)
        column_values = [[] for _ in range(num_cols)]
        row_colors = []
        
        for row in table_rows:
            # Determine row color based on content
            if row and (row[0] == 'Income' or row[0] == 'Expense'):
                row_colors.append('darkgrey')
            elif row and row[0] and len(row) > 1 and all(cell == '' for cell in row[1:]):
                # Category headers: non-empty first column, all other columns empty
                row_colors.append('lightgrey')
            else:
                row_colors.append('white')
            
            for col_idx in range(num_cols):
                if col_idx < len(row):
                    column_values[col_idx].append(row[col_idx])
                else:
                    column_values[col_idx].append('')
        
        # Create color matrix for cells (each column gets the same row colors)
        cell_colors = [row_colors for _ in range(num_cols)]
        
        # Create column widths - make source column wider
        num_year_cols = len(available_years)
        source_col_width = max(300, 400 - (num_year_cols * 20))  # Adaptive width based on number of year columns
        year_col_width = min(120, max(80, (1000 - source_col_width) // num_year_cols)) if num_year_cols > 0 else 120
        
        column_widths = [source_col_width] + [year_col_width] * num_year_cols
        
        # Create plotly table
        fig = go.Figure(data=[go.Table(
            columnwidth=column_widths,
            header=dict(
                values=headers,
                fill_color='lightblue',
                align='left',
                font=dict(size=16, color='black'),
                height=40  # Add height to header
            ),
            cells=dict(
                values=column_values,
                fill_color=cell_colors,
                align='left',
                font=dict(size=14),
                height=35,  # Add height to cells for padding
                line=dict(color='#E0E0E0', width=1)  # Add subtle borders
            )
        )])
        
        fig.update_layout(
            title="Yearly Budget Summary",
            height=max(450, len(table_rows) * 30 + 120)  # Dynamic height based on rows (increased for larger font)
        )
    else:
        # Empty table
        headers = ['Source/Category'] + [str(year) for year in available_years] if available_years else ['No Data']
        fig = go.Figure(data=[go.Table(
            header=dict(values=headers,
                       fill_color='lightblue',
                       align='left'),
            cells=dict(values=[[] for _ in headers],
                      fill_color='white',
                      align='left')
        )])
    
    return fig


def get_monthly_budget_data(year=None, categories=None):
    """
    Get monthly budget data as a DataFrame for editing in Streamlit.
    Returns data organized by month columns and income/expense source rows.
    
    Args:
        year: Optional year filter (string or int for single year)
        categories: Optional list of categories to filter
    
    Returns:
        pandas DataFrame ready for st.data_editor
    """
    
    # Build base queries for monthly data
    income_query = """
        SELECT 
            'Income' as type,
            source, 
            category, 
            EXTRACT(YEAR FROM source_date) as year,
            EXTRACT(MONTH FROM source_date) as month,
            SUM(amount) as total 
        FROM income 
        GROUP BY source, category, EXTRACT(YEAR FROM source_date), EXTRACT(MONTH FROM source_date)
        ORDER BY category, source, year, month
    """
    
    expense_query = """
        SELECT 
            'Expense' as type,
            source, 
            category, 
            EXTRACT(YEAR FROM source_date) as year,
            EXTRACT(MONTH FROM source_date) as month,
            SUM(amount) as total 
        FROM expense 
        GROUP BY source, category, EXTRACT(YEAR FROM source_date), EXTRACT(MONTH FROM source_date)
        ORDER BY category, source, year, month
    """
    
    # Apply year filter if specified
    if year is not None and year != "":
        # Convert to int to ensure proper filtering
        year_int = int(year)
        income_query = f"""
            SELECT 
                'Income' as type,
                source, 
                category, 
                EXTRACT(YEAR FROM source_date) as year,
                EXTRACT(MONTH FROM source_date) as month,
                SUM(amount) as total 
            FROM income 
            WHERE EXTRACT(YEAR FROM source_date) = {year_int}
            GROUP BY source, category, EXTRACT(YEAR FROM source_date), EXTRACT(MONTH FROM source_date)
            ORDER BY category, source, year, month
        """
        expense_query = f"""
            SELECT 
                'Expense' as type,
                source, 
                category, 
                EXTRACT(YEAR FROM source_date) as year,
                EXTRACT(MONTH FROM source_date) as month,
                SUM(amount) as total 
            FROM expense 
            WHERE EXTRACT(YEAR FROM source_date) = {year_int}
            GROUP BY source, category, EXTRACT(YEAR FROM source_date), EXTRACT(MONTH FROM source_date)
            ORDER BY category, source, year, month
        """
    
    # Execute queries
    income_results = run_query(income_query)
    expense_results = run_query(expense_query)
    
    # Combine results
    all_data = []
    
    # Process income data
    for row in income_results:
        type_val, source, category, year_val, month_val, total = row
        if not categories or category in categories:
            all_data.append({
                'type': type_val,
                'source': source,
                'category': category,
                'year': int(year_val),
                'month': int(month_val),
                'amount': float(total)
            })
    
    # Process expense data
    for row in expense_results:
        type_val, source, category, year_val, month_val, total = row
        if not categories or category in categories:
            all_data.append({
                'type': type_val,
                'source': source,
                'category': category,
                'year': int(year_val),
                'month': int(month_val),
                'amount': float(total)
            })
    
    if not all_data:
        # Return empty DataFrame
        return pd.DataFrame()
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Create year-month combinations and sort them in ascending order
    df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2)
    available_months = sorted(df['year_month'].unique())
    
    # Pivot data to have year-months as columns
    pivot_df = df.pivot_table(
        index=['type', 'category', 'source'], 
        columns='year_month', 
        values='amount', 
        fill_value=0,
        aggfunc='sum'
    ).reset_index()
    
    # Calculate total amount for each source (sum across all months) for sorting
    pivot_df['total_amount'] = pivot_df[available_months].sum(axis=1)
    
    # Apply same sorting logic as yearly budget
    def custom_sort_key(series):
        if series.name == 'type':
            return series.map({'Income': 0, 'Expense': 1})
        elif series.name == 'category':
            # Custom category ordering for expenses: taxes, needs, wants, investments
            expense_category_order = {
                'taxes': 0,
                'needs': 1, 
                'wants': 2,
                'investments': 3
            }
            sort_values = []
            for idx, category in enumerate(series):
                row = pivot_df.iloc[idx]
                if row['type'] == 'Expense' and category in expense_category_order:
                    sort_values.append(expense_category_order[category])
                else:
                    sort_values.append(category)  # Keep original order for income categories
            return sort_values
        elif series.name == 'source':
            # For sources, sort by negative total_amount for earned_income and passive_income categories
            # This will give descending order by amount
            sort_values = []
            for idx, source in enumerate(series):
                row = pivot_df.iloc[idx]
                if row['category'] in ['earned_income', 'passive_income']:
                    sort_values.append(-row['total_amount'])  # Negative for descending
                elif row['category'] == 'wants':
                    # For wants category: subscriptions first, then alphabetical
                    if 'subscription' in source.lower():
                        sort_values.append(f"0_{source}")  # Prefix with 0 to sort first
                    else:
                        sort_values.append(f"1_{source}")  # Prefix with 1 to sort after subscriptions
                else:
                    sort_values.append(source)  # Alphabetical for other categories
            return sort_values
        else:
            return series
    
    pivot_df = pivot_df.sort_values(['type', 'category', 'source'], key=custom_sort_key)
    
    # Remove the temporary total_amount column
    pivot_df = pivot_df.drop('total_amount', axis=1)
    
    # Prepare final DataFrame for editing with separator rows between categories
    # Create month column names first
    month_column_names = []
    for month_col in available_months:
        year, month = month_col.split('-')
        month_name = calendar.month_abbr[int(month)]
        col_name = f"{month_name} {year}"
        month_column_names.append(col_name)
    
    # Build the final DataFrame with separator rows
    final_rows = []
    current_type = None
    current_category = None
    
    for _, row in pivot_df.iterrows():
        row_type = row['type']
        row_category = row['category']
        
        # Add separator row if this is a new category
        if current_category is not None and row_category != current_category:
            # Add empty separator row
            separator_row = {
                'type': '',
                'category': '',
                'source': ''
            }
            # Add empty values for all month columns
            for month_col in available_months:
                year, month = month_col.split('-')
                month_name = calendar.month_abbr[int(month)]
                col_name = f"{month_name} {year}"
                separator_row[col_name] = ''
            final_rows.append(separator_row)
        
        # Add the actual data row
        data_row = {
            'type': row_type,
            'category': row_category.replace('_', ' ').title(),
            'source': row['source'].replace('_', ' ').title()
        }
        # Add month data
        for month_col in available_months:
            year, month = month_col.split('-')
            month_name = calendar.month_abbr[int(month)]
            col_name = f"{month_name} {year}"
            # Format as USD currency without decimals
            amount = round(row[month_col])
            if amount != 0:
                data_row[col_name] = f"${amount:,}"
            else:
                data_row[col_name] = ""
        
        final_rows.append(data_row)
        
        # Update current tracking variables
        current_type = row_type
        current_category = row_category
    
    # Create DataFrame from the rows
    final_df = pd.DataFrame(final_rows)
    
    return final_df


def update_monthly_budget_data(original_df, edited_df):
    """
    Update the database with changes from the edited monthly budget DataFrame.
    
    Args:
        original_df: Original DataFrame before editing
        edited_df: DataFrame after user edits
    """
    
    # Find the month columns (everything after 'source')
    month_columns = [col for col in edited_df.columns if col not in ['type', 'category', 'source']]
    
    # Compare original vs edited data to find changes
    changes = []
    
    for idx, row in edited_df.iterrows():
        # Skip empty separator rows
        if row['type'] == '' or row['category'] == '' or row['source'] == '':
            continue
            
        if idx < len(original_df):  # Make sure the row exists in original
            original_row = original_df.iloc[idx]
            
            # Skip if original row is also a separator
            if original_row['type'] == '' or original_row['category'] == '' or original_row['source'] == '':
                continue
            
            for month_col in month_columns:
                original_value = original_row[month_col] if month_col in original_row else 0
                edited_value = row[month_col]
                
                # Skip empty values in month columns
                if edited_value == '' or original_value == '':
                    continue
                
                # Parse currency strings back to float values
                def parse_currency(value):
                    if isinstance(value, str):
                        # Remove $ and commas, then convert to float
                        return float(value.replace('$', '').replace(',', '')) if value.strip() else 0
                    return float(value) if value else 0
                
                original_amount = parse_currency(original_value)
                edited_amount = parse_currency(edited_value)
                
                if abs(original_amount - edited_amount) > 0.01:  # Changed value
                    # Parse month and year from column name (e.g., "Jan 2024")
                    month_name, year = month_col.split(' ')
                    month_num = list(calendar.month_abbr).index(month_name)
                    
                    # Convert formatted names back to database format (snake_case)
                    db_category = row['category'].lower().replace(' ', '_')
                    db_source = row['source'].lower().replace(' ', '_')
                    
                    changes.append({
                        'type': row['type'],
                        'category': db_category,
                        'source': db_source,
                        'year': int(year),
                        'month': month_num,
                        'old_amount': original_amount,
                        'new_amount': edited_amount
                    })
    
    # Apply changes to database
    for change in changes:
        table_name = 'income' if change['type'] == 'Income' else 'expense'
        
        # Check if record exists for this source/category/year/month
        check_query = f"""
            SELECT COUNT(*) FROM {table_name} 
            WHERE source = %s AND category = %s 
            AND EXTRACT(YEAR FROM source_date) = %s 
            AND EXTRACT(MONTH FROM source_date) = %s
        """
        
        existing = run_query(check_query, (
            change['source'], 
            change['category'], 
            change['year'], 
            change['month']
        ))
        
        if existing and existing[0][0] > 0:
            # Update existing record
            update_query = f"""
                UPDATE {table_name} 
                SET amount = %s 
                WHERE source = %s AND category = %s 
                AND EXTRACT(YEAR FROM source_date) = %s 
                AND EXTRACT(MONTH FROM source_date) = %s
            """
            run_query(update_query, (
                change['new_amount'],
                change['source'],
                change['category'], 
                change['year'],
                change['month']
            ))
        else:
            # Insert new record (if new_amount > 0)
            if change['new_amount'] > 0:
                # Create a date for the first day of the month
                source_date = f"{change['year']}-{change['month']:02d}-01"
                insert_query = f"""
                    INSERT INTO {table_name} (source, category, amount, source_date)
                    VALUES (%s, %s, %s, %s)
                """
                run_query(insert_query, (
                    change['source'],
                    change['category'],
                    change['new_amount'],
                    source_date
                ))
    
    return len(changes)  # Return number of changes made


def get_monthly_budget(year=None, categories=None):
    """
    Streamlit component for editable monthly budget table.
    
    Args:
        year: Optional year filter (string or int for single year)
        categories: Optional list of categories to filter
    
    Returns:
        Streamlit data_editor component
    """
    
    # Get the data
    df = get_monthly_budget_data(year, categories)
    
    if df.empty:
        st.write("No data available for the selected filters.")
        return None
    
    # Create the editable table
    st.write("### Monthly Budget (Editable)")
    st.write("Edit values directly in the table. Changes will be saved to the database.")
    
    # Create column configurations
    column_config = {
        "type": st.column_config.SelectboxColumn(
            "Type",
            options=["Income", "Expense"],
            disabled=True
        ),
        "category": st.column_config.TextColumn("Category", disabled=True),
        "source": st.column_config.TextColumn("Source", disabled=True),
    }
    
    # Add currency column configuration for month columns
    month_columns = [col for col in df.columns if col not in ['type', 'category', 'source']]
    for month_col in month_columns:
        column_config[month_col] = st.column_config.TextColumn(
            month_col,
            help="Enter amount as $1,000 or just 1000"
        )
    
    # Use data_editor for editable table
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        column_config=column_config,
        disabled=["type", "category", "source"],  # Make first 3 columns read-only
        key="monthly_budget_editor"
    )
    
    # Add save button
    if st.button("Save Changes", type="primary"):
        try:
            changes_count = update_monthly_budget_data(df, edited_df)
            if changes_count > 0:
                st.success(f"✅ Successfully saved {changes_count} changes to the database!")
                # Small delay to show the message before rerun
                time.sleep(5)
                st.rerun()  # Refresh the data
            else:
                st.info("ℹ️ No changes detected.")
                # Small delay to show the message before rerun
                time.sleep(5)
        except Exception as e:
            st.error(f"❌ Error saving changes: {str(e)}")
            # Small delay to show the message before rerun
            time.sleep(5)
    
    return edited_df
