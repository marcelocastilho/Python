'''
Created on Jul 31, 2018

@author: marcelo
'''

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and 
#put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
#match the output below.

def writeMinAndMaxValues():
    print('Maximum is ', max)
    print('Minimun is ', min)

min = None
max = None    

while True:
    inputValue = input('Enter a Number!')
    
    if(inputValue == 'done'):
        writeMinAndMaxValues()
        break
    try:
        inputAsNumber = int(inputValue)
        if(min is None and max is None):
            min = inputAsNumber
            max = inputAsNumber
        elif(min > inputAsNumber):
            min = inputAsNumber            
        elif(max < inputAsNumber):
            max = inputAsNumber            
    except:
        print('Invalid input')
        continue
    #print(inputAsNumber)