'''
#####################################################################
>>>>>>>>>>>>>  SCRAPE INFO WHALE ALERT <<<<<<<<<<<<<<
This script will make the scrape the Blockchain 
data from the Whale Alert API by using
the python package from Whale Alert:

- https://pypi.org/project/whale-alert/

to install: pip install whale-alert.

The history of transactions will be stored in
one CSV file. To organize the dataset, I will 
create three files:

1 - store ALL the history of transactions 
   -- ALL coins
2 - store the BTC history transactions data.

# Basic Usage:
$ cd whale-alert/source-code/
$ python scrapewhale.py

Or script shell to run forever, if
you get a error, the script will run again
scrapewhale.py

cd whale-alert/script-shell
$ source runscrape.sh

>>> Author: @andvsilva 2022-04-21 10h
#####################################################################
'''

# libraries
import os
import time
from whalealert.whalealert import WhaleAlert
import pandas as pd
from datetime import datetime
import sys
import toolkit as tool
from colored import fore, back, style
import requests

coindesk_api = 'https://production.api.coindesk.com/v1/currency/ticker?currencies=BTC'

# To print colored text in python 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# API key for Whale Alert
# When you are going to use this key maybe something can go wrong, 
# please generate your own key -> https://whale-alert.io/signup
api_key = 'jlo1G5L7K4CBNcw557uOGOzDrq1i7Oca'

# limit of transactions per request - free plan
transaction_count_limit = 1

# WhaleAlert object
whale = WhaleAlert()
WhaleFund = False

# variables
index = 0
id = 0
idx = 0

# column names for the transaction
txo_columns_btc = ['blockchain',
                   'amount_coin',
                   'amount_usd',
                   'hash',
                   'from_to',
                   'id',
                   'date',
                   'price',
                   'change24h_pct']

# columns for the dataset ALL coins
txo_columns = txo_columns_btc[:]

# remove the column names 'price' and 'change24h_pct' -> BTC
del txo_columns[7:]

# The game start here! let's go!
# this loop will collect data for each request
while True:
    
    # Specify a single transaction from the last 10 minutes - free plan
    start_time = int(time.time() - 600)
    success, transaction, status = whale.get_transactions(start_time, 
                                                           api_key=api_key, 
                                                           limit=transaction_count_limit)
    
    # check if the get transactions was sucessfully
    if (success == 'False'):
        print(f'Status request: {status}')
        print("exit now, something is wrong with the request from the Whale API")
        sys.exit() # Abort the job now!
        
    # convert list of dict to dict
    txo = dict((key,d[key]) for d in transaction for key in d)
    
    # date and time of the transaction
    date_txo = datetime.fromtimestamp(txo['timestamp'])
    
    # dataset with the transactions
    database_txo_btc = pd.DataFrame(columns=txo_columns_btc) # BTC only
    database_txo = pd.DataFrame(columns=txo_columns) # ALL coins - available
    
    # get BTC price in USD
    data_BTC = requests.get(coindesk_api).json()
    price_btc = round(data_BTC['data']['currency']['BTC']['quotes']['USD']['price'], 2)
    change24h_pct = round(data_BTC['data']['currency']['BTC']['quotes']['USD']['change24Hr']['percent'], 2)
    
    # get the date - time: YYYY-MM-DD HH:M:S
    date_now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    
    # database - info: BTC - date, price and change24h %
    df_btc = pd.DataFrame(columns=['date','price_btc','change24h_pct'])
    
    # info: BTC - date, price and change24h %
    database = {'date': date_now,
                'price_btc': price_btc,
                'change24h_pct': change24h_pct
               }
    
    df_database = pd.DataFrame([database])
    df_btc = pd.concat([df_btc, df_database])
       
    # check if the file exist, please.
    if os.path.isfile('../dataset/price_date.csv'):
        df_btc = df_btc.reset_index(drop=True)
        df_btc.to_csv('../dataset/price_date.csv', mode='a', index=False, header=False)
    else:
        df_btc = df_btc.reset_index(drop=True)
        df_btc.to_csv('../dataset/price_date.csv', index=False)
    
    # check if the file exist, please.
    if os.path.isfile('../dataset/database_txo.csv') and os.path.isfile('../dataset/database_txo_btc.csv'):
        FileExist=True
    else:
        FileExist=False
        
    # loop in information from one transaction
    for key in txo:
        if(key == 'blockchain'):
            from_wallet = txo['from'] # dictionary
            to_wallet = txo['to'] # dictionary

            # from wallet/ owner    
            from_owner_type = from_wallet['owner_type']
            from_owner = from_wallet['owner']

            # to wallet/ owner
            to_owner_type = to_wallet['owner_type']
            to_owner = to_wallet['owner']

            # symbol and amount currency
            symbol_currency = txo['symbol']
            amount_currency = txo['amount']
            
            # hash of the transaction
            hash_txo = txo['hash']

            # amount USD
            amount_currency_usd = txo['amount_usd']

            database_txo.loc[index,'blockchain'] = symbol_currency
            database_txo.loc[index,'amount_coin'] = amount_currency
            database_txo.loc[index,'amount_usd'] = amount_currency_usd
            database_txo.loc[index,'hash'] = hash_txo
            
            # this is to get diferent transactions
            if(id == txo['id']):
                continue
            
            # tracking the transaction by the ID
            id = txo['id']
            
            # BTC only
            if(symbol_currency == 'BTC'):
                database_txo_btc.loc[idx,'blockchain'] = symbol_currency
                database_txo_btc.loc[idx,'amount_coin'] = amount_currency
                database_txo_btc.loc[idx,'amount_usd'] = amount_currency_usd
                database_txo_btc.loc[idx,'hash'] = hash_txo
                
            # USD price cryptocurrency
            price = round(amount_currency_usd/amount_currency, 2)
            
            # list with the origin and destiny of the transaction
            from_tos = ['unknown','exchange']
            
            for ifrom_to in from_tos:
                for jfrom_to in from_tos:
                    if(from_owner_type == ifrom_to and to_owner_type == jfrom_to):
                        WFund = tool.whaleInfo(price, amount_currency, symbol_currency, id, date_txo, WhaleFund)
                        
                        if(WFund):
                            print(fore.WHITE + back.RED + style.BOLD + f'#{index} {txo[key]}: {amount_currency} {symbol_currency} ({amount_currency_usd} USD){bcolors.ENDC}: from {bcolors.HEADER}{from_owner_type}({from_owner}) to {bcolors.HEADER}{to_owner_type}({to_owner}){bcolors.ENDC} id: {id}, {date_txo}' + style.RESET)
                            WhaleFund = False
                        else:
                            print(f'#{index} {bcolors.HEADER}{txo[key]}{bcolors.ENDC}: {bcolors.OKGREEN}{amount_currency} {symbol_currency}{bcolors.ENDC} ({amount_currency_usd} USD): from {bcolors.HEADER}{from_owner_type}({from_owner}){bcolors.ENDC} to {bcolors.HEADER}{to_owner_type}({to_owner}){bcolors.ENDC} id: {id}, {date_txo}')
                        
                        if(symbol_currency == 'BTC'):
                            database_txo_btc.loc[idx,'from_to'] = f'{ifrom_to}' + '-' + f'{jfrom_to}'
                            database_txo_btc.loc[idx,'id'] = id
                            database_txo_btc.loc[idx,'date'] = date_txo
                            database_txo_btc.loc[idx,'price'] = price_btc
                            database_txo_btc.loc[idx,'change24h_pct'] = change24h_pct

                        database_txo.loc[index,'from_to'] = f'{ifrom_to}' + '-' + f'{jfrom_to}'
                        database_txo.loc[index,'id'] = id
                        database_txo.loc[index,'date'] = date_txo

                        index += 1
                        idx += 1
                        
            if(FileExist == False):
                database_txo = database_txo.reset_index(drop=True)
                database_txo.to_csv('../dataset/database_txo.csv',index=False)
                
                # BTC only
                database_txo_btc = database_txo_btc.reset_index(drop=True)
                database_txo_btc.to_csv('../dataset/database_txo_btc.csv', index=False)
                
            else:
                # saving the dataframe
                database_txo = database_txo.reset_index(drop=True)
                database_txo.to_csv('../dataset/database_txo.csv', mode='a', index=False, header=False)
                
                # saving the dataframe BTC only
                database_txo_btc = database_txo_btc.reset_index(drop=True)
                database_txo_btc.to_csv('../dataset/database_txo_btc.csv', mode='a', index=False, header=False)
    
    tool.release_memory(database_txo)
    tool.release_memory(database_txo_btc)
    time.sleep(6)