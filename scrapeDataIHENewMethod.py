import requests, re
from bs4 import BeautifulSoup
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://ihe.istanbul/satis-noktalari',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

results = {}

with requests.Session() as s:
    s.headers = headers
    r = s.get('http://ihe.istanbul/satis-noktalari')
    soup = BeautifulSoup(r.content, 'lxml')
    options = {i.text: i['value'] for i in soup.select('[name=ilceID] option:nth-child(n+2)')}
    for k, v in options.items():
        data = {'ilceID': v, 'SatisBufe': '1'}

        r = s.post('http://ihe.istanbul/satis-noktalari', data=data)

        lat, lon = re.search(r'google.maps.LatLng\(([\d.]+),\s?([\d.]+)\)', r.text).groups()
        print(k, f'lat = {lat}', f'lon = {lon}')

        results[k] = [lat, lon]