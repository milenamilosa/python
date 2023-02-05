import random # needed for heal function, see lab text

### Function Definitions ###
def attack_is_valid(attack):
    #your code here
    return False


def defense_is_valid(attack, defense):
    #your code here
    return False


def calc_damage(attack, defense, is_critical):
    #your code here
    return -1


def calc_hitpoints(damage, current_hitpoints):
    #your code here
    return ""


def heal(current_hitpoints, max_hitpoints):
    #your code here
    return -1


### main program ###
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    score = 0

    attack_pikachu = 25
    defense_pikachu = 5
    attack_caterpie = 10
    defense_caterpie = 10
    attack_charizard = 0
    defense_charizard = 50
    attack_mewtwo = -9

    # TEST 1 #
    print( "# TEST 1: attack_is_valid() #" )
    t1_1 = attack_is_valid(attack_pikachu)
    t1_2 = attack_is_valid(attack_caterpie)
    t1_3 = attack_is_valid(attack_mewtwo)
    t1_4 = attack_is_valid(attack_charizard)
    print( t1_1 )
    print( t1_2 )
    print( t1_3 )
    print( t1_4 )
    
    if t1_1 == True and t1_2 == True and t1_3 == False and t1_4 == False:
        score = score + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )

    # TEST 2 #
    print( "# TEST 2: defense_is_valid() #" )
    t2_1 = defense_is_valid(attack_pikachu, defense_pikachu)
    t2_2 = defense_is_valid(attack_caterpie, defense_caterpie) 
    t2_3 = defense_is_valid(attack_charizard, defense_charizard)
    print( t2_1 )
    print( t2_2 )
    print( t2_3 )

    if t2_1 == True and t2_2 == True and t2_3 == False:
        score = score + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
      
    # TEST 3 #  
    print( "# TEST 3: calc_damage() #" )
    t3_1 = calc_damage(attack_caterpie, defense_pikachu, False)
    t3_2 = calc_damage(attack_caterpie, defense_charizard, False)
    t3_3 = calc_damage(attack_pikachu, defense_caterpie, True)
    print( t3_1 )
    print( t3_2 )
    print( t3_3 )
    
    if t3_1 == 5 and t3_2 == 1 and t3_3 == 30:
        score = score + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )

    # TEST 4 #
    print( "# TEST 4: calc_hitpoints() #" )
    t4_1 = calc_hitpoints(20, 10)
    t4_2 = calc_hitpoints(18, 18)
    t4_3 = calc_hitpoints(9, 11)
    t4_4 = calc_hitpoints(16, 36)
    print( t4_1 )
    print( t4_2 )
    print( t4_3 )
    print( t4_4 )
    
    if t4_1 == "Target has fainted" and t4_2 == "Target has fainted" and t4_3 == "Target has 2 hitpoints left" and t4_4 == "Target has 20 hitpoints left":
        score = score + 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print( "--------------------" )

    # TEST 5 #
    print( "# TEST 5: heal() #" )
    t5_1 = heal(18, 18)
    t5_2 = heal(10, 20)
    print( t5_1 )
    print( t5_2 )
    
    if t5_1 == 0 and t5_2 > 0 and t5_2 <= 10:  #it's hard to test for randomness. Here, we're only checking if the resulting value lies between the two extremes
        score = score + 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print( "--------------------" )


    print("Your score for this exercise is ", score, "/5.")
    
    
if __name__ == "__main__":    
    test()
