import pandas as pd

# get raw data
df = pd.read_csv('aihack2018/cleanedSimpleData.csv')
counties_raw = pd.read_excel('aihack2018/geocodes.xlsx',sheet='Sheet1', dtype={'FIPS code':object})
counties = counties_raw[['County','FIPS code']]

# append FIPS code and County onto df
df['FIPS code'] = df['GEOID'].apply(lambda geocode: geocode[8:12])
df = df.merge(counties, on='FIPS code', how='left')

# prepare plot data
plot_data = df['FIPS code'].value_counts().rename_axis('FIPS').reset_index(name='value')
fips = plot_data['FIPS'].tolist()
values = plot_data['value'].tolist()

import plotly
import plotly.figure_factory as ff
plotly.tools.set_credentials_file(username='alexdurkin96',api_key='zJzMmH3OL1gS7VAloYne')

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    binning_endpoints=[10, 50, 100, 500, 1000, 1500, 5000], colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Number of data points', title='Distribution of data'
)
plotly.plotly.iplot(fig, filename='choropleth_california_and_surr_states_outlines')
