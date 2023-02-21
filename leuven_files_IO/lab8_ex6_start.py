### Define functions ###

def extract_years(file_name):
    file = open(file_name)
    years = []
    counter = 1
    for data in file:
        if counter % 3 == 0:
            years = years + [int(data[:-1])]
        counter += 1
    file.close()
    return years

def full_name_of_oldest(file_name):
    file = open(file_name)
    counter = 1
    first_list = []
    years = []
    for data in file:
        first_list = first_list + [data[:-1]]
        if counter % 3 == 0:
            years = years + [data[:-1]]
        counter += 1
        
    sorted_years = sorted(years)
    first_year = sorted_years[0]
    year_eldest_index = first_list.index(sorted_years[0])
    
    name_eldest = first_list[first_list.index(sorted_years[0]) - 2]
    surname_eldest = first_list[first_list.index(sorted_years[0]) - 1]
    ful_name = name_eldest + " " + surname_eldest
    
    return ful_name


#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    final_grade = 0
    
    # TEST 1 #
    print( "# TEST 1 : extract_years() #" )
    t1_1 = extract_years("lab8_teachers_1.txt")
    t1_2 = extract_years("lab8_teachers_2.txt")
    print(t1_1)
    print(t1_2)
    
    if t1_1 == [1991,1933,2005] and t1_2 == [1850,1964,1950]:
        final_grade += 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
        
    # TEST 2 #
    print( "# TEST 2 : full_name_of_oldest() #" )
    t2_1 = full_name_of_oldest("lab8_teachers_1.txt")
    t2_2 = full_name_of_oldest("lab8_teachers_2.txt")
    print(t2_1)
    print(t2_2)
    
    if t2_1 == "Stef Desmet" and t2_2 == "Nigel Vinckier":
        final_grade += 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", final_grade, "/2.")
    
    


if __name__ == "__main__":    
    test() 

