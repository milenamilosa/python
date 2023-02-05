# #function definition
# def hello_function():
#     print ("Hello, world!")
# 
# #main function/function call
# hello_function()
# print ("\n")
# 
# #ex1
# def hello_function(name):
#     print ("Hello,", name)
# 
# hello_function("Milena")
# hello_function("Cassie")
# 
# print ("\n")
# 
# #ex2
# def hello_to(name, place):
#     print ("Hello,", name, ", and welcome to", place)
# 
# hello_to("Milena", "your room")
# print ("\n")
# 
# #ex3
# def calculate_area(radius):
#     pi=3.14
#     area=radius*radius*pi
#     if pi == 3 or pi == 3.1:
#         print ("error – pi not exact enough")
#     else:
#         print ("The area of the circle is", area)
# calculate_area(4)
# print ("\n")
# 
# #ex4
# def greet_based_on_name_length(name):
#     letter = 0
#     for i in name:
#         letter +=1
#     if letter >= 4:
#         print ("Hello,", name, "you have quite a long name")
#     else:
#         print ("Hello,", name, "you have a short name")
# 
# greet_based_on_name_length("Pasa")
# print ("\n")
# 
# #ex5
# def greet_based_on_name_length(name):
#     letter = 0
#     value = 10
#     for i in name:
#         letter +=1
#     if letter >= value:
#         print ("Hello,", name, "you have quite a long name")
#     else:
#         print ("Hello,", name, "you have a short name")
# 
# greet_based_on_name_length("Milena")
# print ("\n")
# 
# #ex6
# def greet_full_or_not(name, full):
#     if full == 1:
#         print ("Hello", name, "I hope you have a pleasant day")
#     if full == 0:
#         print ("Hello", name)
# greet_full_or_not("Milena", True)
# print ("\n")
# 
# #ex7
# def alcohol(percentage):
#     if percentage >=0 and percentage < 0.5:
#         print ("no fine")
#     elif percentage >=0.5 and percentage < 0.8:
#         print ("Fine is 50$.")
#     elif percentage >=0.8 and percentage < 1.5:
#         fine = 50+(((percentage-0.8)/0.7)*100)
#         print (fine)
#     elif percentage >=1.5:
#         print ("Fine is 250$. You are in mortal danger.")
#     else:
#         print (percentage, "Error, negative value detected")
# alcohol(1.6)
# print ("\n")
# 
# #ex8_0
# def movie_access(age, suitable):
#     if age >=18:
#         print ("Age is", age)
#         if suitable == "yes":
#             print ("Movie is suitable for adults")
#         else:
#             print ("Movie is not suitable for adults")
#     else:
#         print ("Age is", age)
#         if suitable == "yes":
#             print ("Movie is suitable for children")
#         else:
#             print ("Movie is not suitable for children")
# 
# movie_access(2, "no")
# print ("\n")
# 
# #ex8_1
# def movie_access_alt(age_restricted, age_of_visitor):
#     if age_restricted == "no":
#         print ("Welcome to this family movie")
#     else:
#         if age_of_visitor < 18:
#             print ("Please leave")
#         else:
#             print ("Welcome!")
# 
# movie_access_alt("yes", 23)   
# print ("\n")
# 
# #ex8_2
# def movie_access_alt(age_restricted, age_of_visitor):
#     if age_restricted == "no":
#         print ("Welcome to this family movie")
#     else:
#         if age_of_visitor < 18:
#             print ("Please leave")
#         else:
#             print ("Welcome!")
# 
# movie_access_alt("yes", 23)   
# print ("\n")

#ex9
def whether_multiple_of_2_and_or_3(number):
    '''	Decides if the number is the multiple of 2 or 3 or both.
        Prints the result.
    '''
    if number % 2 == 0:
        print (number, "is a multiple of 2")
        if number % 3 == 0:
            print (number, "is a multiple of 3")
            print (number, "is multiple both of 2 and 3")
        else:
            print (" ")
    else:
        print (" ")
        if number % 3 == 0:
            print (number, "is a multiple of 3")
        else:
            print (number, "is not a multiple nor of 2 neither of 3")

whether_multiple_of_2_and_or_3(6)
print ("\n")

#ex9_alt

def whether_multiple_of_2_and_or_3(number):
    if number % 2 == 0 and number % 3 == 0:
        print (number, "is multiple both of 2 and 3")
    elif number % 3 == 0:
        print (number, "is a multiple of 3")
    elif number % 2 == 0:
        print (number, "is a multiple of 2")
    else:
        print (number, "is not a multiple nor of 2 neither of 3")

whether_multiple_of_2_and_or_3(20)
print ("\n")

#ex10
def time_conv(hour, min):
    '''Converts and prints time from 24h system to 12h system.
    '''
    if hour < 0 or hour > 23:
        print ("Change value of hour")
    elif min < 0 or min > 59:
        print ("Change value of min")
    elif hour >= 12 and hour < 24:
        hour = hour - 12
        print (hour,":",'%02d' % min,"pm")
    else:
        print (hour,":",'%02d' % min,"am")
time_conv(23, 5)

