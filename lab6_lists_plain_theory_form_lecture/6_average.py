#average without list
def calc_average_nolist( num1, num2, num3 ):
    result = (num1 + num2 + num3) / 3
    return result

print( calc_average_nolist( 8, 10, 12 ) )


# average with list
def calc_average_list( num_list ):
    result = 0
    for element in num_list:
        result = result + element
    return result / len( num_list )

my_list = [ 8, 10, 12, -76, 144, 10 ]
print( calc_average_list( [ 8, 10, 12 ] ) )
print( calc_average_list( my_list ) )