"""
source code: https://mempool.space/docs/api/websocket

Endpoint
wss://mempool.space/api/v1/ws
Description
Default push: { action: 'want', data: ['blocks', ...] } to express what you want pushed. 
Available: blocks, mempool-blocks, live-2h-chart, and stats.

Push transactions related to address: { 'track-address': '3PbJ...bF9B' } to receive all 
new transactions containing that address as input or output. Returns an array of transactions. 
address-transactions for new mempool transactions, and block-transactions for new block 
confirmed transactions.

"""

import websocket
import _thread
import time
import rel
import json
import blockcypher
import pandas as pd
import feather
import time
import gc
import sys
import feather
import os
import csv

# Pandas has a high consume of memory RAM usage
# release memory RAM
def release_memory(df):   
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')

rel.safe_read()


def on_message(ws, message):

    data = json.loads(message)

    for i in data:
        subset = data[i]
        
        #if isinstance(subset, int):
            #print(f'{i}: {subset}')

        df = pd.DataFrame()

        if isinstance(subset, list):
            newsubset = {key: [i[key] for i in subset] for key in subset[0]}
            for j in newsubset:
                if j == 'txid':
                    print(f'{j}: {newsubset[j]}')

                    for txid in newsubset[j]:

                        with open('txids.txt', 'a') as file:
                            file.write(txid)
                            file.write('\n')
                        
                            # Close the file
                            #file.close()
                    

        #if isinstance(subset, dict):
            #print(f'{subset}')
            #for isubset in subset:
            #    print(f'{isubset}: {subset[isubset]}')



def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    message = { "action": "init" }
    ws.send(json.dumps(message))
    message = { "action": "want", "data": ['blocks', 'stats', 'mempool-blocks', 'live-2h-chart', 'watch-mempool'] }
    ws.send(json.dumps(message))

if __name__ == "__main__":
    print("Requesting data from mempool...")
    ws = websocket.WebSocketApp("wss://mempool.space/api/v1/ws",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()