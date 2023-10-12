
"""
https://github.com/JuaanM0/blockchain-metrics/tree/blockchain


seg 02 out 2023 19:22:18 -03 Author: @andvsilva
"""

from blockchain_metrics import blockchain_data

block = blockchain_data.blockchain_stats_currency()

#total bitcoins in circulation
dataframe_total_bitcoins = block.total_bitcoins()
print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.market_price()
print(dataframe_total_bitcoins)
block.plot_data()

dataframe_total_bitcoins = block.market_cap()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.n_transactions_total()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.n_transactions_total()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.median_confirmation_time()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.hash_rate()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.difficulty()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.transaction_fees()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.cost_per_transaction()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.n_unique_addresses()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.output_volume()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.mempool_count()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.mempool_growth()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.mempool_size()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.utxo_count()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.estimated_transaction_volume()
#print(dataframe_total_bitcoins)
#block.plot_data()

dataframe_total_bitcoins = block.my_wallet_n_users()
#print(dataframe_total_bitcoins)
#block.plot_data()