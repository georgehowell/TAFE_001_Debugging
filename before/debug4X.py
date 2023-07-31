
#	Cert III Python Programming
#	Practical Debug Exercise 4

#	Description:
#	The program is to accept a word from the user and then prints that word out in revers.

#	Sample output

#   enter a word: fred
#   fred in reverse is derf

word = input ( "enter a word : ")
reverseword = ""
for char in word:
    reverseword = reverseword + char

print(word + " in reverse is " + reverseword)
