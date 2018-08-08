'''
Created on Aug 7, 2018

@author: marcelo
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl 

# ignore SSL certificate erros
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter -')
html = urllib.request.urlopen('http://www.google.com.br', context=ctx).read()
#print('Html:', html)

soup = BeautifulSoup(html, 'html.parser')
#print('Soup:', soup, '\n\n')

tags = soup('a')
print('Tags type', type(tags))
print(tags, '\n\n')
for tag in tags: 
    print(tag.get('href', None))