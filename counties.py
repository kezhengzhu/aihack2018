import pandas as pd
import numpy as np

poverty = pd.read_csv('/Users/Alex/Dropbox/python/aihack2018/california/train/ln-X17_POVERTY.csv')
income = pd.read_csv('/Users/Alex/Dropbox/python/aihack2018/california/train/ln-X19_INCOME.csv')
earnings = pd.read_csv('/Users/Alex/Dropbox/python/aihack2018/california/train/ln-X20_EARNINGS.csv')

df = pd.read_excel('/Users/Alex/Dropbox/python/geocodes.xlsx',sheet='Sheet1', dtype={'FIPS code':object})

df.head()

counties = df[['County','FIPS code']]

poverty['FIPS code'] = poverty['GEOID'].apply(lambda geocode: geocode[9:12])
poverty = poverty.merge(counties, on='FIPS code', how='left')

poverty['County'].value_counts()
