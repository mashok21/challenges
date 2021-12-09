''' chapter 5 - Iteration '''

# Updating Variables
x = 0
x = x + 1
print(x)

#The while Statement: example

n = 5 # initializer
while n > 0:
	print(n)
	n = n - 1
print('blastoff')

# Infinite loop

n = 0
while True:
	print(n, end = ' ')
	n = n - 1
print('Done')

# Infinite Loop: with break​

while True:
	line = input('>')
	if line == 'done':
		break​
	print(line)
print('We are done')

