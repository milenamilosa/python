# alter the code so that it does what it should do (done)

age = 1

if (age < 18 and age > 0):
    message = "you are a minor"
elif (age >= 18):
    message = "you are an adult"
elif (age <= 0):
    message = "error - age < 0"
    
print(message)