# This script make one analysis of the 
# InFlow and OutFlow in exchanges (From-To)
# -> unknown-unknown
# -> unknwon-exchange
# -> exchange-exchange
# -> exchange-unknown

# Author: @andvsilva 2022-01-25

# libraries
import snoop
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from icecream import ic
import requests
import os
import time
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime as dt
from icecream import ic
import notify2

def notify(order, symbol_currency, now):
    
    ICON_PATH = "../images/btc.jpg" # This is not working, FIXME, I do not know why.

    # initialise the d-bus connection
    notify2.init("Cryptocurrency reach the price")

    # create Notification object
    n = notify2.Notification("Crypto Notifier", icon = ICON_PATH)

    # Set the urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)

    # Set the timeout
    n.set_timeout(1000)

    # Update the content
    n.update(f"{now}", order)

    # Show the notification
    n.show()

coindesk_api = 'https://production.api.coindesk.com/v1/currency/ticker?currencies=BTC'

# set the theme to the seaborn
sns.set_theme(style="darkgrid")

# set figure, canvas and subplots
fig, ax = plt.subplots(figsize = (10, 7))
fig.canvas.manager.set_window_title("On-Chain Analysis")
fig.subplots_adjust(top = 0.93, right = 0.9, bottom = 0.1, left = 0.1)

# update plot in a loop
#@snoop
def update(i):
    # get the date - time: YYYY-MM-DD HH:M:S
    now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    
    # loading data feather format
    database_txo = pd.read_csv('../dataset/database_txo.csv')
    
    # delete all the rows with NaN
    database_txo = database_txo.dropna()
    
    # get BTC price in USD
    data_BTC = requests.get(coindesk_api).json()
    
    # parsing and set precision...
    price_btc = round(data_BTC['data']['currency']['BTC']['quotes']['USD']['price'], 2)
    change24h_pct = round(data_BTC['data']['currency']['BTC']['quotes']['USD']['change24Hr']['percent'],2)
    
    # BTC only
    database_txo_btc = database_txo.loc[(database_txo['blockchain'] == 'BTC')]
    
    stats_from_to = database_txo_btc['from_to'].value_counts(normalize=True).map('{:.2%}'.format)
    stats_from_to = dict(stats_from_to)
    
    coins_txos = database_txo_btc[['from_to','amount_coin','amount_usd']]
    
    from_to_stat = {}
    
    from_tos = []
    for ifrom_to in stats_from_to:
        from_to_stat[f'{ifrom_to}'] = float(stats_from_to[ifrom_to][:-1])
        from_tos.append(f'{ifrom_to}')
    
    amount_coins_txos = {}
    
    for from_to in from_tos:
        amount_coins = coins_txos.loc[(coins_txos["from_to"] == f'{from_to}'), 'amount_coin'].sum()
        amount_coins_txos[f'{from_to}'] = amount_coins
    
    # amount   
    #ic(amount_coins_txos)        
                
    # dataframe price and date - history
    btc = pd.read_csv('../dataset/price_date.csv')
    
    # convert object to pandas datetime feature.
    btc['date'] = pd.to_datetime(btc['date'])
    
    ymax_lim = btc['price_btc'].max()
    ymin_lim = btc['price_btc'].min()
    
    #coin_max = database_txo_btc['amount_coin']
    #usd_max = database_txo_btc['amount_usd']
    #
    #idxmax = coin_max.idxmax()
    #
    #coin_max = coin_max.max()
    #usd_max = usd_max.max()
    #
    #date_max = database_txo_btc.loc[idxmax, 'date']
    #from_to = database_txo_btc.loc[idxmax, 'from_to']
    #print(f'txo ({from_to})-> amount:  {coin_max} BTC ($ {usd_max}) USD date: {date_max}')
    
    ax.cla()
    plt.xticks(rotation=0)
    plt.grid(True)
    
    sns.lineplot(data=btc, x="date", y="price_btc", color='orange')
        
    ax.set_title(f'{now}    1 BTC - ${price_btc} USD - change 24h: {change24h_pct}%', fontsize = 16, color='red')
    ax.set_ylabel('price (USD)')
    ax.set_ylim(0.997*ymin_lim, 1.006*ymax_lim)
    ax.yaxis.label.set_color('black')
    ax.yaxis.label.set_fontsize(14)
    ax.tick_params(axis='y', colors='black', labelsize=14)
    ax.legend(['BTC'], loc="upper left")
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d  %H:%M:%S'))
    
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.1)
    
    xmin, xmax, ymin, ymax = plt.axis()
    
    x_mean = (xmax+xmin)/2
    y_mean = (ymax+ymin)/2
    
    xscale = 1.000055
    yscale = 1.05
    diff_space=0
    
    for ifrom_to in from_to_stat:
        coins_txos = round(amount_coins_txos[f'{ifrom_to}'], 4)
        plt.text(x_mean*xscale, 0.989*ymax_lim-diff_space, f'{ifrom_to}: {from_to_stat[ifrom_to]} % ({coins_txos} BTC)', fontsize = 14)
        diff_space -= 140
    
            
    #plt.text(x_mean-0.016, 0.99*price_btc+diff_space, f'{now}    1 BTC - ${price_btc} USD - change 24h: {change24h_pct}%', dict(size=14), color = 'black')
    txo_max_fromtos = []
    ysprad = 0
    
    icolor=0
    colors = ['red', 'green', 'blue', 'black']
    
    for ifrom_to in from_tos:
        txo_from_to = database_txo_btc.loc[(database_txo_btc['from_to'] == f'{ifrom_to}')]
        coin_max = txo_from_to['amount_coin']
        usd_max = txo_from_to['amount_usd']

        idxmax = coin_max.idxmax()
        coin_max = round(coin_max.max(),2)
        usd_max = usd_max.max()
        
        date_max = database_txo_btc.loc[idxmax, 'date']
        from_to = database_txo_btc.loc[idxmax, 'from_to']
        
        txo_max_fromtos.append(f'({from_to}): {coin_max} BTC {date_max}')
        
        year  = int(date_max[0:4])
        month = int(date_max[5:7])
        day   = int(date_max[8:10])
        
        # time
        HH = int(date_max[11:13])
        MM = int(date_max[14:16])
        SS = int(date_max[17:19])
        
        color = colors[icolor]
        
        symbol_currency = 'BTC'
        
        #if(coin_max > 1000):
        #
        #    if(f'{from_to}' == 'exchange-unknown'):
        #        order = 'Buy now!'
        #        notify(order, symbol_currency, now)
        #        
        #    if(f'{from_to}' == 'unknown-exchange'):
        #        order = 'Sell now!'
        #        notify(order, symbol_currency, now)
        
        plt.axvline(pd.Timestamp(f'{year}-{month}-{day} {HH}:{MM}:{SS}'), ymin=0.05, ymax=0.58, color = f'{color}', linestyle='--', linewidth=1)
        plt.text(pd.Timestamp(f'{year}-{month}-{day} {HH}:{MM}:{SS}'), 0.999*ymin_lim+ysprad, f' {from_to}:  {coin_max} BTC - {date_max}', fontsize = 11, color=f'{color}')    
        ysprad += 60
        icolor += 1 
        
    #plt.text(pd.Timestamp(f'{year}-{month}-{day} {HH}:{MM}:{SS}'), 0.998*ymin_lim, f' ({from_to}):  {coin_max} BTC - {date_max}', fontsize = 12, color='red')
    #plt.vlines(x=x_mean, ymin = ymin_lim, ymax= ymax_lim, colors='teal', ls='--', lw=2, label='vline_multiple - partial height')
    plt.savefig("../images/price_btc_ioflow.pdf", dpi=150)
    plt.savefig("../images/price_btc_ioflow.png", dpi=150)
    plt.grid(True)
    #time.sleep(10)

ani = animation.FuncAnimation(fig, update, frames = 10)

    
plt.show()