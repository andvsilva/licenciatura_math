
"""
https://github.com/JuaanM0/blockchain-metrics/tree/blockchain


seg 02 out 2023 19:22:18 -03 Author: @andvsilva
"""

from blockchain_metrics import blockchain_data

block = blockchain_data.blockchain_stats_currency()

#total bitcoins in circulation
#dataframe_total_bitcoins = block.total_bitcoins()
#block.plot_data()

#dataframe_total_bitcoins = block.market_cap()
#block.plot_data()

#dataframe_total_bitcoins = block.trade_volume()
#block.plot_data()

dataframe_total_bitcoins = block.mempool_growth()
print(dataframe_total_bitcoins)
block.plot_data()