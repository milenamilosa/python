number_one = 7
number_two = 7
if (number_one == number_two):
    print ( number_one )
else:
    print (" ")


number_one = 1
number_two = 2
if (number_one < number_two):
    print ( number_one )
else:
    print (" ")


a = 6
if (a % 2 == 0):
    print (a)
else:
    a = a + 1
    print (a)


a = 3
if (a == 1):
    print ("Number one")
elif (a == 2):
    print ("Number two")
else:
    print ("Neither one nor two")


LOOPS.
while - used for repeated execution as long as an expression is true
#Action is only carried out ifcondition (expression) followingwhile is true
#for - used to iterate over the elements of the sequents


a = 10
while a >= 0:
    print (a)
    a -=1	#a = a - 1


word = "Eellogofusciouhipoppokunurious"
letter = 0
for i in word:
    letter +=1
print (letter)


a = 0
while a <= 10:
    print (a)
    a +=2


word = "homicide"
letter = 0
for i in word:
    letter +=1
    print (i)


word = "homicide"
letter = 0
for i in word:
    letter +=1
    print ("homicide")


a = 455
while a != 10:
    if a<10:
        a +=1
    else:
        a -=1
print (a)


word1 = "bike"
word2 = "booba"
letter1 = 0
letter2 = 0
for i in word1:
    letter1 +=1
for i in word2:
    letter2 +=1
if letter1 > letter2:
    print ("Word 1 is longer than word 2")
elif letter1 < letter2:
    print ("Word 1 is shorter than word 2")
else:
    print ("Both words are the same lenght")


a = 2
b = 5
c = a*b
print (c)


a = 37
b = 5
if a % b == 0:
    print ("a is divisible by b without remainder")
else:
    print ("result has remainder")


if a % b == 0:
    print ("a is divisible by b without remainder")
elif a % b == 1:
    print ("remainder of the division is 1")
elif a % b == 2:
    print ("remainder of the division is 2")
elif a % b == 3:
    print ("remainder of the division is 3")
else:
    print ("remainder of the division is 4 and more")



