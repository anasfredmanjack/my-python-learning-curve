##single quote stinrg
print('Hello')

##Double quotes string
print("Hello")

##how to output a single string 
print("he's a boy")

##how to output a single string by escapint the string character
print("he\'s a boy")

##How to get the position of a character within a string
greet = 'hello'
print(greet[0])
print(greet[1])
print(greet[2])
print(greet[3])
print(greet[4])
##How to get the position of a character within a string backwards
print(greet[-4])
print(greet[-3])
print(greet[-2])
print(greet[-1])
print(greet[-0])
##How to add two variables tpogether
str2 = 'friends'
concatenatedstring = greet+' '+str2
print(concatenatedstring)

##How to multiply string
greettimesfive = greet * 5
print(greettimesfive)

##string to uppercase method conversion 
print(greettimesfive.upper())

##how to split by character 
cheese = 'burger, chicken, goat'
print(cheese.split(' '))

##how to calculate the length of a string in python
cheselength = len(cheese)
print(cheselength)
