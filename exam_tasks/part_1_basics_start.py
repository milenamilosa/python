#count the number of elements in a list
def count_elements( some_list ):
    count = 0
    for i in some_list:
        count += 1
    return count


#check if a value is legal (i.e. between 0 and 1)
def correct_percentage( percentage ):
    if percentage >= 0 and percentage <= 1:
        return "correct"
    return "incorrect"
    

#check if this is a legal percentage distribution (in other words, whether the sum of all values is equal to 1)
def probability_distribution( some_list ):
    temp = 0
    for i in some_list:
        temp += i
        if temp == 1:
            return True
    return False


#check if an element is in a list
def find_element( some_list, percentage ):
    for i in some_list:
        if i == percentage:
            return True
    return False


#read a file and return the average of its contents
def read_from_file( filename ):
    file = open(filename)
    sum_of = 0
    counter = 0
    for data in file:
        sum_of += float(data)
        counter += 1
    average = sum_of / counter
    
    file.close()
    return average


#return all values in a list above a certain threshold, sorted small to large
def sorted_above( some_list, threshold ):
    new_list = []
    for i in some_list:
        if i > threshold:
            new_list += [i]
    sorted_list = sorted(new_list)
    return sorted_list


#create a list that contains all elements of an original list multiplied by 100, in inverse order (back to front)
def invert_list( some_list ):
    new_list = []
    sorted_new = some_list[::-1]
    for i in sorted_new:
        i = i*100
        new_list += [int(i)]
    return new_list


#store all non-zero values from a matrix in a 1D list
def matrix_to_list( matrix ):
    new_list = []
    for row in matrix:
        for element in row:
            if element != 0:
                new_list += [element]
    return new_list


### DON'T CHANGE ANYTHING BELOW THIS LINE ###

def test():
    
    score = 0
    
    percentage_distribution = [ 0.12, 0.06, 0.14, 0.33, 0.27, 0.01, 0.07 ]
    
    # TEST 1 #
    print("# TEST 1 : count_elements() #")
    t1_1 = count_elements( percentage_distribution )
    t1_2 = count_elements( [] )
    print( t1_1 )
    print( t1_2 )

    if t1_1 == 7 and t1_2 == 0:
        score += 0.5
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print("--------------------")


    # TEST 2 #
    print("# TEST 2 : correct_percentage() #")
    t2_1 = correct_percentage( -0.1 )
    t2_2 = correct_percentage( 1.2 )
    t2_3 = correct_percentage( 0.67 )
    print( t2_1 )
    print( t2_2 )
    print( t2_3 )
    if t2_1 == "incorrect" and t2_2 == "incorrect" and t2_3 == "correct":
        score += 0.5
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2  FAILED" )
    print("--------------------")
    
    # TEST 3 #
    print("# TEST 3 : probability_distribution() #")
    t3_1 = probability_distribution( percentage_distribution )
    t3_2 = probability_distribution( [ 0.5, 0.6 ] )
    t3_3 = probability_distribution( [] )
    print( t3_1 )
    print( t3_2 )
    print( t3_3 )   
    if t3_1 == True and t3_2 == False and t3_3 == False:
        score += 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print("--------------------")
    
    # TEST 4 #
    print("# TEST 4 : find_element() #")
    t4_1 = find_element( percentage_distribution, 0.27 )
    t4_2 = find_element( percentage_distribution, 0.28 )
    t4_3 = find_element( [], 0.27 )
    print( t4_1 )
    print( t4_2 )
    print( t4_3 )
    
    if t4_1 == True and t4_2 == False and t4_3 == False:
        score += 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print("--------------------")
    
    # TEST 5 #
    print("# TEST 5 : read_from_file() #")
    t5_1 = read_from_file( "percentages.txt" )
    print( t5_1 )
    if abs(t5_1 - 0.14286) <= 0.01:
        score += 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print("--------------------")
    
    # TEST 6 #
    print("# TEST 6 : sorted_above() #")
    t6_1 = sorted_above( percentage_distribution, 0.1 )
    t6_2 = sorted_above( percentage_distribution, 0.3 )
    t6_3 = sorted_above( percentage_distribution, 0.4 )
    print( t6_1 )
    print( t6_2 )
    print( t6_3 )    
    if t6_1 == [ 0.12, 0.14, 0.27, 0.33 ] and t6_2 == [ 0.33 ] and t6_3 == []:
        score += 1
        print( "TEST 6 SUCCESS" )
    else:
        print( "TEST 6 FAILED" )
    print("--------------------")
    
    # TEST 7 #
    print("# TEST 7 : invert_list() #")
    t7_1 = invert_list( percentage_distribution )
    print( t7_1 )
    if t7_1 == [ 7, 1, 27, 33, 14, 6, 12 ]:
        score += 1.5
        print( "TEST 7 SUCCESS" )
    else:
        print( "TEST 7 FAILED" )
    print("--------------------")
    
    # TEST 8 #
    print("# TEST 8 : matrix_to_list() #")
    t8_1 = matrix_to_list( [[ 0.2, 0, 0.2 ], [ 0.2, 0.02, 0.11 ], [ 0.24, 0, 0 ]] )
    t8_2 = matrix_to_list( [[ 0, 0 ], [ 0, 0 ]] )
    print( t8_1 )
    print( t8_2 ) 
    if t8_1 == [ 0.2, 0.2, 0.2, 0.02, 0.11, 0.24 ] and t8_2 == []:
        score += 1.5
        print( "TEST 8 SUCCESS" )
    else:
        print( "TEST 8 FAILED" )
    print("--------------------")
    
    print( "Final score:", score)

if __name__ == "__main__":
    test()