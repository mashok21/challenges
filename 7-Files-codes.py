''' Chapter 7: Files '''

# Text files: newline

message = 'Hello\nWorld!'
print(message)

thing = 'x\ny'
print(thing)
print(len(thing))

# Reading contents of a file

fhand = open('alice.txt')

# Reading file contents: for loop​

fhand = open('alice.txt')
count = 0
for line in fhand:
	count = count + 1
print(count)


# Read method

fhand = open('alice.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Count characters using loop​

fhand = open('alice.txt')
count = 0
for line in fhand:
	for ch in line:
		count = count + 1
print(count)

# Searching through a file

fhand = open('alice.txt')
for line in fhand:
	if line.startswith('Alice'):
		print(line)

# Searching a file: alternative

fhand = open('alice.txt')
for line in fhand:
	line = line.strip()
	if line.find('Alice') == 0:
		print(line)

# The extra newline space

fhand = open('Alice.txt')
for line in fhand:
	print(line)

# Removing the extra newline

fhand = open('alice.txt')	
for line in fhand:
	line = line.rstip()
	print(line)

# Writing files

fhandle = open(‘sample.txt’, ‘w’)​
line1 = 'This is the first line\n'
fhandle.write(line1)​
line2 = 'This is the second line\n'
fhandle.write(line2)​
fhandle.close()​

# View file

fhandle = open('sample.txt', 'r')
for line in fhandle:
	print(line)
fhandle.close()

# Append line

fhandle = open('sample.txt', 'a')​
line3 = 'This is the third line \n'
fhandle.write(line3)​
fhandle.close()​

# Viewing file

fhandle = open('sample.txt', 'r')​
for line in fhandle:​
	print(line)​
fhandle.close()​