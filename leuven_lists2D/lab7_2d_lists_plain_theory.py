#initialization
int_list = [ 8, 10, 12, -76, 144, 10 ]
string_list = [ "Jack", "Jill", "John" ]
bool_list = [ True, False, False, False ]
list_list = [ [ 8, 10, 12, -76, 144, 10 ], [ "Jack", "Jill", "John" ], [ True, False, False, False ] ] #bad example of a 2-dimensional list
list_2d = [ [ 1, 2, 3 ], [ 6, 5, 4 ], [ 12, 80, 99 ] ] #good example of a 2-dimensional list

print( int_list )
print( string_list )
print( bool_list )
print( list_list )
print( list_2d )

#accesing elements
list_2d = [ [ 1, 2, 3 ], [ 6, 5, 4 ], [ 12, 80, 99 ] ]

# row = list_2d[1]
# element = row[2]
# print( element )

element = list_2d[1][2] #the right way to call a certain element
print( element )

#replacing elements
list_2d = [ [ 1, 2, 3 ], [ 6, 5, 4 ], [ 12, 80, 99 ] ]

list_2d[1][2] = 20
print( list_2d )

#iteration
list_2d = [ [ 1, 2, 3 ], [ 6, 5, 4 ], [ 12, 80, 99 ] ]

#printing all elements of the 2D list
for row in list_2d:
    for element in row:
        print( element )
        
#same thing
for row_index in range( 0, len( list_2d ) ):
    for col_index in range( 0, len( list_2d[ row_index ] ) ):
        print( list_2d[ row_index ][ col_index ] )


