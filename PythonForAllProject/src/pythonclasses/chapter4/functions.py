
msg1Pt = None
msg2Pt = None
msg1Eng = 'Hello'
msg2Eng = 'Using a function'
numberList = 1,2,3,4,5,6,8,65

def writeInPrompt(lang):
    if(lang == 'pt-br'):
        print(msg1Pt)
        print(msg2Pt)    
    else:
        print(msg1Eng)
        print(msg2Eng)

def setMsg(str1, str2):
    msg1Pt. = str1
    msg2Pt = str2

def printMaxNumberOfAnArray():
    print(max(numberList))

def addNumber(int1, int2):
    print('Sum of' , int1, ' and ', int2, int1 + int2)

setMsg('Olá', 'Usando uma função')
print('msg1Pt -->', msg1Pt)
writeInPrompt('pt-br')
writeInPrompt('')
addNumber(5,10)