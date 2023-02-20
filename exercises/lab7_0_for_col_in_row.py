#Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j.

#new way to create an "empty" 2d list (row 8)

row_num = 5
col_num = 5
array = [[0 for col in range(col_num)] for row in range(row_num)]
# literally  means [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]      or
# place 0 for every element in every row (row and col amount is given (row 6,7))

for row in range (row_num):
    for col in range (col_num):
        array[row][col] = row * col
 
print (array)
print ("")

# same thing but starting with really empty 2d list and using .append

matrix = []

for row in range(5):
    new_row = []
    for col in range(5):
        new_row.append(row * col)
    matrix.append(new_row)
print (matrix)
print ("")

for row in matrix:
    for el in row:
        print(el, end ="\t") # \t means "tab"
    print()

