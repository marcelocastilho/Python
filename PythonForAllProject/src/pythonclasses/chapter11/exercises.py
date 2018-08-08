import re

'''
Created on Aug 6, 2018

@author: marcelo
'''

file = open('regex_sum_119186.txt')

text = file.read()

print( sum( [int(k) for k in re.findall('[0-9]+', text)]))
  
   
