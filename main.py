'''
05/03/2021

Review

Recursion

def Function(Parameter):
	if ():		# Base Condition
		return something
	else:
		return something + Function(Parameter +/- 1)



# 2. Fibonacci Sequence With a Recursive function
# 0, 1 > 1 > 2 > 3 > 5 > 8 > ..

def fibonacci(n):
	if (n <= 1):
		return n
	else:
		return (fibonacci(n-1) + fibonacci(n-2))

nterm = int(input("How many terms? "))

if (nterm <= 0):
	print ("Please enter a positive integer.")
else:
	print ("Fibonacci Sequence: ")

	for i in range(nterm):
		print (fibonacci(i))


# 3. Fibonacci Sequence With a loop
n1, n2 = 0, 1
count = 0

nterm = int(input("How many terms? "))

if (nterm <= 0):
	print ("Please enter a positive integer.")
else:
	print ("Fibonacci Sequence: ")

	while (count < nterm):
		print (n1)
		nth = n1 + n2

		n1 = n2
		n2 = nth
		count += 1


Access values in String
- To access substrings, Use the square bracets for slicing along with the index or indicies to obtain your substring.

var = "Hello"

# Individual
string: 		|		H		|		e		|		l		|		l		|		o		|
positive:		|		0		|		1		|		2		|		3		|		4		|
negative:		|		-5	|		-4	|		-3	|		-2	|		-1	|

# Consective
string: 		|		H		|		e		|		l		|		l		|		o		|
index:			0				1				2				3				4				5

In case of printing consecutive characters, it needs to start beginning index and colon, then ending index

ex) print "ello" from var
print (var[1:])

List1 = ["a","b","g","y","j","k","h"]
print (List1[1:4])

string = "student"
print (string[3:])
'''


var1 = "Hello World!"
var2 = "Python Programming"

# 1. print 'h' from var 2
print (var2[3])
print (var2[-15])

# 2. print 'hi' from var1 and var2
print (var1[0] + var2[15])
print (var2[3] + var2[15])