### Define functions ###

def read_names_from_file(file_name):
    text = open(file_name)
    list_of_names = []
    for data in text:
        name = data.rstrip()
        list_of_names = list_of_names + [name]
    return list_of_names

def name_present_in_file(search_name, file_name):
    file = open(file_name)
    for data in file:
        name = data.rstrip()
        if name== search_name:
            return True 
    return False
    
    
#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    file_name_of_students = "lab8_names.txt"
    final_grade = 0
    
    # TEST 1 #
    print( "# TEST 1 : read_names_from_file() #" )
    t1 = read_names_from_file(file_name_of_students)
    print(t1)
    
    if len(t1) == 20 and "Holden Burke" in t1:
        final_grade += 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    
    # TEST 2 #
    print( "# TEST 2 : name_present_in_file() #" )
    t2_1 = name_present_in_file("Nigel Vinckier", file_name_of_students)
    t2_2 = name_present_in_file("Isabel Hines", file_name_of_students)
    t2_3 = name_present_in_file("Julie Scott", file_name_of_students)
    t2_4 = name_present_in_file("Julie Scott\n", file_name_of_students)
    print(t2_1)
    print(t2_2)
    print(t2_3)
    print(t2_4)
    if not t2_1 and t2_2 and t2_3 and not t2_4:
        final_grade += 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", final_grade, "/2.")
    
    


if __name__ == "__main__":    
    test() 

