#ex1
name = "Milena"
print ("Hello,", name)
print ("\n")


#ex2
hour = 23
min = 1
print ("it's")
if hour < 0 or hour > 23:
    print ("Change value of hour")
elif min < 0 or min > 59:
    print ("Change value of min")
elif hour >= 12 and hour < 24:
    hour = hour - 12
    print (hour,":",'%02d' % min,"pm")
else:
    print (hour,":",'%02d' % min,"am")
print ("\n")


#ex3
layer = 12
option = "c"

if option == "a":
    print("x" * layer)
elif option == "b":
    nr_of_spaces = 5 - layer
    spaces = " " * nr_of_spaces
    crosses = "*" * layer
    print(spaces + crosses)
elif option == "c":
    print("x " * layer)
else:
    print("error - please enter a valid option")

    

