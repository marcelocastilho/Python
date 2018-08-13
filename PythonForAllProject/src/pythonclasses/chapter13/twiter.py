'''
Created on Aug 8, 2018

@author: marcelo
'''
import urllib.request, urllib.parse, urllib.error
import json
from pythonclasses.chapter13 import twurl

from textwrap import indent

TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'

acct = '41988030107'

url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count':'5'})

print('Retrieving url:', url)

connection = urllib.request.urlopen(url)

data = connection.read().decode()
headers = dict(connection.getheaders())
print(headers['x-rate-limit-remaining'])

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js,indent=4))
    
if not js or 'status' not in js or js['status'] != 'OK':
    print('Failure to communicate')

for u in js['users']:
    print('Screen_name', u['screen_name'])
    print((u['status'['text']])[:50])
