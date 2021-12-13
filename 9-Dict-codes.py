''' Chapter 9- Dictionary '''

# Creating a dictionary

eng2sp = dict()​
print(eng2sp)​

# Dictionary: adding an item​

eng2sp['one'] = 'uno'

# Accessing a dictionary​

print(eng2sp)​

# Adding more items​

eng2sp['two'] = 'dos​'
eng2sp['three'] = 'tres'

# Accessing values​

print(eng2sp['two'])​

# Missing values​

print(eng2sp['four'])​

# The len function​

print(len(eng2sp))

# The in operator​

print('one' in eng2sp)​​

# The in operator (missing)​

print('uno' in eng2sp​)

# Value in a dictionary

vals = list(eng2sp.values())​

# Value in a List​

print('uno' in vals​)
print(eng2sp.values())​

# File open and initiate a dictionary​

fhandle = open(‘alice.txt’)​
dt = dict()​

# Looping through a dictionary​

for line in handle:​
	words = line.split()​

# Looping through a dictionary​

for word in words:​

# Looping through a dictionary

dt[word] = 'somevalue'
print(dt)​

# The full code​

fhandle = open(‘alice.txt’)​
dt = dict()​
for line in handle:​
	words = line.split()​
	for word in words:​
		dt[word] = ‘somevalue’​
fhandle.close()​
print(dt)​

# Counters: The full program​

word = 'anthropology'
dt = dict()
for ch in word:
	if ch not in dt:
		dt[ch] = 1
	else:
		dt[ch] += 1
print(dt)

# The short code

word = 'anthropology'
dt = dict()
for ch in word:
	dt[ch] = dt.get(ch, 0) + 1


# The full code

fhand = open('alice.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print(counts)

# The improved code

import string
counts = dict()
for line in fhand:
	line = line.rstrip()
	line = line.translate(str.maketrans('', '', string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print(counts)

# Dictionary: Loop

marks = {‘Adam’: 80, ‘Jane’: 90, ‘David’: 85}​
for key in marks:
	print(key, marks[key])

# Dictionary: Key-value pair

for key in marks:
	if marks[key] > 80:
		print(key, marks[key])	

# Dictionary: sorting

lst = list(marks.keys())
print(lst)
lst.sort()
for name in lst:
	print(name, marks[name])

	