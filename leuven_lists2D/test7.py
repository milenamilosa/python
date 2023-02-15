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
# we need to count always from "start" (1) to "to" (chosen number)
# "start" is multiplied by n
# n += 1 every loop. n max is 10
# start += 1
# inner loop  --> start*n
# outer loop --> start+=1

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






