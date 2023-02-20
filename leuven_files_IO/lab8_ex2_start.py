### Define functions ###

def avgerage_score(file_name):
    file = open(file_name)
    score = 0
    sum_of_scores = 0
    counter = 0
    for line in file:
        score = int(line)
        sum_of_scores = sum_of_scores + score
        counter += 1
    file.close()   
    return (sum_of_scores/counter)

def nr_scores_higher_than(result, file_name):
    file = open(file_name)
    counter = 0
    for data in file:
        if int(data) > result:
            counter += 1
    file.close()
    
    return counter

def max_score(file_name):
    file = open(file_name)
    list_of_data = []
    
    for data in file:
        list_of_data = list_of_data + [int(data)]
    
    sorted_list = sorted(list_of_data)
    max_score = sorted_list[len(sorted_list)-1]
        
    return max_score

    
#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    file_name_of_ct = "lab8_results.txt"
    final_grade = 0
    
    # TEST 1 #
    print( "# TEST 1 : avgerage_score() #" )
    t1 = avgerage_score(file_name_of_ct)
    print(t1)
    
    if 11.73 < t1 < 11.75:
        final_grade += 1
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print( "--------------------" )
    
    
    # TEST 2 #
    print( "# TEST 2 : nr_scores_higher_than() #" )
    t2 = nr_scores_higher_than(10, file_name_of_ct)
    print(t2)
    
    if t2 == 15:
        final_grade += 1
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print( "--------------------" )
    
    # TEST 3 #
    print( "# TEST 3 : max_score() #" )
    t3 = max_score(file_name_of_ct)
    print(t3)
    
    if t3 == 18:
        final_grade += 1
        print( "TEST 3 SUCCESS" )
    else:
        print( "TEST 3 FAILED" )
    print( "--------------------" )
    
    print("Your score for this exercise is ", final_grade, "/3.")


if __name__ == "__main__":    
    test() 

