
##A list is a collection of items variables with different datatypes 
fib1 = [1,2,3,4,5,6,7,8,9]

##how to access an element in a list 
print(fib1[4])

##how to slice a python lists
print(fib1[0:4])

##how to concatenate lists
fib2 = [10,11,12,13,14,15]
print(fib1+fib2) 

##how to change a value in a list
fib1[2] = 0
print(fib1)

##how to append to an already existing list
fib1.append(89)
print(fib1)

##remove the last element in an already exiting list
fib1.pop()
print(fib1)

##how to remove the first instance or copy of an element in a list
fib1.append(89)
fib1.remove(89)
print(fib1)

##how to delete an index from a list or variable
del(fib1[4])
print(fib1)

##How to make a list within a list
chars = ['mario', 'anas', 'fred']
doublelists = [chars, fib1, fib2]
print(doublelists)
##How to access a list within a double list
print(doublelists[2])

##How to access an element in a list within a double list
print(doublelists[2][4])