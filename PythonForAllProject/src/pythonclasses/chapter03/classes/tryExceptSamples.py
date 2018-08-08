'''
Created on Jul 30, 2018

@author: marcelo
'''

#change this value to 1 or "Hello" to exercise the two possible ways 
x = "Hello"

try:
    intX = int(x)
    print('Actual value of X is a number ', x  )
except:
    print('Actual value of X isn´t a number, setting the default value' )
    x = -1
    print('X value ', x)
     
if( x < 0):
    print("The value is Smaller than 0")
elif(x > 0):
    print("The value is Bigger than 0")