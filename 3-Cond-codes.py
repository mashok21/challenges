''' Chapter 3: Conditional Execution '''

print(5 == 5)
print(5 == 6)
print(5 != 5)

# Advanced conditionals

print(17 and True)
print(17 and False)
print(17 or False)
print(17 or True)

# Conditional Execution: more examples

x = 3
if x < 10:
	print('small')
print('done')

# Conditional Execution: examples

x = 3
if x < 10:
	print('small')
print('done')

# Alternative Execution

if x % 2 == 0:
	print('x is even')
else:
	print('x is odd')


# Examples: try and except

inp = input("Enter a Fahrenheit temp")
try:
	fahr = float(inp)
	cel = (fahr - 32) x 5/9
	print(cel)
except:
	print("Enter only numbers")


# Short circuit evaluation of logical expressions

x = 6
y = 2
print(x > 2 and (x/y) > 2)

# Guardian pattern

x = 1
y = 0
print(x > 2 and (x/y) > 2)

# Guardian pattern

x = 6
y = 0
print(x > 2 and (x/y) > 2)

# Guardian evaluation

x = 10
y = 0
print(x > 2 and y! = 0 and (x/y) > 2)
print(x > 2 and (x/y) > 2 and y!= 0)

