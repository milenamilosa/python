#ex1
my_matrix = [ [1, 2, 3, 4], [11, 22, 33, 44], [111, 222, 333, 444] ]

#print 1st row, 2nd column
print (my_matrix[0][1])
print ("\n")
#Save a different number on the matrix position on the 3rd row, 4th column
my_matrix[2][3] = 0
print (my_matrix)

#Substitute the 1st row
my_matrix[0] = [2,1,8,-7]
print (my_matrix)
print ("\n")


#ex3
def pretty_printer(matrix, separator):
    for row in matrix:
        for element in row:
            print (element, end=separator)
        print ("\n")
            
matrix = [[345, 576, 393], [5, 4, 2], [45, 12, 0]]
separator = "_"
pretty_printer(matrix, separator)
print ("\n")


#ex4
def print_multiples(to):
    start = 1
    n = 1
    for row in range (start, to+1):
        n = 1
        for element in range (n, 11):
            result = start*n
            n+=1
            print (result, end = "\t")
        start += 1
        print ("\n")
    
print_multiples(12)



#ex6
my_list = [[1, 2, 3, 4, 5],
           [10, 20, 30, 40, 50],
           [11, 22, 33, 44, 55],
           [12, 34, 56, 78, 90]]
print (my_list)
print ("\n")

def show(my_list):
    print()
    for i in range (0, len(my_list)):
        print (my_list[i])

#6_1
def vertical_mirror(my_list):
    for i in range (0, int (len(my_list)/2)):
        my_list[i], my_list[len(my_list)-1-i] = my_list[len(my_list)-1-i], my_list[i]
        
    print ("vertical")
    return my_list
        
show(vertical_mirror(my_list))


#6_2
my_list = [[1, 2, 3, 4, 5],
           [10, 20, 30, 40, 50],
           [11, 22, 33, 44, 55],
           [12, 34, 56, 78, 90]]

def horizontal_mirror(my_list):
    for i in range (0, len(my_list)):
        var = int (len(my_list[i])/2)
        for j in range (0, var):
            my_list[i][j], my_list[i][len(my_list[i])-1-j] = my_list[i][len(my_list[i])-1-j], my_list[i][j]
    print ("horizontal")        
    return my_list
show(horizontal_mirror(my_list))
    
    
#6_3
def starry(my_list):
    for i in range( 0, len(my_list) ):
        for col_index in range( 0, len( my_list[ i ] ) ):
            if my_list[ i ][ col_index ] != " ":
                my_list[ i ][ col_index ] = '*'
    return my_list
show(starry(my_list))

#6_4
my_list = [[1, 2, 3, 4, 5],
           [10, 20, 30, 40, 50],
           [11, 22, 33, 44, 55],
           [12, 34, 56, 78, 90]]
def left(my_list,units):
    for i in range (0, len(my_list)):
        for j in range (0, len(my_list[i])):
            if j+units > len(my_list[i])-1:
                my_list[i][j] = " "
            else:
                my_list[i][j] = my_list[i][j+units]
            
    return my_list
show(left(my_list, 4))

#6_5
my_list = [[1, 2, 3, 4, 5],
           [10, 20, 30, 40, 50],
           [11, 22, 33, 44, 55],
           [12, 34, 56, 78, 90]]
def right(my_list,units):
    for i in range (0, len(my_list)):
        for j in range (len(my_list[i])-1, -1, -1):
            if j-units < 0:
                my_list[i][j] = " "
            else:
                my_list[i][j] = my_list[i][j-units]
            print (j)
    return my_list
show(right(my_list, 1))



