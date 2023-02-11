#creating lists
my_list = [4, 334, 76, 768, -4345, 78, -3, 0, 54]

#this is how to get whole list
print (my_list)

#this is how to get the index of value that is in the list
print (my_list.index(78))

#this is how to get an element that is under a certain index on the list
element = my_list[8]
print (element)

#creating a sublist. first index is included, last is not!!! so [1:4] contains 1th, 2d and 3d element
print(my_list[1:4])

#replacing elements using index in square brackets
my_list[4] = 20
print (my_list) #new list is printed

#add elements to list
#start by combining 2 lists
#to store new list inside the same value just do not rename combined list to smth new
my_list = [4, 334, 76, 768, -4345, 78, -3, 0, 54]
other_list = [1, 2, 3]
combined_list = other_list + my_list

#to store in the same list type in "my_list = " and it saves new list under the name of the first list created
#order of lists is relevant!
print (combined_list)

#add 1 element to the list
my_list = my_list + [32] #variables are also added in square brackets
print (my_list)

# to delete element from the list
del my_list[7]
print (my_list)

#lenght of the current list in elements
print (len(my_list))

#sorting
sorted(my_list) # non destructive operation
# which means if we want to print this function, we need to assign it to a varriable
# sorts numbers form small to large, strings in alfabetical order.
# to get more complex sorting, u need to write the code urself
my_list = sorted(my_list)
print (my_list)

#to refer to each element
for element in my_list:
    print(element)

#to get all elements in certain range
for index in range (0, len(my_list)):
    if index%2==0:
        print(my_list[index])

#to get all elements from first to last
index = 0
while index < len(my_list) -1 :
    index +=1
    print(my_list[index])

print (my_list)

#to get all elements from the last one to the first (so, backwards) (modified)
index = len(my_list) - 1
while index >= 0:
    print(my_list[index])
    index -=1

#function that calculated ther average of the elements on the list
def calc_average(num_list):
    result = 0
    for number in num_list:
        result = result + number
    return result / len(num_list)

print(calc_average([1, 2, 3, 4, 7, 4, 7, 3]))
# u can write elements in square brackets like upwards
# but you also can add a list like below
def calc_average_with_list(num_list):
    result = 0
    for number in num_list:
        result = result + number
    return result / len(num_list)

my_list = [4, 334, 76, 768, -4345, 78, -3, 0, 54]
print(calc_average_with_list(my_list))

# string = an array of chars
#string = a list of characters
some_string = "text"
print (some_string.index("x"))
print (some_string[2])
print (some_string[1:3])

some_string = some_string + "books"
print (some_string)
print (len(some_string))

# with strings U CANT REPLACE ELEMENTS (characters), U CANT DELETE ELEMENTS 	
