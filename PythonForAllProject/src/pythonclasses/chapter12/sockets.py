import urllib.request, urllib.parse, urllib.error 

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

wordDict = dict()
for line in fhand:
    words = line.decode().strip().split()
    for word in words:
        wordDict[word] = wordDict.get(word,0) + 1
        
print('Count words', sorted([(k,v) for v,k in wordDict.items() ]))