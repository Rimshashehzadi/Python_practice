#Comments
'''Comments can be used to explain Python code.

#Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.'''

#To add a multiline comment you could insert a # for each line:
#Python has no command for declaring a variable.

#A variable is created the moment you first assign a value to it.

# Variable Declaration
x = 5
y = 'Rimsha'
print(x)
print("My name is",y)    #concatination use for printing multiple values

#Casting
x = int(4)
y = str('Rimsha')
z=  float(4)
print(type(x))  #type() is the build in function of python that tells the type of variable
print(type(y))
print(y)
print(f"The value of z is {z} the type of z is {type(z)}")  #f-string is used for formatting strings in python

'''A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.'''

#Came Case
myName = 'Rimsha'
#PascalCase
MyName = 'Rimsha'
#Snake Case
my_name = 'Rimsha'

#Many values to multiple variable

# x,y,z = 'rimsha','alina','faiza'


# One value to multiple variable

 # x = y = z = 'rimsha'


#Output variable

# x = "My country name is Pakistan"
print(x)   # print here ' x ' value

# Global variable

#Global variables can be used by everyone, both inside of functions and outside.

# x = "awesome"

# Global variables

def myfunc():
  global x
  x = "fantastic"

myfunc()

#print("Python is " + x)        
#print("Python is " + x)            # 'x' is a global variable 
