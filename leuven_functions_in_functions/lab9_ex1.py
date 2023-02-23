#ex1
# all functions in this exercise have one parameter: a list of unknown length with numbers between -100 and 100

a_list = [34, 8, 1, -57, 27, -565, 21, 55, -2, 5] #  filled with rand numbers for example

def list_without_negatives():
    without_negatives_list = []
    for i in a_list:
        if i >= 0:
            without_negatives_list = without_negatives_list + [i]
    return without_negatives_list

def positive_sorted():
    sorted_list = sorted(list_without_negatives())
    return sorted_list

def squared_list():
    squared_list = []
    for i in a_list:
        j = i*i
        squared_list = squared_list + [j]
    return squared_list

def square_over_thousand():
    square_over = []
    for i in a_list:
        j = i*i
        if j > 1000:
            square_over = square_over + [i]
    return square_over

def fibonacci():
    n = 0
    m = 1
    new_list = [n, m]
    while m < 100:
        n_next = m + n
        new_list = new_list + [n_next]
        n = m
        m = n_next
    
    if n_next > 100:
        new_list.remove(n_next)
    
    return new_list
    
def fibonacci_numbers_in_list():
    a_fibonacci = []
    for i in a_list:
        if i in fibonacci():
            a_fibonacci = a_fibonacci + [i]
    return a_fibonacci

def lottofy():
    count = 0
    temp_list = positive_sorted()
    temp_list_2 = []
    list_of_6 = []
    for i in temp_list:
        if i in fibonacci_numbers_in_list():
            temp_list_2 = temp_list_2 + [i]
            count += 1
    if count == 6:
        list_of_6 =  temp_list_2
        string = "The winning numbers are: "
        result = string + str(list_of_6)
    elif count > 6 or count < 6:
        string = " is not the correct amount of numbers to play the lotto"
        result = str(len(temp_list_2)) + string
        
        
    return result
        
print(lottofy())