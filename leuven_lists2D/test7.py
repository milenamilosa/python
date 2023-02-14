#ex1
my_matrix = [ [1, 2, 3, 4], [11, 22, 33, 44], [111, 222, 333, 444] ]

#print 1st row, 2nd column
print (my_matrix[0][1])

#Save a different number on the matrix position on the 3rd row, 4th column
my_matrix[2][3] = 0
print (my_matrix)

#Substitute the 1st row
my_matrix[0] = [2,1,8,-7]
print (my_matrix)