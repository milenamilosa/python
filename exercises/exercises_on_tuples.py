# Python Tuple
# Python Tuple is a collection of objects separated by commas.
# In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition
# but a tuple is immutable, unlike lists which are mutable

#     Exercise 1: Reverse the tuple
#     Exercise 2: Access value 20 from the tuple
#     Exercise 3: Create a tuple with single item 50
#     Exercise 4: Unpack the tuple into 4 variables
#     Exercise 5: Swap two tuples in Python
#     Exercise 6: Copy specific elements from one tuple to a new tuple
#     Exercise 7: Modify the tuple
#     Exercise 8: Sort a tuple of tuples by 2nd item
#     Exercise 9: Counts the number of occurrences of item 50 from a tuple
#     Exercise 10: Check if all items in the tuple are the same

#ex1
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]	#reversing/iterating from the end
print(tuple1)
print()


#ex2
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
print()

#ex3
tuple1 = (50, )
print(tuple1)
print()

#ex4
tuple1 = (10, 20, 30, 40)
# unpack tuple into 4 variables. should be able to access each variable separately
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
print()

#ex5
tuple1 = (11, 22)
tuple2 = (99, 88)
a, b = tuple1
c, d = tuple2
tuple1 = c, d
tuple2 = a, b
print(tuple1)
print(tuple2)
print()

#or
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)
print()

#ex6
tuple1 = (11, 22, 33, 44, 55, 66)
a, b, c, d, e, f = tuple1
tuple2 = d, e
print(tuple2)
print()

# correct option
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:4] # getting element under index 3 (3 is included, 4 is not)
tuple3 = tuple1[3:-1] # getting elements under indexes 3 and 4
# -1 means going from the last element (0, -1, -2 etc. to iterate from end)
# use for convenience
# tuple1[3:-1] = tuple1[3:5]
print(tuple2)
print(tuple3)
print()

#
t1 = (10,20,30,40,50,60,70,80,90,100)
t2 = t1[2:-2] # 2 is included,  -2 is not
print(t2)
print()

#ex7
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
print()

#ex8
# lambda
# lambda is a keyword in Python for defining the anonymous function. argument(s) is a placeholder,
# that is a variable that will be used to hold the value you want to pass into the function expression.
# A lambda function can have multiple variables depending on what you want to achieve.

#     Syntax: lambda arguments: expression
# 
#         This function can have any number of arguments but only one expression, which is evaluated and returned.
#         One is free to use lambda functions wherever function objects are required.
#         You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#         It has various uses in particular fields of programming, besides other types of expressions in functions.
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
print()


#ex9
tuple1 = (50, 10, 60, 70, 50)
count = 0
for i in tuple1:
    if i == 50:
        count += 1
print (count)
#or
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
print()

#ex10
tuple1 = (45, 45, 45, 45)
for i in range (0, len(tuple1)-1):
    if tuple1[i] == tuple1[i+1]:
        True
    else:
        False
if True:
    print(True)
    
# correct option
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

# Метод grid() позволяет поместить виджет в определенную ячейку условной сетки или грида.
# Метод grid применяет следующие параметры: column: номер столбца, отсчет начинается с нуля row: номер строки, отсчет начинается с нуля
# Grid - сетка, таблица - один из трех управляющих размещением, или менеджеров геометрии
