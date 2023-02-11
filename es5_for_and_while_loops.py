
#ex1
number = 0
def print_odd(number):
    for number in range(1, 100):
        if number%2!=0:
            print (number)
            number +=1
             
print_odd(number)

#ex2
number = 7
def multipliers(number):
    for i in range(1, 11):
        mul_number = number*i
        i+=1
        print (mul_number, end="\t")
        

multipliers(number)

#ex3.1

word = "elevator"
def print_letters(word):
    letter = 0
    for i in word:
        letter += 1
        print (i, end=" ")     
print_letters(word)

#ex3.2
word = "casino"
def print_vowels(word):
    letter = 0
    for i in word:
        if i == "a" or i == "e" or i == "u" or i == "i" or i == "o":
            letter += 1
            print (i, end=" ")
        else:
            letter +=1          
print_vowels(word)
    
#ex3.3
word = "videogame"
def print_vowel_locations(word):
    letter = 0
    for i in word:
        if i == "a" or i == "e" or i == "u" or i == "i" or i == "o":
            letter += 1
            print (str(i) + str(letter), end=" ")
        else:
            letter +=1          
print_vowel_locations(word)


#ex5 - did not get the correct code
price = 25000 
budget = 12000 
annual_savings = 2500
interest = 2
inflation = 1

def savings_evolution(price, budget, annual_savings, interest, inflation):
    years = 0
    while price > budget:
        years+=1
        budget = budget * (years+interest) + annual_savings
        price = price * (years+inflation)
        print (price, budget)
    return years
        
print (savings_evolution(price, budget, annual_savings, interest, inflation))


#ex6 - game to guess randomly generated number
import random 
maximum_number = 20

def game(maximum_number):
    generated_number = random.randint(1, maximum_number)
    total_attempt = 5
    attempt = 1
    while total_attempt <= 5 and attempt > 0:
        number = int(input("Type in the number: "))
        if number > generated_number:
            left_attempt = total_attempt - attempt
            print ("too big, ", left_attempt, "attempts left")
            attempt+=1
        elif number < generated_number:
            left_attempt = total_attempt - attempt
            print ("too small, ", left_attempt, "attempts left")
            attempt+=1
        elif number == generated_number:
            print ("Congratulations, you win!")
            break
        else:
            break
        
        if left_attempt == 0:
            print ("Game over, the correct answer was ", generated_number)
            break

game(maximum_number)

ex7 how to remove numbers after dot?
circumference = 20

def rectangle_surface(circumference):
    half_circumference = circumference / 2
    length = 1
    surface = 1
    width = half_circumference - length
    while length < width:
        surface = length*width
        length+=1
    print ("The maximum surface is", surface, ". The length is: ", length, ". The width is: ", width)

rectangle_surface(circumference)


#print (length, width, surface)