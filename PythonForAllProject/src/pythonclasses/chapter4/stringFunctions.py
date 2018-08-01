fh = open("C:\\Python\\pi4e\\Python\\PythonForAllProject\\resources\\mbox-short.txt", "r")

count = 0
for line in fh:
    actualLineValue = line.strip() 
    #Lower case
    print('Lower: ', actualLineValue.lower())
    #Upper case
    print('Upper: ', actualLineValue.upper())
     #Inserting caracters between the caracteres
    print('Cancating some letters: ', ' '.join(actualLineValue)) 
    #Resersing
    print('Reserve is: ', ''.join(reversed(actualLineValue)))    
    #Spliting the sentence to an array of words
    #TO DO learn how to use a array
    #print('The second word is: '. actualLineValue.split())    
    #Remove Caracter
    print('Without a: ', line.split('a'))
    #replace a string
    print('Replacing @: ', actualLineValue.replace('@', "MARCELO").upper())
    
    #Find de max caracter
    #left the code if the line has just blank spaces
    #if(len(actualLineValue) > 0):
    if(actualLineValue.isspace()):
        print('Max string code' ,max(line.strip()))
    count = count + 1
    
    print('\t')
    
    #Using the count to scape of the loop
    if(count == 10):#1910
        break
    
print(count,"Lines")
