### FUNCTION DEFINITIONS ###
import random
#Exercise 3
def get_shortest_list(list_1, list_2):    
    if len(list_1) > len(list_2):
        return list_2
    elif len(list_1) < len(list_2):
        return list_1
    else:
        return list_1

#Exercise 4
def count(element_list, element):
    number = 0
    i = 0
    for i in element_list:
        if element == i:
            number +=1
            
    return number    
    
    

#Exercise 5
def contains_element(element_list, element):
    for element_ in element_list:
        if element_ == element:
            return True
    return False
       

#Exercise 6
def last_occurrence(element_list, element):
    size = len(element_list)-1
    while size >= 0:
        if element == element_list[size]:
            return size

        size-=1


    return -1


#Exercise 7a
def divisors(number):
    list = []
    starter_number = 0
    for starter_number in range (1, number+1):
        if number%starter_number == 0:
            list = list + [starter_number]
        else:
            starter_number +=1
    return list
    

#Exercise 7b
def divisors_high_to_low(number):
    list = []
    starter_number = number
    while starter_number > 0:
        if number%starter_number == 0:
            list = list + [starter_number]
    
        starter_number -=1
    return list


#Exercise 8
def find_largest_number(number_list):
    number_list = sorted(number_list)

    return number_list[len(number_list)-1]

#Exercise 9
def replace(element_list, element_to_replace, new_element):
    count = 0
    for i,x in enumerate(element_list):
        if x==element_to_replace:
            count+=1
        if count ==2:
            element_list[i] = new_element
    
    return element_list


#Exercise 10
def count_x_y(count_string):
    
    count = 0
    for i in range (0, len(count_string)-2):
        n = i+2
        if count_string[i] == "x" and count_string[n] == "y":
            count += 1
        if count_string[i] == "y" and count_string[n] == "x":
            count +=1
            
    return count
    
#Exercise 11
def is_palindrome(string_to_check):
    #another_string = elements from last to first
    #one_more_string = elements of string_to_check from first to last but separated into chars
    
    another_string = []
    index = len(string_to_check) - 1
    while index >= 0:
        another_string = another_string + [string_to_check[index]]
        index -=1
    
    one_more_string = []
    second_index=0
    while second_index < len(string_to_check):
        one_more_string = one_more_string + [string_to_check[second_index]]
        second_index+=1
    
    if another_string == one_more_string:
        return True
    return False

#Exercise 12
def is_near_palindrome(string_to_check):
    
    another_string = []
    index = len(string_to_check) - 1
    one_more_string = []
    second_index = 0    
    mistake_count = 0
    
    while index >= 0:
        another_string = another_string + [string_to_check[index]]
        index -= 1
    
    while second_index < len(string_to_check):
        one_more_string = one_more_string + [string_to_check[second_index]]
        second_index += 1
        
    for i in range (0, len(string_to_check) - 1):
        if another_string[i] != one_more_string[i]:
            mistake_count += 1
    if mistake_count > 2:
        return False
    return True

    #another_string[character] == one_more_string[character]:
         
    
    
    
    return False


### main program ###
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():    
    final_grade = 0
    
    # TEST 1 #
    print( "# TEST 1 : exercise 3 - get_shortest_list() #" )
    t1_1 = get_shortest_list([1, -8, 6], [9, 7])
    t1_2 = get_shortest_list([9, 9, 9], [4, 0, 1])
    t1_3 = get_shortest_list([], [0, 3])
    t1_4 = get_shortest_list("string", "much longer string")
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    
    if t1_1 == [9, 7] and t1_2 == [9, 9, 9] and t1_3 == [] and t1_4 == "string":
        final_grade = final_grade + 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    # TEST 2 #
    print( "# TEST 2: exercise 4 - count() #" )
    t2_1 = count(["a","b","c"], "a")
    t2_2 = count([7, 8, 4, 2, 2, 2], 2)
    t2_3 = count("test string", "T")
    t2_4 = count([], 0)
    print(t2_1)
    print(t2_2)
    print(t2_3)
    print(t2_4)
    
    if t2_1 == 1 and t2_2 == 3 and t2_3 == 0 and t2_4 == 0:
        final_grade = final_grade + 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )

    # TEST 3 #
    print( "# TEST 3: exercise 5 - contains_element() #" ) 
    t3_1 = contains_element(["a","b","c"], "b")
    t3_2 = contains_element([7,8,-9], -7)
    t3_3 = contains_element("this is a string", "h")
    t3_4 = contains_element([], 5)
    print(t3_1)
    print(t3_2)
    print(t3_3)
    print(t3_4)

    if t3_1 and not t3_2 and t3_3 and not t3_4:
        final_grade = final_grade + 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    
    # TEST 4 #
    print( "# TEST 4: exercise 6 - last_occurrence() #" )
    t4_1 = last_occurrence([5, 3, 8], 3)
    t4_2 = last_occurrence([7, 8, 4, 2, 2, 2], 2)
    t4_3 = last_occurrence(["a", "b", "c"], "x")
    t4_4 = last_occurrence("contrafibularities", "a")
    print(t4_1)
    print(t4_2)
    print(t4_3)
    print(t4_4)
    
    if t4_1 == 1 and t4_2 == 5 and t4_3 == -1 and t4_4 == 11:
        final_grade = final_grade + 1
        print( "TEST 4 SUCCESS" )
    else:
        print( "TEST 4 FAILED" )
    print( "--------------------" )

    # TEST 5 #
    print( "# TEST 5: exercise 7a - divisors() #" )
    t5_1 = divisors(6)
    t5_2 = divisors(1)
    t5_3 = divisors(97)
    print(t5_1)
    print(t5_2)
    print(t5_3)
    
    if t5_1 == [1, 2, 3, 6] and t5_2 == [1] and t5_3 == [1, 97]:
        final_grade = final_grade + 1
        print( "TEST 5 SUCCESS" )
    else:
        print( "TEST 5 FAILED" )
    print( "--------------------" )
    
    # TEST 6 #
    print( "# TEST 6: exercise 7b - divisors_high_to_low() #" )
    t6_1 = divisors_high_to_low(6)
    t6_2 = divisors_high_to_low(1)
    t6_3 = divisors_high_to_low(97)
    print(t6_1)
    print(t6_2)
    print(t6_3)
    
    if t6_1 == [6, 3, 2, 1] and t6_2 == [1] and t6_3 == [97, 1]:
        final_grade = final_grade + 1
        print( "TEST 6 SUCCESS" )
    else:
        print( "TEST 6 FAILED" )
    print( "--------------------" )
    
    # TEST 7 #
    print( "# TEST 7: exercise 8 - find_largest_number() #" )
    t7_1 = find_largest_number([4, 3, 9, 0, -1, 7])        
    t7_2 = find_largest_number([0.3, -1.4, 0.3, -4.5])
    t7_3 = find_largest_number([-9876000, -9000111, -9876000])
    print(t7_1)
    print(t7_2)
    print(t7_3)
    
    if t7_1 == 9 and t7_2 == 0.3 and t7_3 == -9000111:
        final_grade = final_grade + 1
        print( "TEST 7 SUCCESS" )
    else:
        print( "TEST 7 FAILED" )
    print( "--------------------" )

    # TEST 8 #
    print( "# TEST 8: exercise 9 - replace() #" )
    t8_1 = replace(["a", "h", "b", "f", "a", "a", "z"], "a", "-")
    t8_2 = replace(["+", "+", "+", "+", "+", "+"], "+", "9")
    t8_3 = replace([0, 4, 2, 2, 3], 4, 7)
    t8_4 = replace([], "x", " ")
    print(t8_1)
    print(t8_2)
    print(t8_3)
    print(t8_4)
    
    if t8_1 == ["a", "h", "b", "f", "-", "a", "z"] and t8_2 == ["+", "9", "+", "+", "+", "+"] and t8_3 == [0, 4, 2, 2, 3] and t8_4 == []:
        final_grade = final_grade + 1
        print( "TEST 8 SUCCESS" )
    else:
        print( "TEST 8 FAILED" )
    print( "--------------------" )
    
    # TEST 9 #
    print( "# TEST 9: exercise 10 - count_x_y() #" )
    t9_1 = count_x_y("xzy")
    t9_2 = count_x_y("axyyx8yx")
    t9_3 = count_x_y("xy")
    t9_4 = count_x_y("xxxxyyyy")
    print(t9_1)
    print(t9_2)
    print(t9_3)
    print(t9_4)
    
    if t9_1 == 1 and t9_2 == 3 and t9_3 == 0 and t9_4 == 2:
        final_grade = final_grade + 1
        print( "TEST 9 SUCCESS" )
    else:
        print( "TEST 9 FAILED" )
    print( "--------------------" )
        
    # TEST 10 #
    print( "# TEST 10: exercise 11 - is_palindrome() #" )
    t10_1 = is_palindrome("AA")
    t10_2 = is_palindrome("rotor")
    t10_3 = is_palindrome("6gTXq+;f4f;+qXTg6")
    t10_4 = is_palindrome("rotir")
    t10_5 = is_palindrome("word")
    print(t10_1)
    print(t10_2)
    print(t10_3)
    print(t10_4)
    print(t10_5)
    
    if t10_1 and t10_2 and t10_3 and not t10_4 and not t10_5:
        final_grade = final_grade + 1
        print( "TEST 10 SUCCESS" )
    else:
        print( "TEST 10 FAILED" )
    print( "--------------------" )

    # TEST 11 #
    print( "# TEST 11: exercise 12 - is_near_palindrome() #" )
    t11_1 = is_near_palindrome("AA")
    t11_2 = is_near_palindrome("rotor")
    t11_3 = is_near_palindrome("6GTXq+;f4f;+qXTg6")
    t11_4 = is_near_palindrome("6GTXq-;f4f;+qXTg6")
    t11_5 = is_near_palindrome("word")
    print(t11_1)
    print(t11_2)
    print(t11_3)
    print(t11_4)
    print(t11_5)
    
    if t11_1 and t11_2 and t11_3 and not t11_4 and not t11_5:
        final_grade = final_grade + 1
        print( "TEST 11 SUCCESS" )
    else:
        print( "TEST 11 FAILED" )
    print( "--------------------" )
     
            
    print("Your score for this lab is ", final_grade, "/11.")
    
    
if __name__ == "__main__":    
    test() 