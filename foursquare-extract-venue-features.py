import webbrowser

import pandas as pd  # library to handle data in a vectorized manner
from selenium import webdriver
import json  # library to handle JSON files

import requests  # library to handle requests

import folium  # map rendering library

print('Libraries imported.')

data = {'Neighbourhoods': ['Antwerp', 'Berchem', 'Berendrecht', 'Borgerhout', 'Deurne', 'Ekeren', 'Hoboken', 'Merksem',
                           'Wilrijk'],
        'Latitude': ['51.22139', '51.1955771', '51.3455396', '51.2128453', '51.20849', '51.2773404', '51.1794946',
                     '51.2512626', '51.1683102'],
        'Longitude': ['4.39722', '4.4188392', '4.319401', '4.4462406', '4.4719297', '4.4181413', '4.3617847',
                      '4.4485629', '4.3942868']
        }

df = pd.DataFrame(data, columns=['Neighbourhoods', 'Latitude', 'Longitude'])
print(df)


def auto_open(path):
    html_page = f'{path}'
    map_antwerp.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)


latitude = 51.22139
longitude = 4.39722

map_antwerp = folium.Map(location=[latitude, longitude], zoom_start=12)

# add markers to map
for neighbourhood, lat, lng in zip(df['Neighbourhoods'], df['Latitude'], df['Longitude']):
    label = '{}'.format(neighbourhood)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=6,
        popup=label,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=1,
        parse_html=False).add_to(map_antwerp)

auto_open("C:\\Users\\sukruburak.cetin\\Desktop\\txt_arc\\asd.html")

# go to developer.foursquare.com and create a free account

CLIENT_ID = 'JBQWOXSXPYFXRVFB2440EM0R1AGYUYGB41SSZ2O44D35T0Z2'
CLIENT_SECRET = '4SGY0WSUIHJ4OLOCBUBFKY50JKIDXZHKOQLFHIGTDSQ4D5H4'
VERSION = 20202808
search_query = "restaurant"
radius = 500
LIMIT=30



# fsq3rA6CSwCMH0/G1gTrm2qazXriPY5M0NxM6rfldpd9EkY=
def getNearbyVenues(names, latitudes, longitudes):
    venues_list = []
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)

        # Part 1: creating the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID,
            CLIENT_SECRET,
            VERSION,
            lat,
            lng,
            radius,
            LIMIT)

        # Part 2: making the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        results = requests.get(url).json()
        venues = results['response']['venues']

        # Part 3 returning only relevant information for each nearby venue and append to the list
        venues_list.append([(
            name,
            lat,
            lng,
            v['venue']['name'],
            v['venue']['location']['lat'],
            v['venue']['location']['lng'],
            v['venue']['categories'][0]['name']) for v in results])

    return (venues_list)


antwerp_venues = getNearbyVenues(names=df['Neighbourhoods'],
                                 latitudes=df['Latitude'],
                                 longitudes=df['Longitude'])

print(antwerp_venues)
