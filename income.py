from db import *
import pandas as pd # type: ignore
import plotly.express as px # type: ignore
import plotly.io as pio # type: ignore


connection = connect_to_db()
df = pd.read_sql('select * from income', con=connection)
df['source_date'] = pd.to_datetime(df['source_date'])
df['year'] = df['source_date'].dt.year


def get_income_sources():
    return df['source'].unique()


def get_income_categories():
    return df['category'].unique()


def get_income_ts(income_sources=None, income_categories=None, group_by_year=False):
    x = 'source_date'
    data = df
    title = 'Income over Time'
    line_group = None

    if income_sources and group_by_year:
        data = df[df['source'].isin(income_sources)].groupby(by=["source", "year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Income by {', '.join(income_sources).title().replace('_', ' ')} and Year"
        line_group = 'source'
    elif income_sources and not group_by_year:
        data = df[df['source'].isin(income_sources)].groupby(by=["source", x], as_index=False).agg({"amount": "sum"})
        title = f"Income by {', '.join(income_sources).title().replace('_', ' ')}"
        line_group = 'source'
    elif not income_sources and not income_categories and group_by_year:
        data = df.groupby(by=["year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Income by Year"
    elif not income_sources and income_categories and not group_by_year:
        data = df[df['category'].isin(income_categories)].groupby(by=["category",x], as_index=False).agg({"amount": "sum"})
        title = f"Income by {', '.join(income_categories).title().replace('_', ' ')}"
        line_group = 'category'
    elif not income_sources and income_categories and group_by_year:
        data = df[df['category'].isin(income_categories)].groupby(by=["category", "year"], as_index=False).agg({"amount": "sum"})
        x = 'year'
        title = f"Income by {', '.join(income_categories).title().replace('_', ' ')} and Year"
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
    