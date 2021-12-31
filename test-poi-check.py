import re
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
from requests_html import HTMLSession
import pandas as pd
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def convert(string):
    li = list(string.split("'"))
    return li


def listToString(s):
    # initialize an empty string
    str1 = ""
    str2 = " "

    # traverse in the string
    for ele in s:
        str1 += ele
        str1 += str2
        # return string
    return str1


urlpage = 'https://sukruburakcetin.github.io/test-poi-check/appended.html'
print(urlpage)
driver = webdriver.Chrome()  # allocate web driver
driver.get(urlpage)  # load url to web driver
soup = BeautifulSoup(driver.page_source, features="lxml")
html_content = soup.contents[0]
body_html_content = html_content.find("body")
result = body_html_content.find("script")

lst = convert(result.text)

sonuc = [k for k in lst if '<li><bold>' in k]
sonuc_name = [k for k in sonuc if '<li><bold>NAME:' in k]
sonuc_type = [k for k in sonuc if '<li><bold>TYPE:' in k]
sonuc_latitude = [k for k in sonuc if '<li><bold>LATITUDE:' in k]
sonuc_longitude = [k for k in sonuc if '<li><bold>LONGITUDE:' in k]

name_IDs = []
type_IDs = []
latitude_IDs = []
longitude_IDs = []
# stringSonuc = listToString(sonuc)
# stringSonuc_name = listToString(sonuc_name)
# stringSonuc_type = listToString(sonuc_type)
# stringSonuc_latitude = listToString(sonuc_latitude)
# stringSonuc_longitude = listToString(sonuc_longitude)

# param1, param2 = re.search(r'\(\'<li><bold>(\w+):(\w+)', stringSonuc).groups()
# name1, name2, type1, type2, lat1, lat2, long1, long2 = re.search(r'\(\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):([\d.]+)\',\s\'<li><bold>(\w+):([\d.]+)\'\)', stringSonuc).groups()

# ('<li><bold>NAME:100.YIL MAHALLESİ ŞUBESİ'  '<li><bold>TYPE:PTT İşyeri'  '<li><bold>LATITUDE:28.85444'  '<li><bold>LONGITUDE:41.05938')

# re.search(r'<li><bold>(\w+):(\w.+)', stringSonuc_name).groups()

get_pattern = re.compile(r'<li><bold>(\w+):(\w.+)')

for x in range(len(sonuc_name)):
    nameName, nameID = re.search(get_pattern, sonuc_name[x]).groups()
    name_IDs.append(nameID)
    typeName, typeID = re.search(get_pattern, sonuc_type[x]).groups()
    type_IDs.append(typeID)
    latName, latID = re.search(get_pattern, sonuc_latitude[x]).groups()
    latitude_IDs.append(latID)
    longName, longID = re.search(get_pattern, sonuc_longitude[x]).groups()
    longitude_IDs.append(longID)

print(len(sonuc_name))
print(len(sonuc_type))
print(len(sonuc_latitude))
print(len(sonuc_longitude))

for y in range(len(sonuc_name)):
    print("Şube ismi: " + name_IDs[y] + ", " + "Tür: " + type_IDs[y] + ", " + "Lat: " + latitude_IDs[
        y] + ", " + "Long: " + longitude_IDs[y])


d = {'Name': name_IDs, 'Type': type_IDs, 'Latitude': latitude_IDs, 'Longitude': longitude_IDs}
df = pd.DataFrame(data=d)

# d = {}
# df = pd.DataFrame(data=d)
#
#
# for x in range(len(sonuc_name)):
#     df.at[x, 'Name'] = name_IDs[x]
#     df.at[x, 'Type'] = type_IDs[x]
#     df.at[x, 'Latitude'] = latitude_IDs[x]
#     df.at[x, 'Longitude'] = longitude_IDs[x]

# df = pd.DataFrame(data=d)
print(df)


# # ('<li><bold>NAME:HASTANE ŞUBESİ'  '<li><bold>TYPE:PTT İşyeri'  '<li><bold>LATITUDE:29.1072'  '<li><bold>LONGITUDE:40.96997')
# patternTest = re.compile(
#     r'\'<li><bold>(\w+):(\w+)\s(\w+)\'\s\s\'<li><bold>(\w+):(\w+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\)'
# )
# patternTest2 = re.compile(
#     r'\'<li><bold>(\w+):(\w+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\)'
# )
#
# # re.search(r'\'<li><bold>(\w+):(\w+)\s(\w+)\'\s\s\'<li><bold>(\w+):(\w+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\s\s\'<li><bold>(\w+):([\d.]+)\'\)', stringSonuc).groups()
# pattern = re.compile(
#     r'\(\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):([\d.]+)\',\s\'<li><bold>(\w+):([\d.]+)\'\)')
#
# pattern2 = re.compile(
#     r'\(\'<li><bold>(\w+):(\w+)\',\s\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):([\d.]+)\',\s\'<li><bold>(\w+):([\d.]+)\'\)')
#
# pattern3 = re.compile(
#     r'\(\'<li><bold>(\w+):(\w+)\s\'<li><bold>(\w+):(\w+)\',\s\'<li><bold>(\w+):([\d.]+)\',\s\'<li><bold>(\w+):([\d.]+)\'\)')
#
#
# # <li><bold>NAME:HASTANE ŞUBESİ <li><bold>NAME:100.YIL MAHALLESİ ŞUBESİ
#
# # ('<li><bold>NAME:ZÜMRÜTEVLER '<li><bold>TYPE:KargoMat', '<li><bold>LATITUDE:29.15362', '<li><bold>LONGITUDE:40.94144')
# for (nameName, nameID, typeName, typeID, latName, latID, longName, longID) in re.findall(patternTest2, stringSonuc):
#     print(
#         nameName + ":" + nameID + ", "
#         + typeName + ":" + typeID + ", "
#         + latName + ":" + latID + ", " +
#         longName + ":" + longID)
#
# for (nameName2, nameID2, typeName2, typeID2, latName2, latID2, longName2, longID2) in re.findall(pattern2, stringSonuc):
#     print(
#         nameName2 + ":" + nameID2 + ", "
#         + typeName2 + ":" + typeID2 + ", "
#         + latName2 + ":" + latID2 + ", " +
#         longName2 + ":" + longID2)
#
# for (nameName3, nameID3, typeName3, typeID3, latName3, latID3, longName3, longID3) in re.findall(pattern3, stringSonuc):
#     print(
#         nameName3 + ":" + nameID3 + ", "
#         + typeName3 + ":" + typeID3 + ", "
#         + latName3 + ":" + latID3 + ", " +
#         longName3 + ":" + longID3)

# ('<li><bold>NAME:HASTANE '<li><bold>TYPE:PTT '<li><bold>LATITUDE:29.1072', '<li><bold>LONGITUDE:40.96997')
# print(stringSonuc)
# print(param1)
# print(param2)

# ('<li><bold>NAME:ÜMRANİYE', '<li><bold>TYPE:PTT '<li><bold>LATITUDE:29.10504', '<li><bold>LONGITUDE:41.01613')
# ('<li><bold>NAME:ÜMRANİYE '<li><bold>TYPE:PTT '<li><bold>LATITUDE:29.0987', '<li><bold>LONGITUDE:41.02467')

# '(\'<li><bold>NAME:ALT'
# '\'<li><bold>TYPE:PTT'
# '\'<li><bold>LATITUDE:28.67899\','
# '\'<li><bold>LONGITUDE:41.0163\')'

# re.search(r'google.maps.LatLng\(([\d.]+),\s?([\d.]+)\)', result.text).groups()
print("code is executed")


