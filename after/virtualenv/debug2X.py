#

#	Cert III Python  Programming
#	Practical Debug exercise 2

#	Description:
#	The program asks the user to choose 2 chemicals out of Red Green or Blue.
	#The program will then output a result based on the following rules:

#		-	If Red is chosen at all, the compound immediately begins to bubble
#		-	If Red is mixed with Green, it explodes
#		-	If Red is mixed with Blue, it melts
#		-	If Green is mixed with Blue, it freezes
#		-	If 2 of the same chemical is used, nothing happens.

#	----- Expected output sample 1:---

#	Choose the first chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	1

#	Choose the second chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	3

#	The compound immediately begins to bubble, then
#	The compound EXPLODES!

#	----- Expected output sample 2:-----

#	Choose the first chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	2

#	Choose the second chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	1

#	The compound Freezes!

#	----- Expected output sample 3:-----

#	Choose the first chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	2

#	Choose the second chemical:
#	1 - Green
#	2 - Blue
#	3 - Red
#	3

#	The compound immediately begins to bubble, then
#	The compound Melts!




chemicalA=-1                # variable intialisation
chemicalB=-1
RED = 3                     # easier to read code if we use these variable names
GREEN = 1
BLUE = 2


print("Choose the first chemical:\n1 - Green\n2 - Blue\n3 - Red\n")

chemicalA = int(input("Choose the first chemical"))

print("Choose the second chemical:\n1 - Green\n2 - Blue\n3 - Red\n")

chemicalB = int(input("Choose the second chemical"))

print("")

# If red is ever chosen, the compound starts bubbling immediately
if (chemicalA == RED or chemicalB == RED):
    print("The compound immediately begins to bubble, then\n")

# Mix Green and Red and it explodes!


if (chemicalA == GREEN and chemicalB == RED) or (chemicalA == RED and chemicalB == GREEN):
    print("The compound EXPLODES!\n")

# Mix Green and Blue and it freezes!
if (chemicalA == GREEN and chemicalB == BLUE) or (chemicalA == BLUE and chemicalB == GREEN):  # 'and' not 'or'
    print("The compound Freezes!\n")

# Mix Red and Blue and it melts!
if (chemicalA == BLUE and chemicalB == RED) or (chemicalA == RED and chemicalB == BLUE):
    print("The compound Melts!\n")

if (chemicalA == chemicalB):
    print("Nothing happens...\n")
