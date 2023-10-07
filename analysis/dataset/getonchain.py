"""

-> blockcypher-python
https://github.com/blockcypher/blockcypher-python/tree/master


"""

import blockcypher
import pandas as pd
import time

file = open('txids.txt', 'r')

while True:
    txid = file.readline()
    if not txid:
        break

    txid = txid.replace("\n", "")
    print(txid)
        
    print(blockcypher.get_transaction_details(f'{txid}'))

    #print(block_details)
    time.sleep(20)