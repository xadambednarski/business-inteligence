import pandas as pd
import requests
import json


def import_data(curr, dates):
    start, end = dates
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{curr}/{start}/{end}/'
    response_api = requests.get(url)
    data = response_api.text.encode().decode('utf-8-sig') 
    parse_json = json.loads(data)
    df = pd.DataFrame(parse_json)
    return df


def clean_data(df):
    df['rates'].apply(pd.Series)
    df = pd.concat([df, df['rates'].apply(pd.Series)], axis=1)
    df.drop(columns=['rates','table'], inplace=True)
    return df


currency = 'usd'
daterange = ('2022-01-01', '2023-01-01')
data = import_data(currency, daterange)
rates = clean_data(data)



dates = pd.date_range(start='2022-01-01', end='2023-01-01')
dates = pd.to_datetime(dates, format='%Y-%d-%m')
dates = pd.DataFrame(dates)
dates=dates.astype(str)
df3 = pd.merge(rates, dates, how = 'outer', left_on = ['effectiveDate'], right_on=0)
df3.fillna(method='ffill')
print(df3)
