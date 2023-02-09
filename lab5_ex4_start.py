### function definition ###

def gcd( num1, num2 ):
    if num1 > num2:
        n = num2
        while n > 0:
            if num1 % n == 0 and num2 % n == 0:
                return n
            else:
                n-=1
    elif num2 > num1:
        n = num1
        while n > 0:
            if num1 % n == 0 and num2 % n == 0:
                return n
            else:
                n-=1
    else:
        return 0



### main program ###
def test():
    final_grade = 0
    
    # TEST 1 #
    print( "# TEST #" )
    t1_1 = gcd( 8, 12 )
    t1_2 = gcd( 30, 20 )
    t1_3 = gcd( 124000, 86500 )
    t1_4 = gcd( 0, 0 )
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    
    if t1_1 == 4 and t1_2 == 10 and t1_3 == 500 and t1_4 == 0:
        final_grade = final_grade + 1
        print( "TEST SUCCESS" )
    else:
        print( "TEST FAILED" )
    print( "--------------------" )
    
    print("Your score for this exercise is ", final_grade, "/1.")
    
    
if __name__ == "__main__":    
    test()