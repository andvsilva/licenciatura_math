"""
-> blockcypher-python
https://github.com/blockcypher/blockcypher-python/tree/master



"""

import blockcypher
import pandas as pd
import time


df_txids = pd.read_csv('feather/txids.csv')

#print(df_txids)

for index, row in df_txids.iterrows():
    print(row)

#print(blockcypher.get_block_details(f'800000'))

#for iblock in range(800000, 810386):
#    block_details = blockcypher.get_block_details(f'{iblock}')
#
#    print(block_details)
#    print("Please, wait a few seconds...")
#    time.sleep(8)
    