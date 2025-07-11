from db import *
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import plotly.io as pio # type: ignore


connection = connect_to_db()
df = pd.read_sql('select * from expense', con=connection)
df['source_date'] = pd.to_datetime(df['source_date'])
df['year'] = df['source_date'].dt.year


def get_expense_sources():
    return df['source'].unique()


def get_expense_categories():
    return df['category'].unique()



def get_expense_ts(expense_sources=None, expense_categories=None, group_by_year=False):
    x = 'source_date'
    data = df
    title = 'Expense over Time'
    line_group = None

    if expense_sources and group_by_year:
        data = df[df['source'].isin(expense_sources)].groupby(by=["source", "year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Expense by {', '.join(expense_sources).title().replace('_', ' ')} and Year"
        line_group = 'source'
    elif expense_sources and not group_by_year:
        data = df[df['source'].isin(expense_sources)].groupby(by=["source", x], as_index=False).agg({"amount": "sum"})
        title = f"Expense by {', '.join(expense_sources).title().replace('_', ' ')}"
        line_group = 'source'
    elif not expense_sources and not expense_categories and group_by_year:
        data = df.groupby(by=["year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Expense by Year"
    elif not expense_sources and expense_categories and not group_by_year:
        data = df[df['category'].isin(expense_categories)].groupby(by=["category", x], as_index=False).agg({"amount": "sum"})
        title = f"Expense by {', '.join(expense_categories).title().replace('_', ' ')}"
        line_group = 'category'
    elif not expense_sources and expense_categories and group_by_year:
        data = df[df['category'].isin(expense_categories)].groupby(by=["category", "year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Expense by {', '.join(expense_categories).title().replace('_', ' ')} and Year"
        line_group = 'category'
    else:
        data = df.groupby(by=["source_date"], as_index=False).agg({"amount": "sum"})
    
    fig = px.bar(data, x=x, y='amount', title=title, barmode='group', color=line_group)
    fig.update_layout(
        yaxis=dict(
            tickprefix="$",  # Add a dollar sign prefix
            tickformat=",.2f"  # Format to two decimal places
        )
    )

    return fig
    