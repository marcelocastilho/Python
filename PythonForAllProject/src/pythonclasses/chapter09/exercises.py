'''
Created on Aug 6, 2018

@author: marcelo
'''

#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#out: cwen@iupui.edu 5

#name = input("Enter file:")

fileIn = open('mbox-short.txt')
wordsMap = dict()

for line in fileIn:
    if(line.startswith('From ')):
        words = line.split() 
        word = words[1]
        wordsMap[word] = wordsMap.get(word,0) + 1
        #print(word)

maxSender = max(wordsMap.values())    
for mail, count in wordsMap.items():
    if(count == maxSender):            
        print(mail, count)