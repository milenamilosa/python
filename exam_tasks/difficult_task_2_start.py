# TASK 1 #

def is_valid(queen_positions):
    numbers = "12345678"
    letters = "abcdefgh"
    position_list = []
    li = []
    for i in letters:
        for j in numbers:
            position = i + j
            position_list += [str(position)]
    for k in queen_positions:
        if k not in li and k in position_list:
            li += [k]
            if len(li) == len(queen_positions):
                return True
    if queen_positions == []:
        return True
    return False


# TASK 2 #

def squares_covered(queen_position):
    array = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    rows = "87654321"
    collumns = "abcdefgh"
    row_index = 0
    col_index = 0
    queen = -1
    covered = 1
    
    # finding queen's position
    for i in queen_position:
        if i in collumns:
            col_index = collumns.index(i)
        elif i in rows:
            row_index = rows.index(i)
            
    # finding rows
    for i in range (0, len(array[row_index])):
        array[row_index][i] = covered
        temp = array[row_index][i]
    
    # finding collumns
    for i in range (0, len(array)):
        array[i][col_index] = covered
        temp1 = array[i][col_index]
    
    # finding left-right diagonal
    start_row = row_index-col_index
    start_col = 0
    for i in range (0, len(array)):
        if i == start_row:
            array[start_row][start_col] = covered
            start_row+=1
            start_col+=1
            
    # finding right-left diagonal
    row_start = 0
    col_start = row_index + col_index
    while col_start > len(array[i])-1:
        col_start-=1
        row_start+=1
    for i in range(0, len(array)-1):
        array[row_start][col_start] = covered
        row_start += 1
        col_start-=1
    
    # placing queen 
    array[row_index][col_index] = queen
    
    # printing nicely
    for i in array:
        print(i)
    print("\n")
    
    return array


            
### DON'T CHANGE ANYTHING BELOW THIS LINE ###

def test():
    
    score = 0
    
    # TEST 1 #
    t1_1 = is_valid([])
    t1_2 = is_valid(["b4", "c6"])
    t1_3 = is_valid(["b4", "c6", "b4"])
    t1_4 = is_valid(["4b", "c6"])
    t1_5 = is_valid(["4b", "j9"])
    print("# TEST 1 #")
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    print(t1_5)
    if t1_1 and t1_2 and not t1_3 and not t1_4 and not t1_5:
        score += 3
        print( "Test 1 success" )
    print("--------------------")
    
    
    # TEST 2 #
    t2_1 = squares_covered("d3")
    t2_2 = squares_covered("a1")
    print("# TEST 2 #")
    print(t2_1)
    print(t2_2)
    
    answer2_1 = [[0, 0, 0, 1, 0, 0, 0, 0], #rank 8
                 [0, 0, 0, 1, 0, 0, 0, 1], #rank 7
                 [1, 0, 0, 1, 0, 0, 1, 0], #rank 6
                 [0, 1, 0, 1, 0, 1, 0, 0], #rank 5
                 [0, 0, 1, 1, 1, 0, 0, 0], #rank 4
                 [1, 1, 1,-1, 1, 1, 1, 1], #rank 3
                 [0, 0, 1, 1, 1, 0, 0, 0], #rank 2
                 [0, 1, 0, 1, 0, 1, 0, 0]] #rank 1
            #file A  B  C  D  E  F  G  H
    
    answer2_2 = [[1, 0, 0, 0, 0, 0, 0, 1], #rank 8
                 [1, 0, 0, 0, 0, 0, 1, 0], #rank 7
                 [1, 0, 0, 0, 0, 1, 0, 0], #rank 6
                 [1, 0, 0, 0, 1, 0, 0, 0], #rank 5
                 [1, 0, 0, 1, 0, 0, 0, 0], #rank 4
                 [1, 0, 1, 0, 0, 0, 0, 0], #rank 3
                 [1, 1, 0, 0, 0, 0, 0, 0], #rank 2
                [-1, 1, 1, 1, 1, 1, 1, 1]] #rank 1
            #file A  B  C  D  E  F  G  H
    
    if t2_1 == answer2_1 and t2_2 == answer2_2:
        score += 3
        print( "Test 2 success" )
    print("--------------------")
        
    print("Final score:", score)    
    
if __name__ == "__main__":
    test() 