# Function Definition
# returns a cuteness-percentage (=float between 0 and 1) based on what pet (=string) you have 
def how_cute_is_my_pet(pet):
    if pet == "goldfish":
        cuteness = 0.20
    elif pet == "dog":
        cuteness = 0.85
    elif pet == "cat":
        cuteness = 0.99
    elif pet == "mole rat":
        cuteness = 0
    else:
        cuteness = 0   
    return cuteness
    

# Test Code: Do not change anything below the line
#__________________________________________________
def test():
    score = 0

    goldfish_test = how_cute_is_my_pet("goldfish")
    if goldfish_test == 0.20:
        score = score + 1

    dog_test = how_cute_is_my_pet("dog")
    if dog_test == 0.85:
        score = score + 1

    cat_test = how_cute_is_my_pet("cat")
    if cat_test == 0.99:
        score = score + 1
        
    mole_rat_test = how_cute_is_my_pet("mole rat")
    if mole_rat_test == 0:
        score = score + 1
        
    print("You scored " + str(score) + "/4 for this exercise.")
    
    
if __name__ == "__main__":    
    test()
