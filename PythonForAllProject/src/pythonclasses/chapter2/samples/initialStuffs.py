'''
Created on Jul 30, 2018

@author: marcelo
'''

from builtins import str

#
#Comentarios são assim!! 
#

#Variables types/assigns  
msg = 'Hello World'
isOdd = False
intOrange = 15
floatOrange = 3.5

print('The type of varible msg is ', type(msg))
print('The type of varible isOdd is ', type(isOdd))
print('The type of varible intOrange is ', type(intOrange))
print('The type of varible floatOrange is ', type(floatOrange))

#Types Conversions
print('Float value of intOrange ' , float(intOrange))

print('Int value of floatOrange ' , int(floatOrange))

print('Float value of the string 123 ', float(123))

#Expressions
floatResultOfAMultiplicationExpression = float(floatOrange * intOrange * (floatOrange - 1))
print('floatResultOfAMultiplicationExpression = ', floatResultOfAMultiplicationExpression) 

floatResultOfADivisionExpression = intOrange / 2
print('floatResultOfADivisionExpression = ', floatResultOfADivisionExpression)

floatResultOfAPowerExpression =  floatResultOfAMultiplicationExpression ** floatResultOfADivisionExpression
print('floatResultOfAPowerExpression = ', floatResultOfAPowerExpression)

print("Printing a convertion into a expression", int(35)*float(2.75) )


#Conditional samples
print('Verifying if the number ' + str(intOrange) + " is ODD")
if(intOrange % 2 > 0):
    print('intOrange IS ODD!')
else:
    print('intOrange IS Pair!') 

#Simple Loop tests
loopCount = 10  
for i in range(0, loopCount):
    print(i, ' ' + msg)
    #if ()
    
    

    
