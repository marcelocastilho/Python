'''
Created on Aug 8, 2018

@author: marcelo
'''
import urllib.request, urllib.parse, urllib.error
import json
from textwrap import indent


serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'Rua Mariano Skakuy 209, parana, brasil'

url = serviceUrl + urllib.parse.urlencode({'address': address})

print('Retrieving url:', url)

uh = urllib.request.urlopen(url)

data = uh.read().decode()

print('Retrieved', len(data), 'characters','\n')

try:
    js = json.loads(data)
except:
    js = None
    
if not js or 'status' not in js or js['status'] != 'OK':
    print('Failure to communicate')

for addressDetails in js['results'][0]['address_components']:
    print(addressDetails['types'][0],addressDetails['short_name'],'\n')

print(json.dumps(js,indent=4))

lat = js['results'][0]['geometry']['location']['lat']
lon = js['results'][0]['geometry']['location']['lng']
print('Lat + lon', lat, lon )
