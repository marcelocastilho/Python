
friends = ['Jose','Joao','Maria', 'Bastiao']
print('List of strings:', friends )
print('Lenght of the list:', range(len(friends)))
print('Range returns the type ', type(range(len(friends))))
#Ordering list
friends.sort()
print('Ordering the list', friends)
friends.sort(reverse=True)
print('Ordering the list', friends)

arrayDifferentTypes = ['string', 26, True, 33.9]
print('\nList of different types:', arrayDifferentTypes )

for index in arrayDifferentTypes:
    print('Type:', type(index), ' Value:', index);

arrayWithAnotherList = [1,2,['Str1',89.9], False]
print('\narrayWithAnotherList:', arrayWithAnotherList)

for index in arrayWithAnotherList:
    print('Type:', type(index), ' Value:', index);

#Concating lists
list1 = [0,1,2,3,4,5,6,7,8,9]
print('\nList1', list1)
list2 = [10,11,12,13,14,15,16,17,18,19]
print('List2', list1)
list3 = list1 + list2
print('Cacatened list', list3)
print('Printing part of a list', list3[3:4])

#Adding itens to the list
anotherList = list()
anotherList.append('AAAAAAAAAAAAAAAA')
anotherList.append('BBBBBBBBBBBBBBBB')
anotherList.append(19.0)
print('List created with append method',anotherList)
print('Removing the index 1:',anotherList.remove(anotherList[1]))
print('List after removed index 1',anotherList)
print('List contains AAAAAAAAAAAAAAAA ?', 'AAAAAAAAAAAAAAAA' in anotherList)
print('List not contains 19 ?', 19 not in anotherList)

#Spliting string using a specific caracter
str1 = 'Marcelo;Batista;Castilho'
print('String to be splited:', str1)
print('Spliting string using \';\' :',str1.split(';'))
 
