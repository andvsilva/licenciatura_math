import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from icecream import ic

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://mempool.space/")

time.sleep(2)
print('block....')
link_block = driver.find_element('xpath','//*[@id="bitcoin-block-811780"]/a')

link_block.click()

##  Numbers of transactions.
numbers_txs_block_str = driver.find_element('xpath','//*[@id="block-tx-title"]/h2').text
numbers_txs_block_str = numbers_txs_block_str.replace(",", "")
numbers_txs = int(numbers_txs_block_str.rsplit(' transaction', 1)[0])
ic(numbers_txs)

# get hash for the block
block = driver.current_url
hash = re.sub('https://mempool.space/block/', '', block)
print(hash)

# timestamp
timestamp = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/app-timestamp/span') 
timestamp = timestamp.text

timestamp = timestamp.rsplit(' (', 1)[0]
print(timestamp)

limit_txs_page = 0
limit_txs = 0
itx = 1

time.sleep(3)
print('loop on transactions...')
while limit_txs < numbers_txs:
    if limit_txs_page < 25:
        if limit_txs == numbers_txs:
            break 
            
        limit_txs_page += 1
        tx = driver.find_element('xpath',f'/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/app-transactions-list/div/div[{itx}]/a/app-truncate/span/span[1]').text
        print(f'#{itx}: {tx}')
        limit_txs += 1
        itx += 2
        time.sleep(0.5)
    else:
        time.sleep(2)
        print('next page...')
        next_page = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/ngb-pagination/ul/li[8]/a/span').click()
        time.sleep(15)
        limit_txs_page = 0
        itx = 1


#/html/body/app-root/app-master-page/div/div/main/app-start/app-transaction/div/app-transactions-list/div/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/a/app-truncate/span/span[1]
#/html/body/app-root/app-master-page/div/div/main/app-start/app-transaction/div/app-transactions-list/div/div/div[1]/div[3]/table/tbody/tr[2]/td[1]/a/app-truncate/span/span[1]

#hash = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/app-clipboard/span/button/app-svg-images/svg/path')

#hash.click()

# Get text of h1 tag
#first_h1_text = hash.text

#print(first_h1_text)

# Match the first h1 tag on the page
#first_h1 = driver.find_element(By.XPATH, "/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/a")

# Get text of h1 tag
#first_h1_text = first_h1.text

#print(first_h1_text)

time.sleep(1000)