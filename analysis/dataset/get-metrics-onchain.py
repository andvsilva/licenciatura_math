
"""
https://github.com/JuaanM0/blockchain-metrics/tree/blockchain


seg 02 out 2023 19:22:18 -03 Author: @andvsilva
"""

from blockchain_metrics import blockchain_data
import pandas as pd

block = blockchain_data.blockchain_stats_currency()

#total bitcoins in circulation
total_bitcoins = block.total_bitcoins()
market_price = block.market_price()
market_cap = block.market_cap()
n_transactions_total = block.n_transactions_total()
median_confirmation_time = block.median_confirmation_time()
hash_rate = block.hash_rate()
difficulty = block.difficulty()
transaction_fees = block.transaction_fees()
cost_per_transaction = block.cost_per_transaction()
n_unique_addresses = block.n_unique_addresses()
output_volume = block.output_volume()
mempool_count = block.mempool_count()
mempool_growth = block.mempool_growth()
mempool_size = block.mempool_size()
utxo_count = block.utxo_count()
estimated_transaction_volume = block.estimated_transaction_volume()
my_wallet_n_users = block.my_wallet_n_users()

metrics_btc = pd.concat([total_bitcoins, 
                       market_price, 
                       market_cap,
                       n_transactions_total,
                       median_confirmation_time,
                       hash_rate,
                       difficulty,
                       transaction_fees,
                       cost_per_transaction,
                       n_unique_addresses,
                       mempool_count,
                       mempool_growth,
                       mempool_size,
                       utxo_count,
                       estimated_transaction_volume,
                       my_wallet_n_users
                       ], axis=1)

print(metrics_btc)