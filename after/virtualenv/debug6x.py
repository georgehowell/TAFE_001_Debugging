
#	Cert III Python Programming
#	Practical Debug Exercise 6

#	Description:
#	The program gets a number from the user between 1 and 10.
#	Then the program prints the following pattern

#	Sample output
#    enter a number (1..10): 6
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5
#   6 6 6 6 6 6

num = input("enter a number (1..10): ")
num = int(num)  # convert input using "int()"
for i in range(0, num+1):   # "+1" to include input number, as range is always one short
    for j in range(i+1):
        print(i, end=" ")
    print("")