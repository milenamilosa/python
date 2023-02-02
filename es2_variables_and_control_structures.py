#ex1
name = "Milena"
age = 20
print (name, "-", age, "years old")
age +=1
print (name, "-", age, "years old")
print ("\n")


#ex2
pi = 3.14
radius = 10
area = pi*radius*radius
print ("%.1f" % area)
circumference = 2*pi*radius
print ("%.1f" % circumference)
print ("\n")


#ex3
floor = 50
while floor < 55 and floor > 0:
    floor +=1
    print (floor)
if floor == 55:
    print ("DING!")
print ("\n")


#ex4
name = "Mi"
letter = 0
for i in name:
    letter +=1
if letter < 4:
    name = name+name
    print (name)
else:
    print (name)
print ("\n")

#ex5
pi = 3.14
radius = 2
if radius >= 0:
    area = pi*radius*radius
    print ("%.1f" % area)
    circumference = 2*pi*radius
    print ("%.1f" % circumference)
    print ("\n")
else:
    print ("error – radius negative")
print ("\n")

#ex6
pi = 3.14
radius = 6
if pi == 3 or pi == 3.1:
    print ("error – pi not exact enough")
else:
    if radius >= 0:
        area = pi*radius*radius
        print ("%.1f" % area)
        circumference = 2*pi*radius
        print ("%.1f" % circumference)
        print ("\n")
    else:
        print ("error – radius negative")
print ("\n")

#or

pi = 3.14
radius = 7
if pi == 3 or pi == 3.1:
    print ("error – pi not exact enough")
elif radius < 0:
    print ("error – radius negative")
else:
    area = pi*radius*radius
    print ("%.1f" % area)
    circumference = 2*pi*radius
    print ("%.1f" % circumference)
    
print ("\n")


#ex7
number = 5
if number % 2 == 0:
    print ("even")
else:
    print ("odd")
print ("\n")

#ex9 only upwards going lift
floor = 1
min_floor = 0
max_floor = 60
if floor < min_floor:
    print ("error – too low")
elif floor > max_floor:
    print ("error – too high")
elif floor == min_floor or floor == max_floor:
    print ("DING!")
else:
    while floor % 10 != 0:
        floor +=1
    while floor % 10 == 0:
        print (floor)
        floor +=10
        if floor == max_floor:
            print (max_floor)
            print ("DING!")
            break
        
print ("\n")