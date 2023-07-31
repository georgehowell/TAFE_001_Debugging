
#	Cert III Python Programming
#	Practical Debug Exercise 6

#	Description:
#	The program get a number from the userbetween 1 and 10.
#	Then the program is to print the following pattern

#	Sample output
#    enter a number (1..10): 6
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5
#   6 6 6 6 6 6

num = input ("enter a number (1..10): ")
for i in range(0, num):
    for j in range(i+1):
        print (i, end=" ")
    print ("")