# import libraries
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from requests_html import HTMLSession
import pandas as pd
# specify the url
urlpage = 'http://ihe.istanbul/'
print(urlpage)
# run firefox webdriver from executable path of your choice
# driver = webdriver.Firefox(executable_path='C:/Users/BURAK/Desktop/geckodriver-v0.30.0-win64/geckodriver.exe')
driver = webdriver.Chrome(executable_path='C:/Users/BURAK/Desktop/chromedriver_win32/chromedriver.exe')

# get web page
driver.get(urlpage)
# execute script to scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
driver.find_element_by_link_text("Satış Noktalarımız").click()
time.sleep(1)
driver.find_element_by_name("ilceID").click()
time.sleep(1)
driver.find_element_by_xpath("//option[@value='5']").click()
time.sleep(1)
# result = driver.find_element_by_xpath("/html/body/script[3]/text()[contains(., 'var point')]")

soup = BeautifulSoup(driver.page_source, features="lxml")
html_content = soup.contents[0]

_script = html_content.find_all("script")[23]  # 23 for chrome, 24 for firefox

# found_json = [i for i in _script if i.text.find("LatLng") > 0]
print(_script)


# sleep for 30s
# time.sleep(30)
# driver.quit()

# find elements by xpath
# at time of publication, Nov 2018:
# results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
# updated Nov 2019:
# results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
# print('Number of results', len(results))

# create empty array to store data
# data = []

# loop over results
# for result in results:
#     product_name = result.text
#     link = result.find_element_by_tag_name('a')
#     product_link = link.get_attribute("href")
#     # append dict to array
#     data.append({"product" : product_name, "link" : product_link})