### FUNCTION DEFINITIONS ###

def supermarket(weekday, bought_alcohol):
    score = 0
    if weekday == "Monday":
        if bought_alcohol == True:
            return 80
        else:
            return 40
    elif weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or weekday == "Friday":
        if bought_alcohol == True:
            return 20
        else:
            return 10


def buy_textbooks(willingness_to_pay, acco_card):
    score = 0
    if willingness_to_pay == 0:
        if acco_card == True or acco_card == False:
            return 0
    if willingness_to_pay == 1:
        if acco_card == True:
            return 200
        else:
            return 200
    if willingness_to_pay == 2:
        if acco_card == True:
            return 390
        else:
            return 400
    if willingness_to_pay == 3:
        if acco_card == True:
            return 660
        else:
            return 700


def calc_fine(alcohol_pct):
    count = 0
    if alcohol_pct > 0 and alcohol_pct < 0.5:
        return 0
    elif alcohol_pct >= 0.5 and alcohol_pct<= 0.8:
        return 50
    elif alcohol_pct >0.8 and alcohol_pct < 1.5:
        this_case = abs(alcohol_pct-100)
        return this_case
    elif alcohol_pct == 1.5:
        return 150
    elif alcohol_pct >1.5:
        return 250


### main program ###
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    score = 0

    # TEST 1 #
    print( "# TEST 1 : supermarket() #" )
    t1_1 = supermarket('Monday', False)
    t1_2 = supermarket('Monday', True)
    t1_3 = supermarket('Tuesday', False)
    t1_4 = supermarket('Friday', True)
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    
    if t1_1 == 40 and t1_2 == 80 and t1_3 == 10 and t1_4 == 20:
        score = score + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
        
    # TEST 2 #
    print( "# TEST 2: buy_textbooks() #" )
    t2_1 = buy_textbooks(0, False)
    t2_2 = buy_textbooks(0, True)
    t2_3 = buy_textbooks(1, False)
    t2_4 = buy_textbooks(1, True)
    t2_5 = buy_textbooks(2, False)
    t2_6 = buy_textbooks(3, False)
    t2_7 = buy_textbooks(2, True)
    t2_8 = buy_textbooks(3, True)
    print( t2_1 )
    print( t2_2 )
    print( t2_3 )
    print( t2_4 )
    print( t2_5 )
    print( t2_6 )
    print( t2_7 )
    print( t2_8 )
    
    if t2_1 == 0 and t2_2 == 0 and t2_3 == 200 and t2_4 == 200 and t2_5 == 400 and t2_6 == 700 and t2_7 == 390 and t2_8 == 660:
        score = score + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )

    # TEST 3 #
    print( "# TEST 3: calc_fine() #" )
    t3_1 = calc_fine(0.4)
    t3_2 = calc_fine(0.5)
    t3_3 = calc_fine(0.8)
    t3_4 = calc_fine(1.5)
    t3_5 = calc_fine(1.15)
    t3_6 = calc_fine(9.9)
    print( t3_1 )
    print( t3_2 )
    print( t3_3 )
    print( t3_4 )
    print( t3_5 )
    print( t3_6 )
    print (abs(t3_5-100))
    #note that we don't check for an exact match for t3_5, but for "close enough" to the expected value of 100. This is because floating point arithmetic in a computer is inherently imprecise.
    if t3_1 == 0 and t3_2 == 50 and t3_3 == 50 and t3_4 == 150 and abs(t3_5-100) < 0.0001 and t3_6 == 250:
        score = score + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )

    print("Your score for this exercise is ", score, "/3.")


if __name__ == "__main__":    
    test()
