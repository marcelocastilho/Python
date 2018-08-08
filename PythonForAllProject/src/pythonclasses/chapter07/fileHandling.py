import os

path = 'C:\\Python\\pi4e\\Python\\PythonForAllProject\\resources' 

file1 = open(path + '\\chapter7Assigment.txt', 'w+')

for i in range(10):
    file1.write('Nova linha ' + str(i) + '\n' );

file1.close()

file1 = open(path + '\\chapter7Assigment.txt', 'r')

count = None
#Read all file
completeFile = file1.read()    

for caracter in completeFile:
    if('a' in caracter):        
        if count is None:
            count = 1
        else:
            count = count + 1
            
print('Count of substr \'Nova\' =', count)
print('Lenght of the text=', len(completeFile))

print('Showing the files on path', path)

dir = os.listdir(path)

for file in dir:
    print(file)
    if(file == 'chapter7Assigment.txt'):
        #os.remove(path + '\\chapter7Assigment.txt')
        None