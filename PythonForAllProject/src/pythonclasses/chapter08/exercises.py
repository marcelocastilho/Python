'''
Created on Aug 2, 2018

@author: marcelo
'''
#8.4 Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
#

#fname = input("Enter file name: ")
resultList = list()
fh = open('romeo.txt')
for line in fh:
    listOfActualLinep = line.split()
    
    for word in listOfActualLinep:
        if(word in resultList): continue
        else:
            resultList.append(word)
resultList.sort()
print(resultList)
    
#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line 
#(i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open('mbox-short.txt')

count = 0
for index in fh:
    if(index.startswith('From ')):
        list = index.split()
        count = count +1
        print(list[1])

print("There were", count, "lines in the file with From as the first word")