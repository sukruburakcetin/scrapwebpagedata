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

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.page_load_strategy = 'normal'

tag = "//*[@id="
tail = "]"
idPrefix = "\"SelectedCompany"
# specify the url
urlpage = 'https://enyakinptt.ptt.gov.tr/Enyakinptt/'
print(urlpage)
driver = webdriver.Chrome()  # allocate web driver
driver.get(urlpage)  # load url to web driver
types = driver.find_elements_by_class_name('dxeRadioButtonList_MetropolisBlue')
typeCount = len(types[1].text.split("\n"))

for z in range(typeCount):
    y = 0
    i = 0
    driver.find_element_by_id('MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTIl_0_B-1').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTIl_0_DDD_L_LBT")))
    driver.find_element_by_id(
        'MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTIl_0_DDD_L_LBI40T0').click()
    driver.find_element_by_id(
        'MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTTur_0_RB' + str(z)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#SelectedCompany0")))
    soup = BeautifulSoup(driver.page_source, features="lxml")
    html_content = soup.contents[0]
    parent = driver.find_element_by_xpath('//*[@id="PTTIsYeriSonuc"]')
    for i in range(len(html_content.find_all("div", {'class': 'act'}))):
        element = tag + idPrefix + str(y) + "\"" + tail
        name = (parent.find_element_by_xpath(element)).text
        onClickValue = parent.find_element_by_xpath(element).get_attribute("onclick")
        onClickValueSplitted = onClickValue.split(",")
        latModified = onClickValueSplitted[0].split("(")
        lat = latModified[1]
        long = onClickValueSplitted[1]
        # if i == 0:
            # print(lat)
            # print(long)
            # print(name)
            # print("----------iterating next point------------")
        y += 1
        data = [name, (types[1].text.split("\n"))[z], lat, long]
        # opening the csv file in 'w+' mode
        file = open('g4g.csv', 'a+', newline='', encoding='utf-8')

        with file:
            # identifying header
            headers = ['NAME', 'TYPE', 'LATITUDE', 'LONGITUDE']
            writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
            # writing data row-wise into the csv file
            if file.tell() == 0:
                writer.writeheader()  # file doesn't exist yet, write a header
            # writing the data into the file
            with file:
                write = csv.writer(file)
                writer.writerow({'NAME': data[0], 'TYPE': data[1], 'LATITUDE': data[2], 'LONGITUDE': data[3]})


