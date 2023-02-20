### Define functions ###

def names_and_years(file_name):
    file = open(file_name)
    counter = 0
    list_of_names = []
    list_of_years = []
    for data in file:
        if counter % 2 == 0:
            list_of_names = list_of_names + [data[:-1]]
            counter += 1
        else:
            list_of_years = list_of_years + [int(data[:-1])]
            counter += 1
    
    return [list_of_names, list_of_years]
    

#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    file_name_of_students = "lab8_names_years.txt"
    final_grade = 0
    
    # TEST #
    print( "# TEST : names_and_years() #" )
    t1 = names_and_years(file_name_of_students)
    print(t1)
    t_names = t1[0]
    t_years = t1[1]
    
    if len(t_names) == 12 and "Holden Burke" in t_names and t_years[8] == 1970:
        final_grade += 1
        print( "TEST SUCCESS" )
    else:
        print( "TEST FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", final_grade, "/1.")
    
    


if __name__ == "__main__":    
    test() 

