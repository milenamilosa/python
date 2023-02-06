# FUNCTION DEFINITION
def buy_cocktail(is_birthday):
    price = 8.50
    if is_birthday == True:
        new_price = 6.50
        return new_price
    else:
        return price



# TEST CODE: DO NOT CHANGE ANYTHING BELOW THE LINE
#__________________________________________________
def test():
    print("Now testing: buy_cocktail...")
    score = 0 # the variable score is set to zero, it will increment with every succesfull test

    print("Test 1: it is not your birthday")
    non_birthday_price = buy_cocktail(False)
    if non_birthday_price == 8.50:
        score = score + 1 # if your code returns the correct value, you get a higher score
        print("OK")
    else:
        print("FAILED")

    print("Test 2: it is your birthday")
    birthday_price = buy_cocktail(True)
    if birthday_price == 6.50:
        score = score + 1 
        print("OK")
    else:
        print("FAILED")
        
    print("Your score for this exercise is " + str(score) + "/2")


if __name__ == "__main__":    
    test()
        