from db import *
from constants import *


def get_expense_data(year=None):

    query = "select category, CEILING(sum(amount)) as total from expense group by category"
    if year:
        query = f"""
            select category, CEILING(sum(amount)) as total 
            from expense
            where source_date BETWEEN '{year}-01-01' and '{year}-12-01'
            group by category
            """    
    
    results = run_query(query)

    take_home = 1
    discretionary = 0
    amount_mappings = {
        'taxes': 0,
        'needs': 0,
        'investments': 0,
        'wants': 0,
        'take_home': 0,
        'discretionary': 0
    }

    amounts = []

    for result in results:
        category = str(result[0])
        amount = float(result[1])
        if not year or year == '2023':
            amount = amount - 150561 if category == 'investments' else amount
        
        amount_mappings[category] = amount
        if category != 'taxes':
            take_home = take_home + amount
        if category == 'investments' or category == 'wants':
            discretionary = discretionary + amount


    amount_mappings['take_home'] = take_home
    amount_mappings['discretionary'] = discretionary

    for link in links:
        if link['target'] in amount_mappings:
            amounts.append(amount_mappings[link['target']])

    return amounts, amount_mappings