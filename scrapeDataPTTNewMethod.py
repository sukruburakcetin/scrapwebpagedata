import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def convert(string):
    li = list(string.split("'"))
    return li


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
