import json
import pandas as pd
import numpy as np
from IPython.display import HTML
import matplotlib.pyplot as plt
import seaborn as sns
import os.path
from matplotlib.backends.backend_pdf import PdfPages
import sys
import gc
import time
from datetime import datetime
from pprint import pprint  # For formatted dictionary printing
import os.path
import sys
import gc
from sys import getsizeof
from colored import fore, back, style
import toolkit as tool
import snoop
import requests
import notify2


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
    
def notify(price, symbol_currency, date_time):
    
    ICON_PATH = "../images/btc.jpg" # This is not working, FIXME, I do not know why.

    # initialise the d-bus connection
    notify2.init("Cryptocurrency reach the price")

    # create Notification object
    n = notify2.Notification("Crypto Notifier", icon = ICON_PATH)

    # Set the urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)

    # Set the timeout
    n.set_timeout(1000)

    result = str(price)

    # Update the content
    n.update(f"1 {symbol_currency} in USD - {date_time}", result)

    # Show the notification
    n.show()

# Reduce DataFrame size
# This part of the code is not my, I get from this webpage: 
# https://www.mikulskibartosz.name/how-to-reduce-memory-usage-in-pandas/
def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype
    if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.uint8).min and c_max < np.iinfo(np.uint8).max:
                    df[col] = df[col].astype(np.uint8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.uint16).min and c_max < np.iinfo(np.uint16).max:
                    df[col] = df[col].astype(np.uint16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.uint32).min and c_max < np.iinfo(np.uint32).max:
                    df[col] = df[col].astype(np.uint32)                    
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
                elif c_min > np.iinfo(np.uint64).min and c_max < np.iinfo(np.uint64).max:
                    df[col] = df[col].astype(np.uint64)
            elif str(col_type)[:5] == 'float':
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    return df

# release memory RAM
def release_memory(df):   
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    #print('memory RAM released.')

# release memory for large arrays (dictionary)
def release_array(dd):
    del dd 
    gc.collect()
    dd = None

list_limits = [500]
list_symbols = ['BTC', 'ETH']
            
#@snoop
def whaleInfo(price, amount_currency, symbol_currency, id, date_time, WhaleFund):
    for ilist_symbol in list_symbols:
        if symbol_currency == f'{ilist_symbol}':
            for ilist_limit in list_limits:
                if( amount_currency >= ilist_limit):
                    notify(price, symbol_currency, date_time)
                    print('******************************************************************************************************')
                    print('>>>>>>>>>> WARNING: WHALE MOVING FUNDS <<<<<<<<<<<<<')
                    print(fore.WHITE + back.RED + style.BOLD + f'>>>  {amount_currency} {ilist_symbol} MOVED - ID: {id}' + style.RESET)
                    print('******************************************************************************************************')
                    WhaleFund=True
                    
    return WhaleFund