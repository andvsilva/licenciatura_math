import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://mempool.space/")

time.sleep(5)
button_enter = driver.find_element('xpath','//*[@id="bitcoin-block-811633"]/div[1]/a')

button_enter.click()

hash = driver.find_element('xpath','/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/app-clipboard/span/button/app-svg-images/svg/path')

hash.click()

# Get text of h1 tag
first_h1_text = hash.text

print(first_h1_text)

# Match the first h1 tag on the page
#first_h1 = driver.find_element(By.XPATH, "/html/body/app-root/app-master-page/div/div/main/app-start/app-block/div/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/a")

# Get text of h1 tag
#first_h1_text = first_h1.text

#print(first_h1_text)

time.sleep(1000)