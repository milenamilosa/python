# function definitions

def multiples( to ):
    list = []
    my_list = []
    start = 1
    n = 1
    for row in range (start, to+1):
        n = 1
        list = []
        for element in range (n, 11):
            result = start * n
            list = list + [result]
            n+=1
            
        start += 1
        my_list = my_list + [list]
    return my_list


#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    final_grade = 0
    
    # TEST #
    print( "# TEST #" )
    t_1 = multiples(0)
    t_2 = multiples(7)
    print(t_1)
    print(t_2)
    
    if t_1 == [] and t_2 == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]]:
        final_grade = final_grade + 1
        print( "TEST SUCCESS" )
    else:
        print( "TEST FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", final_grade, "/1.")
    

if __name__ == "__main__":
    test()
