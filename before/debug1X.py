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


a=0                 # intialisation of variables
b=0
c=0

print("This program will swap 2 variables.")

a = 2
b = 7

print(" a = " , a , ", b = ",b)

a = b
c = a
b = c

print(" a = ", a, ", b = ", b)