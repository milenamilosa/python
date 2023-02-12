#ex1 How could you make this function “safer” to check whether an empty list was passed?
list = [3,4,1,0]
def print_first_element(list):
    if not list:
        print ("List is empty.")
    else:
        print(list[0])
    
print_first_element(list)
print ("\n")

#ANOTHER WAY through length
list = []
def print_first_element(list):
    if len(list) == 0:
        print('the list is empty')
    else:
        print(list[0])
    
print_first_element(list)
print ("\n")

#ex2
list = [3,4,1,0]
def print_all_elements_of_list(list):
    element = 0
    for element in list:
        print(element)
        
print_all_elements_of_list(list)
print ("\n")

list = "This is a sentance"
def print_all_elements_of_list_string(list):
    element = 0
    for element in list:
        print(element)
        
print_all_elements_of_list_string(list)
print ("\n")

list = [3,4,1,0]
def print_all_elements_of_list_alternative_vers(list):
    element = 0
    while element <= len(list)-1:
        print (list[element])
        element+=1
print_all_elements_of_list_alternative_vers(list)
print ("\n")

list = [3,4,1,0]
def print_all_elements_of_list_alternative_vers_2(list):
    index = 0
    while index < len(list) :
        print(list[index])
        index +=1
        
print_all_elements_of_list_alternative_vers_2(list)


