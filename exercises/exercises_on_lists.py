#     Exercise 1: Reverse a list in Python
#     Exercise 2: Concatenate two lists index-wise
#     Exercise 3: Turn every item of a list into its square
#     Exercise 4: Concatenate two lists in the following order
#     Exercise 5: Iterate both lists simultaneously
#     Exercise 6: Remove empty strings from the list of strings
#     Exercise 7: Add new item to list after a specified item
#     Exercise 8: Extend nested list by adding the sublist
#     Exercise 9: Replace list’s item with new value if found
#     Exercise 10: Remove all occurrences of a specific item from a list.

#ex1
list1 = [100, 200, 300, 400, 500]
list2 = []
n = 0
if len(list1)%2 == 0:
    for i in range (int (len(list1)/2), -1, -1):
        list1[n], list1[(len(list1)-1) - n] = list1[(len(list1)-1) - n], list1[n]
        n+=1
else:
    for i in range (int ((len(list1)-1)/2), -1, -1):
        list1[n], list1[(len(list1)-1) - n] = list1[(len(list1)-1) - n], list1[n]
        n+=1
print (list1)
print()

#another option
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
print()

#anther option
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)
print()

#ex2
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
n = 0
while n < len(list1):
    list3 = list3 + [list1[n] + list2[n]]
    n+=1
print (list3)
print()

#another option using zip
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
print()

#ex3
numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers = []
for i in numbers:
    new_numbers.append(i*i)
print (new_numbers)
print()

#ex4
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i+j)
print (list3)
print()

#another option
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [i + j for i in list1 for j in list2]
print(list3)
print()

#ex5
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3 = []

for i in range(0, len(list1)):
    var1 = list1[i]
    list3 = list3 + [var1]
for j in range(len(list2)-1, -1, -1):
    var2 = list2[j]
    list3 = list3 + [var2]
print (list3)
print()

#another, correct solution
#::-1 means itterating from the last element to the first
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print (i, j)
print()

#ex6
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1:
    if i == "":
        list1.remove(i)
print (list1)
print()

#another solution
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

list1 = list(filter(None, list1)) # remove None from list1 and convert result into list
print(list1) 
print()

#ex7
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print (list1)
print()

#ex8
#.extend
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)
print()

#ex9
list1 = [5, 10, 15, 20, 25, 50, 20]
number = 20

for i in range (0, len(list1)):
    if list1[i] == number:
        list1[i] = 200
        break
print(list1)
print()

#another option
list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)

list1[index] = 200
print(list1)
print()

#ex10
list1 = [5, 20, 15, 20, 25, 50, 20]
element = 20
while element in list1:
    list1.remove(20)
print(list1)
print()

#another option
list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

list1 = remove_value(list1, 20)
print(list1)



