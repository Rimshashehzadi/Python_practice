#Variables can store data of different types, and different types can do different things.
 #Number types
# 1.int
# 2.float
# 3. complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# 1.int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # type() is a function that tell  data type of variable

print(type(y))
print(type(z))

#float

#x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#complex
#x = 3+5j
#y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#convert from one type to another

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random number
'''Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
'''
#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

#Casting

#For int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#For float

# x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
# For String

'''x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''
