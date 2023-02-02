#condition = sth that is true or false
#compare 1element to 2element (<, >, ==, !=, <=, >=)
#can compare AMONG THEMSELVES variables, values and operationas
#cant compare e.g. variable to value!
#can combine 2+ conditions using "and", "or"

age = 15
if age < 18: #colon is very important
    print ( "Not an adult yet" ) #tab is important so the program knows that we are in the body of the code
else:
    print ( "You are an adult" )
    if age > 65:
        print ( "Congratulations on retirement" ) #tab is impotant!
    else:
        print ( "Still of working age!" )
        
print ( "But everyone sees this text as it is not in the if " )

# or you can write the code like that:
# if age < 18:
#     print ( "Not an adult yet" )
# elif age > 65:
#     print ( "You are an adult" )
#     print ( "Congratulations on retirement" )
# else:
#     print ( "You are an adult" )
#     print ( "Still of working age!" )
# print ( "But everyone sees this text as it is not in the if " )
