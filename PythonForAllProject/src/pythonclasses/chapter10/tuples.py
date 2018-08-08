from Tools.scripts.fixcid import Reverse


#Transforming dictionary in a tuple inverting the key and values
dict1 = {'a':0, 'b':1, 'c':3, 'd':7, 'e':2, 'f':1 }

listTuples = list()
for key, val in dict1.items():
    newTuple = (val, key)
    listTuples.append(newTuple)
    
print('List without order', listTuples)
print('Ordered list ascending ', sorted(listTuples))
print('Ordered list decreasing', sorted(listTuples, reverse=True))

#Using a List comprehension

print('Sorting using List comprehension', sorted([(k,v) for k,v in dict1.items()]))
print('Sorting using List comprehension and inverting the key, value', sorted([(v,k) for k,v in dict1.items()]))