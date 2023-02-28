import random
import time


# Exercise 1
def show_correct_code(correct_code):
    ''' Prints the correct code, given as a parameter – correct_code (string)
    '''
    print(correct_code)


# Exercise 2
def show_win_message(code_attempts):
    '''Prints a message stating that the player has won and the number of tries it took. The
    code_attempts parameter is a list that contains an element for each attempt it took to find the
    code.'''
    attempts = str(len(code_attempts))
    if attempts == "1":
        writing = "try"
    else:
        writing = "tries"
    output = "Well done! You've cracked the code in " + attempts + " " + writing + ". Keep going! The game gets more challenging with a higher score."
    
    print(output)


# Exercise 3a
def to_string(attempt):
    player_code = attempt[0]
    correct_digits = str(attempt[1])
    dif_place_digits = str(attempt[2])
    output = player_code + " - Correct: " + correct_digits + " / Wrong position: " +  dif_place_digits
        
    return output


# Exercise 3b
def show_all_attempts(code_attempts):
    for i in code_attempts:
        output = to_string(i)
        print(output)


# Exercise 4
def has_attempts_remaining(code_attempts, max_attempts):
    if len(code_attempts) < max_attempts:
        return True
    return False


# Exercise 5
def is_game_won(code_attempts):
    if code_attempts == []:
        return False
    elif code_attempts[len(code_attempts)-1][1] == 4 and code_attempts[len(code_attempts)-1][2] == 0:
        return True
    return False


# Exercise 6a
def any_digit_exceeds_highest_digit_value(number_string, highest_digit):
    for i in number_string:
        if int(i) > highest_digit:
            return True
    return False


# Exercise 6b
def contains_only_numbers(string_to_check):
    new_string = ""
    number_string = "0123456789"
    for i in string_to_check:
        for j in number_string:
            if i == j:
                new_string += j
    if string_to_check == new_string:
        return True
    return False


# Exercise 6c
def is_valid_code_guess(code, number_of_digits, highest_digit):
    if len(code) != number_of_digits or contains_only_numbers(code) == False or  any_digit_exceeds_highest_digit_value(code, highest_digit):
        return False
    return True
    

# Exercise 7
def generate_code(number_of_digits, highest_digit):
    li = range (highest_digit)
    numbers = random.sample(li, number_of_digits)
    numbers_str = ""
    for i in numbers:
        num = str(i)
        numbers_str = numbers_str + num
        
    correct_code = numbers_str
    return correct_code
    
    
# Exercise 8
def get_hint(correct_code):
    num = random.randint(0, len(correct_code)-1)
    shown_num = correct_code[num]
    string_num = ""
    for i in correct_code:
        if i != shown_num:
            i = "X"
        string_num += i
    return string_num
    

# Exercise 9
# needs rethinking!
def compare(code, correct_code):
    return_string = []
    count = 0
    index = 0
    count1 = 0
    code = code
    correct_code = correct_code
    for i in range(0, len(code)):
        if code[i] == correct_code[index]:
            count +=1
        index +=1
        
    if len(set(code)) == 1 or len(set(code)) == 2:
        for i in range (len(code)):
            for j in range (len(correct_code)):
                if code[i] == correct_code[j] and i != j:
                    count1 +=1
    else:
        for i in code:
            for j in correct_code:
                if i == j and code.index(i) != correct_code.index(j):
                    count1 += 1
    
            
    
                
    
    return_string = [code] + [count] + [count1]
    return return_string
    


#########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE.
#########################################

#########################################
# Test code.
#########################################

def test():
    """Return the number of exercises correctly implemented."""
    score = 0
    
    # Exercise 1
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_correct_code("2431")
    
    
    # Exercise 2
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_win_message([["3210", 4, 0]])
    show_win_message([["0123", 0, 4], ["3210", 4, 0]])
    
    
    # Exercise 3a
    # TEST 1 #
    print( "# TEST 3a : to_string() #" )
    t3a_1 = to_string(["0123", 2, 1])
    t3a_2 = to_string(["2322338", 4, 0])
    print(t3a_1)
    print(t3a_2)
    
    if t3a_1 == "0123 - Correct: 2 / Wrong position: 1" and t3a_2 == "2322338 - Correct: 4 / Wrong position: 0":
        score += 1
        print("# TEST 3A SUCCESS #")
    else:
        print("# TEST 3A FAILED #")
    print( "--------------------" )
       
       
    # Exercise 3b
    # This does not test your code, but it calls the function so the result can be seen in the shell.
    show_all_attempts([["0123", 0, 4], ["1111", 1, 3], ["2211", 2, 2], ["3210", 4, 0]])
    
    
    # Exercise 4
    print( "# TEST 4 : has_attempts_remaining() #" )
    t4_1 = has_attempts_remaining( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0] ], 10 )
    t4_2 = has_attempts_remaining( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0] ], 2 )
    t4_3 = has_attempts_remaining( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0], ["5412", 4, 0] ], 10 )
    t4_4 = has_attempts_remaining( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0], ["5412", 4, 0] ], 3 )
    t4_5 = has_attempts_remaining( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0], ["5412", 4, 0] ], 4 )
    print(t4_1)
    print(t4_2)
    print(t4_3)
    print(t4_4)
    print(t4_5)
    
    if t4_1 and not t4_2 and t4_3 and not t4_4 and not t4_5:
        score += 1
        print("# TEST 4 SUCCESS #")
    else:
        print("# TEST 4 FAILED #")
    print( "--------------------" )
  
  
    # Exercise 5
    print( "# TEST 5 : is_game_won() #" )
    t5_1 = is_game_won( [] )
    t5_2 = is_game_won( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0], ["5410", 3, 0] ] )
    t5_3 = is_game_won( [ ["4000", 0, 1], ["4012", 2, 1], ["0412", 3, 0], ["5410", 3, 0], ["5412", 4, 0] ] )
    print( t5_1 )
    print( t5_2 )
    print( t5_3 )

    if not t5_1 and not t5_2 and t5_3:
        score += 1
        print("# TEST 5 SUCCESS #")
    else:
        print("# TEST 5 FAILED #")
    print( "--------------------" )
    
    
    # Exercise 6a
    print( "# TEST 6a : any_digit_exceeds_highest_digit_value() #" )
    t6a_1 = any_digit_exceeds_highest_digit_value("0", 3)
    t6a_2 = any_digit_exceeds_highest_digit_value("4344", 4)
    t6a_3 = any_digit_exceeds_highest_digit_value("2987778", 7)
    t6a_4 = any_digit_exceeds_highest_digit_value("02159", 6)
    print( t6a_1 )
    print( t6a_2 )
    print( t6a_3 )
    print( t6a_4 )
    
    if not t6a_1 and not t6a_2 and t6a_3 and t6a_4:
        score += 1
        print("# TEST 6a SUCCESS #")
    else:
        print("# TEST 6a FAILED #")
    print( "--------------------" )
    
    
    # Exercise 6b
    print( "# TEST 6b : contains_only_numbers() #" )
    t6b_1 = contains_only_numbers("0")
    t6b_2 = contains_only_numbers("990087654123")
    t6b_3 = contains_only_numbers("O0431")
    t6b_4 = contains_only_numbers("79 72 04")
    t6b_5 = contains_only_numbers("1234+")
    print( t6b_1 )
    print( t6b_2 )
    print( t6b_3 )
    print( t6b_4 )
    print( t6b_5 )
    
    if t6b_1 and t6b_2 and not t6b_3 and not t6b_4 and not t6b_5:
        score += 1
        print("# TEST 6b SUCCESS #")
    else:
        print("# TEST 6b FAILED #")
    print( "--------------------" )
        
        
    # Exercise 6c
    print( "# TEST 6c : is_valid_code_guess() #" )
    t6c_1 = is_valid_code_guess("0", 1, 4)
    t6c_2 = is_valid_code_guess("990087654123", 12, 9)
    t6c_3 = is_valid_code_guess("O0431", 5, 6)
    t6c_4 = is_valid_code_guess("79 72 04", 8, 9)
    t6c_5 = is_valid_code_guess("1234+", 5, 5)
    t6c_6 = is_valid_code_guess("4344", 4, 4)
    t6c_7 = is_valid_code_guess("2987778", 7, 7)
    t6c_8 = is_valid_code_guess("02159", 5, 6)
    t6c_9 = is_valid_code_guess("", 1, 9)
    t6c_10 = is_valid_code_guess("0332", 5, 9)
    print( t6c_1 )
    print( t6c_2 )
    print( t6c_3 )
    print( t6c_4 )
    print( t6c_5 )
    print( t6c_6 )
    print( t6c_7 )
    print( t6c_8 )
    print( t6c_9 )
    print( t6c_10 )
    
    if t6c_1 and t6c_2 and not t6c_3 and not t6c_4 and not t6c_5 and t6c_6 and not t6c_7 and not t6c_8 and not t6c_9 and not t6c_10:
        score += 1
        print("# TEST 6c SUCCESS #")
    else:
        print("# TEST 6c FAILED #")
    print( "--------------------" )
    
    
    # Exercise 7
    #The code for this test is more complex than usual, because of the randomness involved. We've written some code to run the function a few times, and analyze whether each result is different and correct.
    print( "# TEST 7 : generate_code() #" )
    unique_digits = True
    always_same_code = True
    code_length_correct = True
    numbers_only = True
    
    for i in range(0, 3):
        first_code = generate_code(i+4, i+5)      
        for j in range(0,10):
            generated_code = generate_code(i+4, i+5)
            if first_code != generated_code:
                always_same_code = False
            if len(generated_code) != i+4:
                code_length_correct = False                             
            count_list = []
            for k in range(0,10):
                count_list = count_list + [0]               
            for element in generated_code:
                if not element in "0123456789":
                    numbers_only = False
                    break
                count_list[int(element)] = count_list[int(element)] + 1
            for total in count_list:
                if total > 1:                    
                    unique_digits = False               
    
    #We check four different cases and print the output here
    if always_same_code:        
        print("# TEST 7 FAILED # The generated code is not random.")
    if not code_length_correct:
        print("# TEST 7 FAILED # Generated code is not a string with the correct number of digits.")
    if not numbers_only:
        print("# TEST 7 FAILED # Generated code does not contain numbers only.")
    if not unique_digits:
        print("# TEST 7 FAILED # All digits of the generated code must be unique.")
    
    if not always_same_code and code_length_correct and numbers_only and unique_digits:
        score += 1
        print("# TEST 7 SUCCESS #")
    print( "--------------------" )


    # Exercise 8
    print( "# TEST 8 : generate_code() #" )
    correct_string = True
    random_hints = False
    
    t8_1 = get_hint("120")
    t8_2 = get_hint("5421")
    print( t8_1 )
    print( t8_2 )
    
    if t8_1 != "1XX" and t8_1 != "X2X" and t8_1 != "XX0" or len(t8_2) != 4:
        correct_string = False
    
    for i in range(0,10):
        if t8_1 != get_hint("120"):
            random_hints = True
    
    if correct_string and random_hints:
        score += 1
        print("# TEST 8 SUCCESS #")
    else:
        print("# TEST 8 FAILED #")
    print( "--------------------" )
        
            
    # Exercise 9
    print( "# TEST 9 : compare() #" )
    t9_1 = compare("0", "0")
    t9_2 = compare("1111", "3201")
    t9_3 = compare("531", "153")
    t9_4 = compare("90210", "90210")
    t9_5 = compare("1155", "1253")
    print( t9_1 )
    print( t9_2 )
    print( t9_3 )
    print( t9_4 )
    print( t9_5 )
    
    if t9_1 == ["0", 1, 0] and t9_2 == ["1111", 1, 3] and t9_3 == ["531", 0, 3] and t9_4 == ["90210", 5, 0] and t9_5 == ["1155", 2, 2]:
        score += 1
        print("# TEST 9 SUCCESS #")
    else:
        print("# TEST 9 FAILED #")
    print( "--------------------" )


    print()        
    print("Score: " + str(score) + "/9")
    return score

if __name__ == "__main__":
    test()

################################################################################
# Additional functions. Not part of the exercises, but required to run the game.
################################################################################

def ask_input(code_attempts, max_attempts):
    """Print a request that the player has to input a code, and return the player's input.

    Parameters:
    code_attempts (list) -- Contains all player's attempts.
    max_attempts (int) -- The maximum number of attempts allowed.
    """
    message = "Attempt " + str(len(code_attempts)+1) + "."
    random_number = random.randint(0, 2)
    random_messages = []
    if len(code_attempts)+1 < max_attempts/2:
        random_messages += ["Try to guess the correct code."]
        random_messages += ["Can you find the code?"]
        random_messages += ["What's your guess?"]
    else:
        random_messages += ["Not many attempts left. Will you crack the code?"]
        random_messages += ["Only " + str(max_attempts-len(code_attempts)) + " left."]
        random_messages += ["You're getting closer to the solution. Make each try count."]
    print(message + " " + random_messages[random_number])
    return input()

def show_objective(number_of_digits, highest_digit_value, max_attempts):
    """Print the game rules.

    Parameters:
    number_of_digits (int) -- The number of unique digits the code should have.
    highest_digit_value (int) -- The highest value that is allowed for any digit of the code.
    max_attempts (int) -- The maximum number of attempts allowed.
    """
    time.sleep(1)
    print_separator()
    print("Objective:")
    print("Find the " + str(number_of_digits) + "-digit code in at most " + str(max_attempts)
          + " attempts. All digits are between 0 and "
          + str(highest_digit_value) + " (both included).")
    print_separator()
    time.sleep(1)

def show_feedback(nb_of_correct_digits, nb_of_digits_in_wrong_position):
    """Print feedback on the player's guess.

    Parameters:
    nb_of_correct_digits (int) -- The number of correct digits the player's code has at the correct position.
    nb_of_digits_in_wrong_position (int) -- The number of wrongly placed correct digits in the player's code.
    """
    print("- Correct digits at correct position: " + str(nb_of_correct_digits))
    print("- Correct digits at wrong position: " + str(nb_of_digits_in_wrong_position))

def show_win_conditionally(cheated, hints_needed):
    """Print a message to let the player know they used the cheat or hint command.

    Parameters:
    cheated (boolean) -- Contains true if the player used the cheat command.
    hints_needed (int) -- The number of times the players asked for a hint.
    """
    time.sleep(3)
    message = "...That would be the message you'd get to see here, but "
    if cheated:
        message = message + "you've cheated to win"
    if cheated and hints_needed > 0:
        message = message + ", and "
    if hints_needed > 0:
        message = message + "you've asked for a hint " + str(hints_needed) + " time"
    if hints_needed > 1:
        message = message + "s"
    message = message + ". As a result, your score remains unchanged."
    print(message)
    time.sleep(3)

def show_lose_message(correct_code):
    """Print a message to inform the player that they've lost.

    Parameters:
    correct_code (string) -- The code the player had to guess.
    """
    print("Too bad! No more attempts left. The correct code was " + correct_code + ".")

def show_reward_code_length_increased():
    """Print a message to inform the player that the code length is increased by one digit."""
    time.sleep(2)
    print("The length of the code is now increased by one digit!")

def show_reward_digit_value_cap_increased():
    """Print a message to inform the player that the highest possible value of each digit is increased."""
    time.sleep(2)
    print("The highest possible value of each digit is now increased by one!")

def show_reward_attempts_increased():
    """Print a message to inform the player that they gained to additional attempts from next game on."""
    time.sleep(2)
    print("You get two additional attempts in your next game!")

def show_score(score):
    """Print the player's score.

    Parameters:
    score (int) -- The player's current score.
    """
    time.sleep(1)
    print("Score: " + str(score))

def show_hint(hint):
    """Print the given hint.

    Parameters:
    hint (string) -- The hint to print.
    """
    print_separator()
    print("Hint: " + hint)
    print_separator()

def show_invalid():
    """Print a message to inform the player that their input is invalid."""
    print_separator()
    print("The code or command you've entered is invalid.")
    print_separator()

def show_game_header():
    """Print the header with the title of the game."""
    print("=====================")
    print("||   MASTERMIND+   ||")
    print("=====================")

def print_separator():
    """Print a separator to make all text appearing on screen more readable/structured."""
    print("---------------------")