### Define functions ###

def extract_doodle(file_name):
    file = open(file_name)
    counter = 0
    first_list = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = [list1, list2, list3, list4]
    list6 = []
    
    for data in file:
        first_list = first_list + [data[:-1]]
    
    for list_n in list5:
        list_n = list_n + [first_list[counter]]
        counter += 1
        while first_list[counter] != "END":
            list_n = list_n + [int(first_list[counter])]
            counter += 1
        counter += 1
        list6 = list6 + [list_n]
    return list6


# def extract_doodle(file_name):
#     file = open(file_name)
#     counter = 0
#     list1 = []
#     list2 = []
#     list3 = []
#     list4 = []
#     list5 = []
#     first_list = []
#     
#     for data in file:
#         first_list = first_list + [data[:-1]]
#     
#     list1 = list1 + [first_list[counter]]
#     counter += 1
#     while first_list[counter] != "END":
#         list1 = list1 + [int(first_list[counter])]
#         counter += 1
#     counter += 1
#     list2 = list2 + [first_list[counter]]
#     counter += 1
#     while first_list[counter] != "END":
#         list2 = list2 + [int(first_list[counter])]
#         counter += 1
#     counter += 1
#     list3 = list3 + [first_list[counter]]
#     counter += 1
#     while first_list[counter] != "END":
#         list3 = list3 + [int(first_list[counter])]
#         counter += 1
#     counter += 1
#     list4 = list4 + [first_list[counter]]
#     counter += 1
#     while first_list[counter] != "END":
#         list4 = list4 + [int(first_list[counter])]
#         counter += 1
#     list5 = [list1] + [list2] + [list3] + [list4]
#     
#     return list5
    
#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    file_name_of_availabilities = "lab8_doodle.txt"
    final_grade = 0
    
    # TEST #
    print( "# TEST : extract_doodle() #" )
    t1 = extract_doodle(file_name_of_availabilities)
    print(t1)
    
    if len(t1) == 4 and len(t1[1]) == 6 and t1[0][0] == "Kathrin" and t1[3][5] == 41:
        final_grade += 1
        print( "TEST SUCCESS" )
    else:
        print( "TEST FAILED" )
    print( "--------------------" )
    
    
    print("Your score for this exercise is ", final_grade, "/1.")
    
    


if __name__ == "__main__":    
    test() 

