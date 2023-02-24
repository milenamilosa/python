### FUNCTION DEFINITIONS ###
# you may write extra helper functions HERE if you need them

#0
def print_names( pokemon ):   # pass the (2D) list of all pokemon as parameter
    for pkmn in pokemon:    # iterate over all individual pokemon (one pkmn is one 12-element list)
        print(pkmn[NUMBER], pkmn[NAME])   # print only the correct column/element: names are in the second column,
                            # or thus the column with index 1 (see MAIN below: NAME = 1)


#1
def find_by_name( pokemon, name ):
    for pkmn in pokemon:
        if name in pkmn:
            result = pkmn
            break
        else:
            result = []
    return result


#2
def find_field_by_name( pokemon, name, field ):
    if find_by_name( pokemon, name ) != []:
        line = find_by_name( pokemon, name )
    
        if field >= 0 and field <= 11:
            searched_field = line[field]
        else:
            return None
        return searched_field


#3
# find 1 pokemon name based on stats (columns between 4 and 10 included)
# 1. check if stat is in (4, 10)
# 2. make a list of all elements in this column: pokemon[pkmn][stat], pkmn+=1..
# 3. sort list
# 4. save len(sorted_list) to a parameter
# 5. find row where this parameter is from
    
def find_best( pokemon, stat ):
    col = 0
    temp_list = []
    if stat >= 4 and stat <= 10:
        col = stat
    elif stat < 4:
        col = 4
    elif stat > 10:
        col = 10
    
    for pkmn in range (0, len(pokemon)):
        temp_list = temp_list + [pokemon[pkmn][col]]
        
    sorted_list = sorted(temp_list)
    best_stat = sorted_list[len(sorted_list)-1]
    
    for pkmn in range (0, len(pokemon)):
        if best_stat == pokemon[pkmn][col]:
            name_pokemon = pokemon[pkmn][NAME]
            break
    
    return name_pokemon


#4
def hall_of_fame( pokemon ):
    list_of_stats = ["NUMBER", "NAME", "TYPE1", "TYPE2", "Total", "HP", "ATT", "DEF", "SP.ATT", "SP.DEF", "SPEED", "LEGENDARY"]
    list_fame = []
    for stat in range (4, (len(pokemon[0])-1)):
        temp = []
        name = find_best( pokemon, stat )
        
        string_stat = str(list_of_stats[stat])
        temp += [string_stat] + [name]
        list_fame = list_fame + [temp]
            
    return list_fame
    
def stat_to_string( stat ):
    return ""

def print_hall_of_fame( pokemon ):
    print()
        
        
#5        
def calc_damage( pokemon, attacker, defender ):
    if find_by_name( pokemon, attacker ) != []  and find_by_name( pokemon, defender ) != []:
        damage = 2 * find_field_by_name( pokemon, attacker, ATTACK ) - find_field_by_name( pokemon, defender, DEFENSE )
        if damage < 1:
            damage = 1
        return damage
    
    return -1


#6
def is_super_effective( pokemon, attacker, defender ):
    if find_by_name( pokemon, attacker ) != []  and find_by_name( pokemon, defender ) != []:
        attack = find_field_by_name( pokemon, attacker, TYPE1 )
        defend = find_field_by_name( pokemon, defender, TYPE1 )
        if attack == "Grass" and defend == "Water" or attack == "Water" and defend == "Fire" or attack == "Fire" and defend == "Grass":
            return True
        
    return False


#7
def is_special_attacker( pokemon, name ):
    if find_by_name( pokemon, name ) != []:
        if find_field_by_name( pokemon, name, SPECIAL_ATTACK ) > find_field_by_name( pokemon, name, ATTACK ):
            return True
    return False


#8
def complex_damage( pokemon, attacker, defender ):
    if find_by_name( pokemon, attacker ) != []  and find_by_name( pokemon, defender ) != []:
        if is_special_attacker( pokemon, attacker ) == True:
            damage = 2 * find_field_by_name( pokemon, attacker, SPECIAL_ATTACK ) - find_field_by_name( pokemon, defender, SPECIAL_DEFENSE )
        else:
            damage = calc_damage( pokemon, attacker, defender )
        
        if is_super_effective( pokemon, attacker, defender ) == True:
            damage = damage * 2
        return damage
        
    return -1
        


#_______________________________________________________________
# MAIN
# DO NOT CHANGE ANYTHING BELOW THE LINE


# a pokémon is defined by a list of 12 values
# look at 'print_names' to see how to use the following variables
# as a way to access the correct column in a readable way.
NUMBER = 0
NAME = 1
TYPE1 = 2
TYPE2 = 3
TOTAL = 4
HITPOINTS = 5
ATTACK = 6
DEFENSE = 7
SPECIAL_ATTACK = 8
SPECIAL_DEFENSE = 9
SPEED = 10
LEGENDARY = 11



def test():
   
    pokemon = [ 
    #   nr.   name           type1      type2      total  HP   ATK  DEF  SP.ATK  SP.DEF  SPEED  Legendary?
        [1,   "Bulbasaur",   "Grass",   "Poison",  318,   45,  49,  49,  65,     65,     45,    False],
        [2,   "Ivysaur",     "Grass",   "Poison",  405,   60,  62,  63,  80,     80,     60,    False],
        [3,   "Venusaur",    "Grass",   "Poison",  525,   80,  82,  83,  100,    100,    80,    False],
        [4,   "Charmander",  "Fire",    "",        309,   39,  52,  43,  60,     50,     65,    False],
        [5,   "Charmeleon",  "Fire",    "",        405,   58,  64,  58,  80,     65,     80,    False],
        [6,   "Charizard",   "Fire",    "Flying",  534,   78,  84,  78,  109,    85,     100,   False],
        [7,   "Squirtle",    "Water",   "",        314,   44,  48,  65,  50,     64,     43,    False],
        [8,   "Wartortle",   "Water",   "",        405,   59,  63,  80,  65,     80,     58,    False],
        [9,   "Blastoise",   "Water",   "",        530,   79,  83,  100, 85,     105,    78,    False],
        [10,  "Caterpie",    "Bug",     "",        195,   45,  30,  35,  20,     20,     45,    True]
        ]
    
    score = 0
    
    print( "# TEST 0 : print_names() #" )
    print_names(pokemon)
    print( "--------------------" )
    
    
    print( "# TEST 1 : find_by_name() #" )
    t1_1 = find_by_name(pokemon, "Charmander")
    t1_2 = find_by_name(pokemon, "Shartmander")
    print(t1_1)
    print(t1_2)

    if t1_1 == [4,"Charmander","Fire","",309,39,52,43,60,50,65,False] and t1_2 == []:
        score = score + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 2 : find_field_by_name() #" )
    t2_1 = find_field_by_name(pokemon, "Charmeleon", TOTAL)
    t2_2 = find_field_by_name(pokemon, "Caterpie", LEGENDARY)
    t2_3 = find_field_by_name(pokemon, "Wartortle", NAME)
    t2_4 = find_field_by_name(pokemon, "Fartfetch'd", HITPOINTS)
    t2_5 = find_field_by_name(pokemon, "Caterpie", 123)
    print(t2_1)
    print(t2_2)
    print(t2_3)
    print(t2_4)
    print(t2_5)

    if t2_1 == 405 and t2_2 == True and t2_3 == "Wartortle" and t2_4 == None and t2_5 == None:
        score = score + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    

    print( "# TEST 3 : find_best() #" )
    t3_1 = find_best(pokemon, ATTACK)
    t3_2 = find_best(pokemon, SPECIAL_DEFENSE)
    t3_3 = find_best(pokemon, 2) # 2 -> 4 -> TOTAL
    t3_4 = find_best(pokemon, 123) # 123 -> 10 -> SPEED
    print(t3_1)
    print(t3_2)
    print(t3_3)
    print(t3_4)

    if t3_1 == "Charizard" and t3_2 == "Blastoise" and t3_3 == "Charizard" and t3_4 == "Charizard":
        score = score + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    

    print( "# TEST 4 : hall_of_fame() #" )
    t4_1 = hall_of_fame( pokemon )
    print(t4_1)

    if t4_1 == [['Total', 'Charizard'], ['HP', 'Venusaur'], ['ATT', 'Charizard'], ['DEF', 'Blastoise'], ['SP.ATT', 'Charizard'], ['SP.DEF', 'Blastoise'], ['SPEED', 'Charizard']]:
        score = score + 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 4 extra : print_hall_of_fame() #" )
    print_hall_of_fame( pokemon )
    print( "--------------------" )
    

    print( "# TEST 5 : calc_damage() #" )
    t5_1 = calc_damage(pokemon, "Blastoise", "Charizard")
    t5_2 = calc_damage(pokemon, "Charizard", "Blastoise")
    t5_3 = calc_damage(pokemon, "Caterpie", "Blastoise")
    t5_4 = calc_damage(pokemon, "Blastoise", "Hitmonchucknorris")
    t5_5 = calc_damage(pokemon, "Hitmonchucknorris", "Blastoise")
    print(t5_1)
    print(t5_2)
    print(t5_3)
    print(t5_4)
    print(t5_5)

    if t5_1 == 88 and t5_2 == 68 and t5_3 == 1 and t5_4 == -1 and t5_5 == -1:
        score = score + 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 6 : is_super_effective() #" )
    t6_1 = is_super_effective(pokemon, "Blastoise", "Charizard")
    t6_2 = is_super_effective(pokemon, "Charizard", "Caterpie")
    t6_3 = is_super_effective(pokemon, "Blastoise", "Parasectamol")
    t6_4 = is_super_effective(pokemon, "Parasectamol", "Blastoise")
    print(t6_1)
    print(t6_2)

    if t6_1 == True and t6_2 == False and t6_3 == False and t6_4 == False:
        score = score + 1
        print( "TEST 6 SUCCESS" )
    else:
        print( "TEST 6 FAILED" )
    print( "--------------------" )
    

    print( "# TEST 7 : is_special_attacker() #" )
    t7_1 = is_special_attacker(pokemon, "Charizard")
    t7_2 = is_special_attacker(pokemon, "Caterpie")
    t7_3 = is_special_attacker(pokemon, "Pikgesundheit")
    print(t7_1)
    print(t7_2)
    print(t7_3)

    if t7_1 == True and t7_2 == False and t7_3 == False:
        score = score + 1
        print( "TEST 7 SUCCESS" )
    else:
        print( "TEST 7 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 8 : complex_damage() #" )
    t8_1 = complex_damage(pokemon, "Caterpie", "Caterpie")
    t8_2 = complex_damage(pokemon, "Caterpie", "Charizard")
    t8_3 = complex_damage(pokemon, "Squirtle", "Caterpie")
    t8_4 = complex_damage(pokemon, "Squirtle", "Charizard")
    t8_5 = complex_damage(pokemon, "Squirtle", "Starthey/them")
    t8_6 = complex_damage(pokemon, "Starthey/them", "Squirtle")
    print(t8_1)
    print(t8_2)
    print(t8_3)
    print(t8_4)
    print(t8_5)
    print(t8_6)

    if t8_1 == 25 and t8_2 == 1 and t8_3 == 80 and t8_4 == 30 and t8_5 == -1 and t8_6 == -1:
        score = score + 1
        print( "TEST 8 SUCCESS" )
    else:
        print( "TEST 8 FAILED" )
    print( "--------------------" )
        
        
    print("Total score : ", score, "/8")

if __name__ == "__main__":
    test()