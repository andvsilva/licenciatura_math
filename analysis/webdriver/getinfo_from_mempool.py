import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from icecream import ic
import blockcypher

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://mempool.space/")

time.sleep(3)

for iblock in range(812054, 812059):
    blockhash = blockcypher.get_block_hash(f'{iblock}')
    driver.get(f"https://mempool.space/block/{blockhash}")
    time.sleep(3)
    print(f'block: {iblock} > {blockhash}')
    ##  Numbers of transactions.
    numbers_txs_block_str = driver.find_element('xpath','//*[@id="block-tx-title"]/h2').text
    numbers_txs_block_str = numbers_txs_block_str.replace(",", "")
    numbers_txs = int(numbers_txs_block_str.rsplit(' transaction', 1)[0])
    ic(numbers_txs)

    # get hash for the block
    #block = driver.current_url
    #hash = re.sub('https://mempool.space/block/', '', block)
    #print(hash)

    time.sleep(3)
    # timestamp
    timestamp = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/app-timestamp/span') 
    timestamp = timestamp.text

    timestamp = timestamp.rsplit(' (', 1)[0]
    print(timestamp)

    limit_txs_page = 0
    limit_txs = 1
    itx = 1

    time.sleep(3)
    print('loop on transactions...')
    while limit_txs <= (numbers_txs + 1):
        if limit_txs == numbers_txs:
            break
        
        if limit_txs_page < 25:
                
            limit_txs_page += 1
            tx = driver.find_element('xpath',f'/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/app-transactions-list/div/div[{itx}]/a/app-truncate/span/span[1]').text
            txend = driver.find_element('xpath',f'/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/app-transactions-list/div/div[{itx}]/a/app-truncate/span/span[2]').text

            # whole hash id for the transaction.
            txid = tx + txend

            print(f'#{limit_txs}/{numbers_txs}: {txid}')

            time.sleep(5)
            # get info from transaction id
            info_txid = blockcypher.get_transaction_details(f'{txid}')
            
            
            # extract addresses from transaction details.
            for key in info_txid:
                 if key == 'addresses':
                     addresses = info_txid[key]
                     print(f'{key}: {addresses}')
                     for iaddress in addresses:
                         with open('wallets.txt', 'a') as file:
                            file.write(iaddress)
                            file.write('\n')


            limit_txs += 1
            itx += 2
            time.sleep(10)
        else:
            print('next page...')
            time.sleep(2)
            next_page = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/ngb-pagination/ul/li[8]/a/span').click()
            time.sleep(3)
            limit_txs_page = 0
            itx = 1
    
    time.sleep(10)

    # go to the homepage.
    driver.get("https://mempool.space/")