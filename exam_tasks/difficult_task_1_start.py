# TASK 1 #

def get_minors(year, minors):
    li_in_li = []
    year_index = 0
    li_names = []
    li_years = []
    
    for name_index in range (0, len(minors[0])):
        person_year = minors[1][year_index]
        if person_year > (year - 18):
            li_names += [minors[0][name_index]]
            li_years += [person_year]
        year_index += 1
        
    li_in_li += [li_names] + [li_years]
        
    return li_in_li

# TASK 2 #

def read_from_file(filename):
    file = open(filename)
    counter = 0
    list_of_years = []
    list_of_names = []
    list_of_years_2 = []
    list_of_names_2 = []
    for data in file:
        if counter % 2 == 0:
            year = data[4:8]
            counter+=1
            list_of_years += [year]
        else:
            name = data[:-1]
            counter+=1
            list_of_names += [name]
    
    for index, value in enumerate(list_of_years):
        if int(value) >= 2023-18:
            list_of_names_2 += [list_of_names[index]]
            list_of_years_2 += [int(value)]
 
    return [list_of_names_2, list_of_years_2]
    

### DON'T CHANGE ANYTHING BELOW THIS LINE ###

def test():
    
    score = 0
    
    # TEST 1 #
    print("# TEST 1 : get_minors() #")
    t1_1 = get_minors(2023, [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]])
    t1_2 = get_minors(2020, [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]])
    print(t1_1)
    print(t1_2)
    if t1_1 == [['Sarah', 'James'], [2019, 2019]] and t1_2 == [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]]:
        score += 2
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print("--------------------")
        
    # TEST 2 #
    print("# TEST 2 : read_from_file() #")
    t2_1 = read_from_file("minors.txt")
    t2_2 = read_from_file("adults.txt")
    print(t2_1)
    print(t2_2)
    if t2_1 == [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]] and t2_2 == [[],[]]:
        score += 4
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print("--------------------")
    

    
    print("Final score:", score)
    
if __name__ == "__main__":
    test()