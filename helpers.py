import re

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from requests_html import HTMLSession
import pandas as pd
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def convert(string):
    li = list(string.split(" "))
    return li


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.page_load_strategy = 'normal'

urlpage = 'https://sukruburakcetin.github.io/test-poi-check/original.html'
driver = webdriver.Chrome()
driver.get(urlpage)  # load url to web driver
soup = BeautifulSoup(driver.page_source, features="lxml")
html_content = soup.contents[0]
targetScriptContent = html_content.find_all("script")[5]
convertedList = convert(targetScriptContent.text)
sonuc = [k for k in convertedList if '<li><bold>' in k]
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html
lon = re.search(r'<li><bold>LATITUDE:([\d.]+)', targetScriptContent.text).groups()
sube1, sube2 = re.search(r'<li><bold>NAME:([\w]+)\s([\w]+)', targetScriptContent.text).groups()
sube3 = re.search(r''+sonuc[0].split(':')[1]+'\s([\w]+)', targetScriptContent.text).groups()
print("pause")
#<li><bold>NAME:HASTANE ŞUBESİ', '<li><bold>TYPE:PTT İşyeri', '<li><bold>LATITUDE:29.1072', '<li><bold>LONGITUDE:40.96997