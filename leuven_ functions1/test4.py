#simple function without parameters
#to define a function write "def", then "the name" of the function and then "parentheses" (round brackets)
#in fuction's name you can use letter, lowercase and numbers, but cant start with a number


def say_hi(): #define a function without parameter
    print ("Hi")
    
say_hi() #this is how the function is called
print ("\n")
##############################

def print_average():
    '''Calculates average of 2 scores.
        Prints average of 2 scores.
    ''' #this is how the explanation is writen. to know wth it is doing type in shell "help (name)"
    average=(score1+score2)/2
    print (" ", average)
    
print ("Averages")
print ("---------")
#score of cat
score1=10
score2=13
print ("cat")
print_average()
#score of dog
score1=20
score2=14
print ("dog")
print_average()
#score of han
score1=13
score2=5
print ("han")
print_average()


#simple function with parameters
def print_square(num):
    '''Calculates and prints the square of num.
    '''
    squarednum=num*num
    print ("The square of", num, "is", squarednum)

def print_average(score1, score2):
    '''Calculates average of 2 scores.
        Prints average of 2 scores.
    ''' 
    average=(score1+score2)/2
    print ("The average of", score1, "and", score2, "is", average)
    
print_square(3)

number = 9
print_square(number)
print_average(1, 3)

print ("\n")

def print_average(name, score1, score2):
    average=(score1+score2)/2
    print ("The average for", name, "is", average)
    
print ("Averages")
print ("---------")
#score of cat
print_average("cat", 10, 13)
#score of dog
print_average("dog", 20, 14)
#score of han
print_average("han", 13, 5)