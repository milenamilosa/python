my_list = [ 8, 10, 12, -76, 144, 10 ]

my_list = my_list + [6]
print( my_list )

# my_list = my_list + 6 # will cause an error


number = 6

# if you turn on these three lines and line 3-4, 6 will be added twice to my_list
# my_list = my_list + [number]
# print( my_list )

# my_list = my_list + number # will cause an error


# if you turn on these two lines and line 3-4 or 12-13, 6 will be added to the front and back of the list
# my_list = [number] + my_list
# print( my_list )