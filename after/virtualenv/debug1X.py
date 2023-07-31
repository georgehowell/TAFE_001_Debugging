# Debugging exercise 1
#
#
#	Cert III Python Programming
#	Practical Debug Test 1

#	Description: A simple program that sets the value of 2 integers and swaps those values.

#	Expected output:

#	This program will swap 2 variables.
#	a = 2, b = 7
#	a = 7, b = 2

# intialisation of variables
a=0
b=0
c=0

print("This program will swap 2 variables.")

a = 2
b = 7

print(" a = " , a , ", b = ",b)

c = a
a = b
b = c

print(" a = ", a, ", b = ", b)

# reference: https://www.programiz.com/python-programming/examples/swap-variables