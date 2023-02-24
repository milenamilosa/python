# FUNCTION DEFINITIONS

plants = ["Aztekium", "Oak", "Cereus", "Sunflower", "Sphagnum", "Willow", "Melocactus", "Banana", "Haircap", "Rose", "Orchid"]
labels = ["c", "t", "c", "f", "m", "t", "c", "t", "m", "f", "f"]

#1
def find_plants_with_label( plant_list, label_list, searched_label ):#
    searched_label_indices = []
    searched_plants = []
    index = [i for i, x in enumerate(label_list) if x == searched_label]
    searched_label_indices = searched_label_indices + index
    for j in searched_label_indices:
        searched_plant = plant_list[j]
        searched_plants = searched_plants + [searched_plant]
        
    return searched_plants

#2
def calc_tree_price( tree_name ):
    price = len(tree_name) * 10
    return price

#3
def calc_cactus_price( cactus_name ):
    if starts_with_vowel( cactus_name ) == True:
        price = len(cactus_name) * 20
    else:
        price = len(cactus_name) * 10
    return price

def starts_with_vowel( cactus_name ):
    if cactus_name[0] == 'A' or cactus_name[0] == 'E' or cactus_name[0] == 'U' or cactus_name[0] == 'I' or cactus_name[0] == 'O':
        starts_with_vowel = True
    else:
        starts_with_vowel = False
    return starts_with_vowel

#4
def calc_flower_price( flower_name ):
    if flower_name[0] == 'A' or flower_name[0] == 'E' or flower_name[0] == 'U' or flower_name[0] == 'I' or flower_name[0] == 'O':
        price = len(flower_name) * 20
    else:
        price = len(flower_name) * 10
        
    if price < 50:
        price = 50
    elif price > 100:
        price = 100
        
    return price
    
#5
def calc_price_list( plant_list, label_list ):
    price_list = []
    for plant in plant_list:
        if plant in find_plants_with_label( plant_list, label_list, "c" ):
            price = calc_cactus_price( plant )
        elif plant in find_plants_with_label( plant_list, label_list, "t" ):
            price = calc_tree_price( plant )
        elif plant in find_plants_with_label( plant_list, label_list, "f" ):
            price = calc_flower_price( plant )
        else:
            price = 0
        price_list = price_list + [price] 
            
    return price_list
        


### main program ###
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________

def test():
    score = 0
    
    plants = ["Aztekium", "Oak", "Cereus", "Sunflower", "Sphagnum", "Willow", "Melocactus", "Banana", "Haircap", "Rose", "Orchid"]
    labels = ["c", "t", "c", "f", "m", "t", "c", "t", "m", "f", "f"]

    # TEST 1 #
    print( "# TEST 1 : find_plants_with_label() #" )
    t1_1 = find_plants_with_label( plants, labels, "c" )
    t1_2 = find_plants_with_label( plants, labels, "t" )
    t1_3 = find_plants_with_label( plants, labels, "f" )
    t1_4 = find_plants_with_label( plants, labels, "d" )
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    
    if t1_1 == ["Aztekium", "Cereus", "Melocactus"] and t1_2 == ["Oak", "Willow", "Banana"] and t1_3 == ["Sunflower", "Rose", "Orchid"] and t1_4 == []:
        score = score + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 2 : calc_tree_price() #" )
    t2_1 = calc_tree_price( "Oak" )
    t2_2 = calc_tree_price( "Willow" )
    t2_3 = calc_tree_price( "Banana" )
    print(t2_1)
    print(t2_2)
    print(t2_3)

    if t2_1 == 30 and t2_2 == 60 and t2_3 == 60:
        score = score + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 3 : calc_cactus_price() #" )
    t3_1 = calc_cactus_price( "Aztekium" )
    t3_2 = calc_cactus_price( "Cereus" )
    t3_3 = calc_cactus_price( "Melocactus" )
    print(t3_1)
    print(t3_2)
    print(t3_3)

    if t3_1 == 160 and t3_2 == 60 and t3_3 == 100:
        score = score + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 4 : calc_flower_price() #" )
    t4_1 = calc_flower_price( "Sunflower" )
    t4_2 = calc_flower_price( "Rose" )
    t4_3 = calc_flower_price( "Orchid" )
    print(t4_1)
    print(t4_2)
    print(t4_3)

    if t4_1 == 90 and t4_2 == 50 and t4_3 == 100:
        score = score + 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print( "--------------------" )
    
    
    print( "# TEST 5 : calc_price_list() #" )
    t5_1 = calc_price_list( plants, labels )
    print(t5_1)

    if t5_1 == [160, 30, 60, 90, 0, 60, 100, 60, 0, 50, 100]:
        score = score + 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", score, "/5.")
    


if __name__ == "__main__":    
    test()