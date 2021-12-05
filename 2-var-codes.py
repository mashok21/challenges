''' Chapter 2: Variables, Expressions and Statements'''
# The str value type

print('Hello')
print('World')
print('Hello, World!')

# The print statement

print(1)
print(2)
print('Hello, World!')

# check value type

type('Hello, World!')
type(17)

# The float value type

type(3.2)

# Strings as numbers

type('17')

# Caution with large numbers

print(100,000,000)

# Variables and assignments

message = 'How are you?'
n = 20
pi = 3.14159

# Retrieving variables

print(message)
print(n)
print(ni)

# Value type of a variable

type(message)
type(n)
type(pi)

# Bad variable naming

100_days = 'games'
more@ = 1000
class  = 'Accounting'

# more examples of statements

print(message)
x = 2
print(x)
print(2+3)

# Examples of operations

minute = 59
hour = minute/60
print(hour)
hour = minute // 60
print(hour)

# Expressions

17
n
n + 17
1 + 1
5
x = 5
x + 1

# Order of precedence: examples

print(2 * 3 - 1)
print(1 + 1 ** 5 - 2)
print(2 * 1 + 1)
print(3 * 1 ** 3)

# More examples

print(6 + 4/2)
print(5 -3 - 1)


# Modulus operator

quotient = 7 // 3
print(quotient)
remainder = 7 % 3
print(remainder)

# String operators

first = "Hello"
second = ' World!'
print(first + second)

# string operations: Using *

first = 'Text'
second = 3
print(first * second)

# User input: example

inp = input()
print(inp)

# User input: example..

name = input('What is your name?')
print(name)

# User input example...

message = "What is your name?"
name = input(message)
print(name)

# User input data type

prompt = "What is the speed of an eagle?"
speed = input(prompt)

# User input data type..

speed = input(prompt)
type(speed)

# Changing user input data type

num = int(speed)
type(num)
print(num + 5)

# Naming variable

a = 35.0
b = 12.5
c = a * b
print(c)

# Mnemonic variable names

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

# Common Errors and Debugging
# Semantic error

print(1.0 / 2.0 * pi)
print(1.0 / (2.0 * pi))

# Common Errors and Debugging
# Syntax error

bad name = "Tom"
month = 09
principle = 327.68
interest = principal * rate