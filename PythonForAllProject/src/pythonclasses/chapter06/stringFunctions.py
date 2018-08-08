fh = open("C:\\Python\\pi4e\\Python\\PythonForAllProject\\resources\\mbox-short.txt", "r")

count = 0
for line in fh:
    actualLineValue = line.strip()
    #left the code if the line has just blank spaces
    if(len(line) <= 2):
        print('Blank line')       
        continue 
    #Upper case
    print('Upper: -->', actualLineValue.upper())
    #Lower case
    print('Lower: -->', actualLineValue.lower())   
    #Inserting caracters between the caracteres
    print('Cancating some letters: -->', ' '.join(actualLineValue)) 
    #Resersing
    print('Reserve is: -->', ''.join(reversed(actualLineValue)))
    #replace a string
    print('Replacing a with @: -->', actualLineValue.replace('a', "@").upper())
    #Using a caracter do separate in a array 
    print('Splited in a array of words: -->', line.split())
    #Spliting the sentence to an array of words    
    print('The first word is: -->', actualLineValue.split()[0])    
    print('The first 3 letters are: -->', actualLineValue.split()[1][0:3])
    print('The 3 until 6 letters are: -->', actualLineValue.split()[1][3:6])
  
    #Finding out in a string 
    if('celo' in line):
        print('Existe \'celo\' na frase no index ', line.find('celo'))
    else:
        print('Não existe \'celo\' na frase')    
    #Find de max caracter
    print('Max string code' ,max(line.strip()))
    count = count + 1
    
    print('\t')
   
   
print(count,"Lines")
