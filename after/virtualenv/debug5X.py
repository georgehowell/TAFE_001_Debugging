
#	Cert III Python Programming
#	Practical Debug Exercise 5

#	Description:
#	the program is to find the index of an item in a list

#	Sample output

#   The list is [5,2,8,9,3,11,4,1]
#   Enter the number to find int the list : 9
#   the index of the number 9 in the list is 3


# alt solution: convert List to 'str'
# theList = ['5','2','8','9','3','11','4','1']

theList = [5,2,8,9,3,11,4,1]

print ("The list is ", theList)
num = int(input("Enter the number to find in the list: "))  # convert input using "int()"

print (theList.index(num))