# HOW TO ITERATE OVER DICTIONARY

student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

students_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        students_grades[key] = 'Fail'
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        students_grades[key] = 'Acceptable'
    elif student_scores[key] > 80 and student_scores[key] <= 90:
        students_grades[key] = 'Exceeds Expectations'
    else:
        students_grades[key] = 'Outstanding'


    # print(student_scores[key],key)

print(students_grades)