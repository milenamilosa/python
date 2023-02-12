my_list = [ 8, 10, 12, -76, 144, 10 ]

#Iterates using a simple for loop. This accesses each element of the list one by one, front to back
for element in my_list:
    print( element )

#Iterates using an index variable. Since we can access the current value of the index, we have more freedom in how we iterate here
for index in range( 0, len(my_list) ):
    if index % 2 == 0:
        print( my_list[ index ] )

#Iterates using a while loop. We have even more freedom here, since we control how the index evolves
index = len( my_list ) - 1
while index >= 0:
    print( my_list[ index ] )
    index = index - 1