### Define functions ###

# PLAN 
# get element under group 1 till group 2
# get element under group 2 till group 3
# get the rest


def extract_groups(file_name):
    file = open(file_name)
    first_list = []
    group1 = []
    group2 = []
    group3 = []
    all_groups = []
    counter = 1
    
    for data in file:
        first_list = first_list + [data[:-1]]
        
    while first_list[counter] != "GROUP 2":
        group1 = group1 + [first_list[counter]]
        counter += 1
    counter += 1
    while first_list[counter] != "GROUP 3":
        group2 = group2 + [first_list[counter]]
        counter += 1
    counter += 1
    while counter < len(first_list):
        group3 = group3 + [first_list[counter]]
        counter += 1
#         
#     print(group1)
#     print(group2)
#     print(group3)
    all_groups = [group1] + [group2] + [group3]
    return all_groups
   
   
#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    file_name_of_groups = "lab8_groups.txt"
    final_grade = 0
    
    # TEST #
    print( "# TEST : extract_groups() #" )
    t1 = extract_groups(file_name_of_groups)
    print(t1)
    
    if len(t1) == 3 and len(t1[1]) == 10 and t1[2][2] == "Kristen Morton":
        final_grade += 1
        print( "TEST SUCCESS" )
    else:
        print( "TEST FAILED" )
    print( "--------------------" )
    
    print("Your score for this exercise is ", final_grade, "/1.")
    
    


if __name__ == "__main__":    
    test() 

