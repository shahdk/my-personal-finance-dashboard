from db import *
from constants import *


def get_income_data(year=None):
    # Income sources
    query = "select source, category, CEILING(sum(amount)) as total from income group by source, category order by total desc"
    if year:
        query = f"""
            select source, category, CEILING(sum(amount)) as total 
            from income
            where source_date BETWEEN '{year}-01-01' and '{year}-12-01'
            group by source, category order by total desc
            """    
    results = run_query(query)

    amounts = []
    total = 0
    
    amount_mappings = {
        'paycheck_person1': 0,
        'paycheck_person2': 0, 
        'stocks': 0,
        'cash_bonus': 0, 
        'interest_income': 0,
        'dividends': 0,
        'capital_gains': 0,
        'earned_income': 0,
        'passive_income': 0
    }
    
    earned_total = 0
    passive_total = 0
    dividend_total = 0
    capital_gains_total = 0
    for result in results:
        source = str(result[0])
        category = str(result[1])
        amount = float(result[2])
        
        
        total = total + amount
        if category == 'passive_income':
            passive_total = passive_total + amount
        else:
            earned_total = earned_total + amount

        if source == 'qualifying_dividends' or source == 'ordinary_dividends':
            dividend_total = dividend_total + amount
        if source == 'long_term_gains' or source == 'short_term_gains':
            capital_gains_total = capital_gains_total + amount
        else:
            amount_mappings[source] = amount
        

    amount_mappings['dividends'] = dividend_total
    amount_mappings['capital_gains'] = capital_gains_total
    amount_mappings['earned_income'] = earned_total
    if capital_gains_total < 0:
        passive_total = passive_total + (-1 * capital_gains_total)
    amount_mappings['passive_income'] = passive_total

    for link in links:
        if link['source'] in amount_mappings:
            amounts.append(amount_mappings[link['source']])

    amount_mappings['total_income'] = total
    return amounts, amount_mappings