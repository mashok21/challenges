''' Chapter 6: Strings '''

# Strings Index

fruit = 'banana'
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)

# String Index, len

fruit = 'banana'
print(len(fruit))

length = len(fruit)
last = fruit[length] # index error
print(last) # index error
last = fruit[length - 1]
print(last)

# String Index, reverse

print(fruit[-1])
print(fruit[-2])

# String: Loop

index = 0
while index < len[fruit]:
	letter = fruit[index]
	print(letter)
	index = index + 1

# String: for loop

for char in fruit:
	print(char)

# String: slices

s = 'Monty Python'
print(s[0:5])
print(s[6:12])

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[:])

# Strings are immutable

greetings = 'Hello, World!'
greetings[0] = 'J'

new_greetings = 'J' + greetings[1:]
print(new_greetings)

# Loop and count

word = 'banana'
count = 0

for letter in word:
	if letter == 'a':
		count = count + 1
print(count)

# The in Operator

print('a' in 'banana')
print('b' in 'banana')

# String Methods

word = 'banana'
print(word.upper())

# String Methods: find

word = 'banana'
index = word.find('a')
print(index)

print(word.find('na'))
print(word.find('na', 3))

# String Methods: strip

line = '    Here we go  '
line.strip()
print(line)

# String Methods: lower

line = 'Have a nice day'
line.lower()
print(line)
print(line.lower().startswith('h'))

# Parsing Strings

data = 'ashok@schoolofpython.com'
atpos = data.find('@')
print(atpos)

host = data[atpos+1:]
print(host)

atposend = data.find('.', atpos)
domain = data[atpos+1:atposend]
print(domain)

# String Format

age = 42
line = 'Hello Jim, you are %d years old' %age​
print(line)

# String Format: examples

age = 42.565
line = 'Hello Jim, you are %d years old' %age​
print(line)

name = 'Jim'
age = 42
line = 'Hello %s, you are %d years old' %(name, age)​