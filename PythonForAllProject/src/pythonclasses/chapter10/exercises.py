'''
Created on Aug 6, 2018

@author: marcelo
'''
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#out: 04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1


fileIn = open('mbox-short.txt')
wordsMap = dict()

listHours = list()
for line in fileIn:
    if(line.startswith('From ')):
        words = line.split() 
        wordDate = words[5]
        wordHour = wordDate[0:2]
        listHours.append(wordHour)

#Creating a dictionary with hours  vs occurency
dictHours = dict()
for hour in listHours:
    dictHours[hour] = dictHours.get(hour,0) + 1
    
#Sorting by Key
for k,v in sorted([(k,v) for k,v in dictHours.items()]):
    print(k, v)

#Sorting by value :-)
#print(sorted([(v,k) for k,v in dictHours.items()]))
        