from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
#oi
product = os.environ.get('PRODUTO')
chrome_options = Options()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN2')
caminho_chromedriver = os.environ.get('CHROMEDRIVER_PATH')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=caminho_chromedriver,options=chrome_options)

driver.get('https://www.mercadolivre.com.br/')
sleep(3)
search = driver.find_element_by_xpath('//*[@name="as_word"]')
search.send_keys(product)
search.send_keys(Keys.ENTER)
sleep(3)
title = driver.find_elements_by_xpath('//span[@class="main-title"]')
price = driver.find_elements_by_xpath('//span[@class="price__fraction"]')
title_text0 = title[0].text
title_text1 = title[1].text
title_text2 = title[2].text
price_text0 = price[0].text
price_text1 = price[1].text
price_text2 = price[2].text
print ('{0} R$: {1}'.format(title_text0,price_text0))
print ('{0} R$: {1}'.format(title_text1,price_text1))
print ('{0} R$: {1}'.format(title_text2,price_text2))