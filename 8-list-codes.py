''' Chapter 8: Lists '''

# List: Creation

[10,  20, 30, 40]​

['eggs', 'spam']​
['David', 'Estelle', 'Kim', 'Charlie']
​['spam', 2, 5, [10, 20]]

# List: Assignment

cheeses = ['cheddar', 'edam', 'gouda']
numbers = [17, 123]​
empty = []
print(cheeses, numbers, empty)

​
# List: Mutability

print(cheeses[0])
numbers = [17,123]​
numbers[1] = 5​
print(numbers)​

# Lists: in

cheeses = [‘cheddar’, ‘edam’, ‘gouda’]​
print('edam' in cheeses​)
print('brie' in cheeses​)​

# Traversing a list

for cheese in cheeses:
	print(cheese)

# The range function: example​

print(range(0,4))


# Mutability: range, len

numbers = [2,4,6,8]​
for i in range(len(numbers)):​
	numbers[i] = numbers[i] * 2​
    print(numbers)​

# List Operations

a = [1,2,3]​
b = [4,5,6]​
c = a + b​
print(c)
print([0] * 4​​)
print([1,2,3] * 3​)

# List Slices

t = ['a', 'b', 'c', 'd', 'e', 'f']​

print(t[1:3])​
print(t[:4])​
print(t[3:])​

# List: omit index positions​

print(t[:])

# List: Copy

t = ['a', 'b', 'c', 'd', 'e', 'f']​
T1 = t[:]

# List: replacing elements

t = ['a', 'b', 'c', 'd', 'e', 'f']​
t[1:3] = ['x', 'y']
print(t)

# List method: Append

t = ['a', 'b', 'c']
t.append('d')
print(t)

# List method: extend

t1 = ['a', 'b', 'c']
t2 = ['d', 'e'] 
t1.extend(t2)
print(t1)

# List method: sort

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

# Deleting Elements

t = ['a', 'b', 'c']
t.pop(1)
print(t)

​# del operator

t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']​
del t[1:5]
print(t)

# Deleting Elements: remove method

t = ['a', 'b', 'c']
t.remove('b')
print(t)

# List: functions

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
average = sum(nums)/lens(nums)
print(average)

# Adding numbers: without list

total = 0
count = 0
while True:
	inp = input()
	if inp == 'done': 
		break
	total = total + float(inp)
	count = count + 1
print(total/count)

# Adding numbers: using lists

numlist = list()​

while True:​
	inp = input()​
    if inp = ‘done’: 
    	break​
	value = float(inp)​
	numlist.append(value)​
	print(sum(numlist)/len(numlist))​

# Strings to list conversion

s = ‘spam’​
t = list(s)​
print(t)​

# List: split method

s = 'This too is a string'
t = s.split()​
print(t)​

# List: split function, delimiter​

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
print(s)

# The join method: example​

t = ['I', 'like', 'ice-cream']​
delimiter = ' '
delimiter.join(t)​
print(t)​

# Variables and Objects​

a = 'banana​'
b = 'banana​'
print(a is b​)
a = [1,2,3]​
b = [1,2,3]​
print(a is b​)

# Aliasing

a = [1,2,3]​
b = a​
print(b is a​)

# Aliasing: mutability

b[0] = 5​
print(a)​

# List: copy

a = [1,2,3]​
b = a[:]​
b[0] = 5​
print(a)​

# Debugging
#correct
t = [1,2,3,4]​
t.append('hello')

#wrong
t.append(['hello'])​
t = t.append('hello')​
t + 'hello'