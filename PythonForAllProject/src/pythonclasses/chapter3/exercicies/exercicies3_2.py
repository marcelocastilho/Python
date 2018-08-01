'''
Created on Jul 30, 2018

@author: marcelo
'''
#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
rateInput = input("Enter Rate:")
try:
    hours = float(hrs)
    normalRate = float(rateInput)
except:
    print("Please enter a correct number")
    quit();
    
resultValue = 0.0
extraHours = 0.0
greatRate = normalRate * 1.5

if(hours > 40 ):
    extraHours = hours - 40
    resultValue = 40 * normalRate + extraHours * greatRate
else:
    resultValue = hrs * normalRate
    
print(str(resultValue))