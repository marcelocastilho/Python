#Creating a dictionary in a single line

dict0 =  {'Name': 'Gislaine', 'Age': 34, 'Weight':80, 'Height': 1.50}
print('Print the dictionary instancied  in a single line', dict0)

dict1 = dict()

dict1['Name'] = 'Marcelo'
dict1['Age'] = 34
dict1['Height'] = 1,69

print('Printing a dictionary', dict1)
print('Keys:', dict1.keys())
print('Values:', dict1.values())

#Using get method
print('Getting a key that dont exists', dict1.get('weight', 0))
print('Getting a key that exists', dict1.get('Age', 0))

#Dictionary with int values
intDict = dict()

intDict[1] = 'Posição 1'
intDict[2] = 'Posição 2'
intDict['Posição'] = 3

print('\nDictionary with int keys', intDict)

#Using a dictionary to count equal values in a array 
list1 = ['a','b','c','a','c','d','f','g','h','a','b','c','c']
dictCount = dict()
for letter in list1:
    dictCount[letter] = dictCount.get(letter,0) + 1    
print('Counting the equals values in a array: ', dictCount)

bigCount=None
bigWord=None

for letter, count in dictCount.items():
    print('letter', letter, 'count', count)

#Using th items method
print('Print the items', dict1.items())
print('What type items returns', type(dict1.items()))




