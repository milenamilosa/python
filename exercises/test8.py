#single line
def read_one_line(filename):
    file = open(filename)
    line_from_file = file.readline()
    file.close()
    print(line_from_file)
    
read_one_line("numbers.txt")

# file I/O simple
def read_numbers_from_file(file_name):
    text = open(file_name)
    for data in text:
        print(data[:-1])
    text.close()
    
read_numbers_from_file("numbers.txt")

# fileI/O complex
def read_names_from_file(file_name):
    text = open(file_name)
    counter = 0
    for data in text:
        if counter % 2 ==0:
            print(data[:-1])
            counter += 1
        else:
            counter += 1
    text.close()
    
read_names_from_file("student_grades.txt")    

# fileI/O 2
def read_grades_from_file(file_name):
    text = open(file_name)
    counter = 0
    sum_of_grades = 0
    for data in text:
        if counter % 2 != 0:
            print(data[:-1])
            sum_of_grades = sum_of_grades + int(data[:-1])
            counter += 1
        else:
            counter += 1
    text.close()
    return sum_of_grades / (counter/2)

print("The average of students grades is: ", read_grades_from_file("student_grades.txt"))
    
#
def add_student(filename, student_name, student_grade):
    file = open(filename, 'a')
    file.write(student_name)
    file.write("\n")
    file.write(str(student_grade))
    file.write("\n")
    file.close()
    
add_student("student_grades.txt", "JoJo", 10)
    