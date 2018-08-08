#7.1Write a program that prompts for a file name, then opens that file and reads through the file, 
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.


# Use words.txt as the file name
##fname = input("Enter file name: ")
#fh = open('words.txt')
#print(fh.read().upper().strip())


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt
#as the file name.

# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("mbox-short.txt")
sumValues = 0.0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
        sumValues = sumValues + float(line[line.find('0'):])
        count = count + 1
        #print(line[line.find('0'):])
        #print(sumValues)
    
print("Average spam confidence:",sumValues/count)
