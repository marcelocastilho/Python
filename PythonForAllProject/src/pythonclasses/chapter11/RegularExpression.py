import re

x = 'My 2 favorite numbers are 34 and 99, and my e-mail is marcelocasnet@gmail.com aaa ssssss'

#Finding number
y = re.findall('[0-9]+', x)
print(y)

#Finding lowercase wors
z = re.findall('[a-z]+', x)
print(z)

#Finding lowercase and upperCase works
z = re.findall('[a-zA-Z]+', x)
print(z)

#Finding sentences stating with 'M'
w = re.findall('^M.', x)
print(w)

#Finding sentences stating with 'M' and   getting all the sentence
w = re.findall('^M.+', x)
print(w)

w = re.findall('e.+?3',x)
print(w)

w = re.findall('\S+@\S+', x)
print(w)

#Finding a word filtering the start of line + the word regular expressionm  
w = re.findall('^My .* (\S+@\S+)', x)
print(w)



# ^    Matches the beginning of a line
# $    Matches the end of the line
# .    Matches any character
# \s    Matches whitespace
# \S    Matches any non-whitespace character
# *    Repeats a character zero or more times
# *?    Repeats a character zero or more times (non-greedy)
# +    Repeats a character one or more times
# +?    Repeats a character one or more times (non-greedy)
# [aeiou]    Matches a single character in the listed set
# [^XYZ]    Matches a single character not in the listed set
# [a-z0-9]    The set of characters can include a range
# (    Indicates where string extraction is to start
# )    Indicates where string extraction is to end