import requests
import pandas as pd
import json
import seaborn as sns
from matplotlib import pyplot as plt 


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


def visualize(df):
    sns.set_style("darkgrid")
    plot = sns.lineplot(data=df, x='effectiveDate', y='mid')
    plot.set(xlabel='time', ylabel='rate',
             title='Currency rate change in time')
    plt.show()


currency = 'usd'
dates = ('2022-01-03', '2023-01-03')
data = import_data(currency, dates)
exchange_rates_USD = clean_data(data)
visualize(exchange_rates_USD)
