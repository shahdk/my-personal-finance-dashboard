from db import *
from constants import *
import plotly.express as px # type: ignore
import pandas as pd # type: ignore
import math
import random


iso_code = []
start_date = []
end_date = []
city = []
latitude = []
longitude = []
amount = []
year = []


query = "select * from vacation"
results = run_query(query)


for result in results:
    iso_code.append(result[0])
    start_date.append(result[1])
    end_date.append(result[2])
    city.append(result[3])
    latitude.append(result[4])
    longitude.append(result[5])
    amount.append(float(math.ceil(result[6])))


vacations = {
    'iso_code': iso_code,
    'Visit Date': start_date,
    'City': city,
    'lat': latitude,
    'lon': longitude,
    'Cost': amount,
}


vacation_df = pd.DataFrame(vacations)
vacation_df['Visit Date'] = pd.to_datetime(vacation_df['Visit Date'])
vacation_df['Year'] = vacation_df['Visit Date'].dt.year

# Create grouped DataFrame for the map (group by location)
vacation_map_df = vacation_df.groupby(['City', 'lat', 'lon', 'iso_code']).agg({
    'Cost': 'sum',
    'Visit Date': lambda x: ', '.join(x.dt.strftime('%Y-%m-%d').sort_values())
}).reset_index()
vacation_map_df.rename(columns={'Visit Date': 'Visit Dates'}, inplace=True)


def get_vacation_map():
    fig = px.scatter_geo(vacation_map_df,
                        lat="lat",
                        lon="lon",
                        color="Cost", # which column to use to set the color of markers
                        hover_name="City", # column added to hover information
                        hover_data=["Visit Dates"], # show all visit dates in hover
                        size="Cost", # size of markers
                        projection="natural earth")
    return fig


def get_vacation_ts():
    fig = px.bar(vacation_df, x='Year', y='Cost', hover_data=['City'], color='City')
    fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.3s')
    return fig