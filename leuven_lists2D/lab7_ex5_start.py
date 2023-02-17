### function definitions ###

def count_starting_with(wordlist, letter):
    count = 0
    for word in wordlist:
        if word[0] == letter:
            count += 1
    return count

def count_total_characters(wordlist):
    count = 0
    for word in wordlist:
        for letter in word:
            count += 1
    return count

def do_letters_occur(wordlist, letters):
    for character in letters:
        for word in wordlist:
            for letter in word:
                if letter == character:
                    return True
    return False

def number_of_consonants(wordlist):
    count = 0
    for word in wordlist:
        for letter in word:
            if letter == "o" or letter == "a" or letter == "e" or letter == "u" or letter == "i":
                count += 0
            else:
                count += 1
    return count

def is_a_word_snake(wordlist):
    n = 0
    for word in wordlist:
        first_letter = wordlist[n][len(word)-1]
        second_letter = wordlist[n+1][0]
        if first_letter == second_letter:
            n+=1
    if n == len(wordlist)-1:
        return True
        
    return False
        


#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    final_grade = 0
    
    words1 = ["data", "amount", "tomato", "onwards", "snake", "editor", "revolving", "genious", "snake", "elongated", "density"]
    words2 = ["this", "is", "just", "a", "random", "bunch", "of", "words", "potato"]
    
    # TEST 1 #
    print( "# TEST 1 : count_starting_with() #" )
    t1_1 = count_starting_with( words1, "a" )
    t1_2 = count_starting_with( words1, "e" )
    t1_3 = count_starting_with( [], "a" )
    print(t1_1)
    print(t1_2)
    print(t1_3)
        
    if t1_1 == 1 and t1_2 == 2 and t1_3 == 0:
        final_grade = final_grade + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    # TEST 2 #
    print( "# TEST 2 : count_total_characters() #" )            
    t2_1 = count_total_characters( words1 )
    t2_2 = count_total_characters( words2 )
    t2_3 = count_total_characters( [] )
    print(t2_1)
    print(t2_2)
    print(t2_3)
        
    if t2_1 == 71 and t2_2 == 35 and t2_3 == 0:
        final_grade = final_grade + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    # TEST 3 #
    print( "# TEST 3 : do_letters_occur() #" )
    t3_1 = do_letters_occur( words2, ["x","y","p"] )
    t3_2 = do_letters_occur( words2, ["x","y","z"] )
    t3_3 = do_letters_occur( [], ["a", "b", "c"] )
    print(t3_1)
    print(t3_2)
    print(t3_3)
    
    if t3_1 and not t3_2 and not t3_3:
        final_grade = final_grade + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    
    # TEST 4 #
    print( "# TEST 4 : number_of_consonants() #" )
    t4_1 = number_of_consonants( words1 )
    t4_2 = number_of_consonants( words2 )
    t4_3 = number_of_consonants( [] )
    print(t4_1)
    print(t4_2)
    print(t4_3)    
    
    if t4_1 == 41 and t4_2 == 23 and t4_3 == 0:
        final_grade = final_grade + 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print( "--------------------" )
    
    # TEST 5 #
    print( "# TEST 5 : is_a_word_snake() #" )
    t5_1 = is_a_word_snake( words1 )
    t5_2 = is_a_word_snake( words2 )
    print(t5_1)
    print(t5_2)

    if t5_1 and not t5_2:
        final_grade = final_grade + 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print( "--------------------" )
    
    print("Your score for this exercise is ", final_grade, "/5.")       
        

if __name__ == "__main__":    
    test()
