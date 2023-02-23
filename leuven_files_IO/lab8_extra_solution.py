# having this text document:

# Jayce Mcdowell
# 15
# x
# 8
# 17
# Julio Woodward
# x
# x
# x
# x
# Wendy Fischer
# 18
# 10
# 10
# 10
# Trey Ruiz
# 15
# 20
# x
# 10
# Laci Phillips
# 14
# 18
# 18
# x
# Morgan Kaiser
# 18
# 14
# 18
# 18
# Kinley Castaneda
# x
# x
# x
# 0

def extract_best_courses(file_name):
    courses = ["Maths","Chemistry","Physics","Biology"]
    file = open(file_name, "r")
    index = 0
    best_courses = []
    course_marks_new_student = []
    new_student = ""
    for line in file:
        if index % 5 == 0:
            new_student = line.rstrip() + ": "
        else:
            if not "x" in line:
                course_marks_new_student += [int(line)]
            else:
                course_marks_new_student += [-1]
            if index % 5 == 4:
                
                # calculate maximum (going from -1) 
                max_for_this_student = -1
                for course_index in range(4):
                    if course_marks_new_student[course_index] > max_for_this_student:
                        max_for_this_student = course_marks_new_student[course_index]
                string_to_add = new_student
                
                # determine which courses should be listed
                courses_to_add = []
                for course_index in range(4):
                    if max_for_this_student != -1 and course_marks_new_student[course_index] == max_for_this_student:
                        courses_to_add +=  [courses[course_index]]
                if courses_to_add == []:
                    string_to_add += "<absent for all courses>"
                else:
                    for course_to_add_index in range(len(courses_to_add)):
                        string_to_add += courses_to_add[course_to_add_index]
                        
                        # separate by "/" for all but last
                        if course_to_add_index != len(courses_to_add) - 1:
                             string_to_add += "/"
                best_courses += [string_to_add]
                course_marks_new_student = []
        index += 1
    return best_courses


#Test code
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#_______________________________________
def test():
    final_grade = 0
    t = extract_best_courses("course_results.txt")
    print(t)
    
    if t == ['Jayce Mcdowell: Biology', 'Julio Woodward: <absent for all courses>', 'Wendy Fischer: Maths', 'Trey Ruiz: Chemistry', 'Laci Phillips: Chemistry/Physics', 'Morgan Kaiser: Maths/Physics/Biology', 'Kinley Castaneda: Biology']:
        final_grade += 1
    
    print("Score after test " + str(final_grade) +"/1.")


if __name__ == "__main__":    
    test() 

