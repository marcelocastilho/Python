
array1 = 1,2,3,4,5,6,7,8,9,20

#Doing loops with while
n = 5
while n > 0 :
    print('N =: ', n)
    n = n - 1
print('\n')

#Doing loops with for and array
for i in range(0, len(array1)):
    print('I =: ', array1[i])
print('\n')

#Doing loops with for and array
for i in array1:
    print('I =: ', i)
    if(i == 5):
        break
    
for i in [0,4,5,7,5,8,9]:
    print('I =: ', i)
    
str = 'Marcelo Batista Castilho'
print('\n', str.split()[1])