def score():
    print("What's your name?")
    name = (input())
    print(name.upper())
    
    print("Enter midterm score: ")
    exam = int(input())

    print("Enter final score: ")
    final = int(input())
    
    print("Enter project sore:")
    project = int(input())
  

    sum = (exam*0.3 + final*0.5 + project*0.2)

    average = sum


    return average, name, exam


def compute_final_score(average, exam):
    final_score = 0.5 * average
    return final_score


def get_letter_grade(final_score):
    if  final_score > 90 :
        grade = 'AA'
    elif 70 <= final_score <= 90:
        grade = 'BB'
    elif 50 <= final_score <= 70:
        grade = 'CC'
    elif 30 <= final_score <= 50:
        grade = 'DD'
    else:
        grade = 'FF'
    return grade

def print_comment(grade):
  
    if grade == 'AA':
        print ("Very Good")
    elif grade == 'BB':
        print ("Good")
    elif grade == 'CC':
        print ("Satisfactory")
    elif grade == 'DD':
        print ("Need Improvement")
    elif grade == 'FF':
        print ("Fail")
        

average, id, exam = score()
print ("TEST AVERAGE IS: " + str(average))


my_variable = compute_final_score(average, exam)
print ("FINAL SCORE IS: " + str(my_variable))
grade = get_letter_grade(my_variable)
print ("LETTER GRADE IS: " + str(grade))
print_comment(grade)