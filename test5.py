#RETURN. return value

#leap year exercise
#what to do: find
#whethter the year is a multiple of 100 (%100)
#whether the year is a multiple of 4 or 400 (% base_number)

def is_century(year):
    year_century = year % 100
    if year_century == 0:
        return True
    else:
        return False

def is_multiple_of(year, base_number):
    remainder_year = year % base_number
    if remainder_year == 0:
        return True
    else:
        return False
    
year = 2020
    
test_century = is_century(year)
if test_century == True:
    test_multiple_of = is_multiple_of(year, 400)
else:
    test_multiple_of = is_multiple_of(year, 4)

if  test_multiple_of == True:
    print (year, "is a leap year.")
else:
    print (year, "is not a leap year.")
print ("\n")


#everything that is writen in a function, stays in the function
#to define a parameter globaly, we need to return the value from the function
#literally return
#to debug the code that has 1 variable and 2+ meaning to it,
#write "store at", id(parameter). this will hint on the location of cell
#where the word is stored at. if cells are diff, the code is bugged
#example:
def canadian_english(word):
    if word == "harbor":
        word = "harbour"
        print ("During coversation:", word, "stored at", id(word))

word = "harbor"
print ("Before conversation:", word, "stored at", id(word))
canadian_english(word)
print ("After conversation:", word, "stored at", id(word))

#how to fix it. change the name of the variable in the function
#so its not the same as global

def canadian_english(word_two):
    if word_two == "harbor":
        word_two = "harbour"
        print ("During coversation:", word_two)
    return word_two

word = "harbor"
print ("Before conversation:", word)
word = canadian_english(word)
print ("After conversation:", word)