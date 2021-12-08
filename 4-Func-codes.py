''' Chapter 4: Functions '''

# built-in functions

type(32)

# built-in functions: examples

print(min(1,2,3,4,5))
print(min(10,20,30,40))
print(max(1,2,3,4))
print(max(10,20,30,40))

# built-in functions: examples...

print(len('Hello'))
print(len('Hello, World!'))
print(round(3.14567, 2))

# Type conversion function

print(int('32'))
print(int(3.99))
print(int(-2.3))

# Type conversion function...

print(float(32))
print(float('3.14159'))
print(str(32))


# Module: dot notation
import math # enter this function at the top of the file
math.factorial(4)
math.sqrt(100)
math.pow(3,2)

# User-defined functions

def print_lyrics():
	print("I'm a lumberjack, and I'm okay")
	print("I sleep all night and I work all day")

# Function: calling

print(print_lyrics)

# Function: defining

def print_msg():
	print('Hello')
	print('How are you?')

# Function: calling

print(print_msg)

# Nested functions

def repeat_msg():
	print('Main function before passing control to another function')
	print_msg()
	print('Now main function is in control')


# Parameters and arguments...

def print_msg(message):
	print(message)
	print(message)

# Parameters and arguments: ex

print_msg('Spam')
print_msg(17)

# Parameters and arguments: ex

greet = 'How, how have you been?'

print_msg(greet)

# Void functions

result = print_msg('Hello')
print(result)

# Fruitful function

def addtwo(a,b):
	added = a + b
	return added

x = added(2,3)
print(x)


