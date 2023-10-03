
"""
https://github.com/JuaanM0/blockchain-metrics/tree/blockchain


seg 02 out 2023 19:22:18 -03 Author: @andvsilva
"""

from blockchain_metrics import blockchain_data

block = blockchain_data.blockchain_stats_currency()

#cost per transaction
block.cost_per_transaction()
block.plot_data()