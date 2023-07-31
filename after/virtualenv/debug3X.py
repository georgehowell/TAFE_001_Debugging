
#	Cert III Python Programming
#	Practical Debug Exercise 3

#	Description:
#	The program will generate an array of 10 integers and fill the array with 10 random numbers.
#	It will then ask the user if it wants to generate another set of numbers, if the user selects presses 'n', the program should quit.

#	Sample output:

#	23 54 12 7 27 67 83 92 74 92
#	Would you like to generate another set of numbers? (y/n)
#	y
#	65 23 54 12 26 93 34 38 1 12
#	Would you like to generate another set of numbers? (y/n)
#	n

import random

numbers = []
choice = ''

running = True

while(running):

    for i in range(0,10):
         numbers.append(i)   # see https://www.stechies.com/indexerror-list-assignment-index-out-range/
         numbers[i]= random.randrange(1,100)
         print(numbers[i], end = " ")

    print ("")
    choice = input("Would you like to generate another set of numbers? (y/n)\n")
    print("")
    if choice == 'n':
        running = False


# numbers[i]= random.randrange(1,100) ...prints: "IndexError: list assignment index out of range"

