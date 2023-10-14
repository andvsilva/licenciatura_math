"""
70f5bb9b1ca4afacee9d96f8200aedf301fb909917f3e49350ca45bdd867b97e API 

# A tutorial for this file will soon be available at www.relataly.com

# Tested with Python 3.9.13, 
Matplotlib 3.5.2, 
Seaborn 0.11.2, 
numpy 1.21.5, plotly 4.1.1, 
cryptocompare 0.7.6

https://www.relataly.com/seven-metrics-for-on-chain-analysis-in-python/10098/

"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import date, timedelta, datetime
import seaborn as sns
sns.set_style('white', {'axes.spines.right': True, 'axes.spines.top': False})
import cryptocompare as cc
import requests
import IPython
import yaml
import json

# Set the API Key from a yaml file
#yaml_file = open('apis/api_config_cryptocompare.yml', 'r')  
#p = yaml.load(yaml_file, Loader=yaml.FullLoader)
#api_key = p['api_key'] 
# alternatively if you have not stored your API key in a separate file
api_key = '70f5bb9b1ca4afacee9d96f8200aedf301fb909917f3e49350ca45bdd867b97e'

# Number of past days for which we retrieve data
data_limit = 2000

# Define coin symbols
symbol_a = 'BTC'
symbol_b = 'ETH'

# Query price data

# Generic function for an API call to a given URL
def api_call(url):
  # Set API Key as Header
  headers = {'authorization': 'Apikey ' + api_key,}
  session = requests.Session()
  session.headers.update(headers)

  # API call to cryptocompare
  response = session.get(url)

  # Conversion of the response to dataframe
  historic_blockdata_dict = json.loads(response.text)
  df = pd.DataFrame.from_dict(historic_blockdata_dict.get('Data').get('Data'), orient='columns', dtype=None, columns=None)
  return df

def prepare_pricedata(df):
  df['date'] = pd.to_datetime(df['time'], unit='s')
  df.drop(columns=['time', 'conversionType', 'conversionSymbol'], inplace=True)
  return df

# Load the price data
base_url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym='
df_a = api_call(f'{base_url}{symbol_a}&tsym=USD&limit={data_limit}')
coin_a_price_df = prepare_pricedata(df_a)

df_b = api_call(f'{base_url}{symbol_b}&tsym=USD&limit={data_limit}')
coin_b_price_df = prepare_pricedata(df_b)


#print(coin_a_price_df)

# Query on-chain data

# Prepare the onchain dataframe
def prepare_onchain_data(df):
  # replace the timestamp with a data and filter some faulty values
  df['date'] = pd.to_datetime(df['time'], unit='s')
  df.drop(columns='time', inplace=True)
  df = df[df['hashrate'] > 0.0]
  return df
  
base_url = 'https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym='
onchain_symbol_a_df = api_call(f'{base_url}{symbol_a}&limit={data_limit}')
onchain_symbol_b_df = api_call(f'{base_url}{symbol_b}&limit={data_limit}')

# Filter some faulty values
onchain_symbol_a_df = onchain_symbol_a_df[onchain_symbol_a_df['hashrate'] > 0.0]
onchain_symbol_a_df.head(3)

# Lineplot Helper Functions

# Adding moving averages
rolling_window = 25
coin_a_price_df['close_avg'] = coin_a_price_df['close'].rolling(window=rolling_window).mean() 
coin_b_price_df['close_avg'] = coin_b_price_df['close'].rolling(window=rolling_window).mean() 

# This function adds bitcoin halving dates as vertical lines
def add_halving_dates(ax, df_x_dates, df_ax1_y):
    halving_dates = ['2009-01-03', '2012-11-28', '2016-07-09', '2020-05-11', '2024-03-12', '2028-06-01'] 
    dates_list = [datetime.strptime(date, '%Y-%m-%d').date() for date in halving_dates]
    for i, datex in enumerate(dates_list):
        halving_ts = pd.Timestamp(datex)
        x_max = df_x_dates.max() + timedelta(days=365)
        x_min = df_x_dates.min() - timedelta(days=365)
        if (halving_ts < x_max) and (halving_ts > x_min):
            ax.axvline(x=datex, color = 'purple', linewidth=1, linestyle='dashed')
            ax.text(x=datex  + timedelta(days=20), y=df_ax1_y.max()*0.99, s='BTC Halving ' + str(i) + '\n' + str(datex), color = 'purple')

# This function creates a nice legend for twinx plots
def add_twinx_legend(ax1, ax2, x_anchor=1.18, y_anchor=1.0):
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc=1, facecolor='white', framealpha=0, bbox_to_anchor=(x_anchor, y_anchor))
    ax2.get_legend().remove()

# Create the lineplot
fig, ax1 = plt.subplots(figsize=(16, 6))
sns.lineplot(data=coin_a_price_df, x='date', y='close', color='cornflowerblue', linewidth=0.5, label=f'{symbol_a} close price', ax=ax1)
sns.lineplot(data=coin_a_price_df, x='date', y='close_avg', color='blue', linestyle='dashed', linewidth=1.0, 
    label=f'{symbol_a} {rolling_window}-MA', ax=ax1)
ax1.set_ylabel(f'{symbol_a} Prices')
ax1.set(xlabel=None)
ax2 = ax1.twinx()
sns.lineplot(data=coin_b_price_df, x='date', y='close', color='lightcoral', linewidth=0.5, label=f'{symbol_b} close price', ax=ax2)
sns.lineplot(data=coin_b_price_df, x='date', y='close_avg', color='red', linestyle='dashed', linewidth=1.0, 
    label=f'{symbol_b} {rolling_window}-MA', ax=ax2)
ax2.set_ylabel(f'{symbol_b} Prices')
add_twinx_legend(ax1, ax2, 0.98, 0.2)
add_halving_dates(ax1, coin_a_price_df.date, coin_a_price_df.close)
#ax1.set_yscale('log'), ax2.set_yscale('log')
plt.title(f'Prices of {symbol_a} and {symbol_b}')
#plt.show()

# Prepare the onchain dataframe
def prepare_onchain_data(df):
  # replace the timestamp with a data and filter some faulty values
  df['date'] = pd.to_datetime(df['time'], unit='s')
  df.drop(columns='time', inplace=True)
  df = df[df['hashrate'] > 0.0]
  return df

# Load onchain data for Bitcoin
print('Load onchain data for Bitcoin...')
base_url = 'https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym='
df_a = api_call(f'{base_url}{symbol_a}&limit={data_limit}')
onchain_symbol_a_df = prepare_onchain_data(df_a)

coin_a_price_df = coin_a_price_df.drop(columns=['close_avg'])

#print(coin_a_price_df)
#print(onchain_symbol_a_df)

df_btc = pd.concat([coin_a_price_df, onchain_symbol_a_df], axis=1)
df_btc = df_btc.dropna()


df_btc = df_btc.loc[:,~df_btc.T.duplicated()]

print(df_btc)

df_btc.to_csv('onchain_data_btc.csv', index=False)