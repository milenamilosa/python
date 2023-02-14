### function definition ###

def dimension( matrix ):
    count_rows = 0
    count_cols = 0
    empty_list_check = [[]]
    
    for row in matrix:
        count_rows += 1
    for col in matrix[0]:
        count_cols += 1
    if matrix == empty_list_check:
        return [0,0]

    return [count_rows,count_cols]



def count_non_zero( matrix ):
    count = 0
    for row_index in range( 0, len( matrix ) ):
        for col_index in range( 0, len( matrix[ row_index ] ) ):
            if matrix[ row_index ][col_index] != 0:
                count +=1
    
    return count


def list_positive( matrix ):
    my_list = []
    for row_index in range( 0, len( matrix ) ):
        for col_index in range( 0, len( matrix[ row_index ] ) ):
            if matrix[ row_index ][col_index] > 0:
                my_list = my_list + [matrix[ row_index ][col_index]]
    return my_list



#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    final_grade = 0
    
    m1 = [[0,-1,8],[-7,5,1]]
    m2 = [[-8,0],[-4,4],[1,8]]
    m_empty = [[]]

    # TEST 1 #
    print( "# TEST 1 : dimension() #" )
    t1_1 = dimension(m1)
    t1_2 = dimension(m2)
    t1_3 = dimension(m_empty)
    print(t1_1)
    print(t1_2)
    print(t1_3)
    
    if t1_1 == [2,3] and t1_2 == [3,2] and t1_3 == [0,0]:
        final_grade = final_grade + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    # TEST 2 #
    print( "# TEST 2 : count_non_zero() #" )
    t2_1 = count_non_zero(m1)
    t2_2 = count_non_zero(m2)
    t2_3 = count_non_zero(m_empty)
    print(t2_1)
    print(t2_2)
    print(t2_3)
    
    if t2_1 == 5 and t2_2 == 5 and t2_3 == 0:
        final_grade = final_grade + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    # TEST 3 #
    print( "# TEST 3 : list_positive() #" )
    t3_1 = list_positive(m1)
    t3_2 = list_positive(m2)
    t3_3 = list_positive(m_empty)
    print(t3_1)
    print(t3_2)
    print(t3_3)
    
    if t3_1 == [8,5,1] and t3_2 == [4,1,8] and t3_3 == []:
        final_grade = final_grade + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    
    print("Your score for this exercise is ", final_grade, "/3.")
    

if __name__ == "__main__":
    test()
