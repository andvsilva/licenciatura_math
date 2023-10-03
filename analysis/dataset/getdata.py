import blockcypher
from bs4 import BeautifulSoup as soup
import requests

HEADERS ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

lblock_height = blockcypher.get_latest_block_height()
lblock_hash = blockcypher.get_latest_block_hash()

print(lblock_height)

print(lblock_hash)

url = 'https://mempool.space/tx/61addefd4c4561429d35e5faf41a16b3e1a1d603a955c9db9cbac9dfef44960c'

req = requests.get(url, headers=HEADERS)
page_soup = soup(req.text, "html5lib")
print(page_soup)
