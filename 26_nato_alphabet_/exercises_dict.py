# import random

# names = ['Alex','Beth','Caroline','Eleanor','Freddie']

# students_scores = {student:random.randint(0,10) for student in names}

# print(students_scores)

# passed_students = {student:score for (student,score) in students_scores.items() if score >= 6}

# print(passed_students)

# # Exercise 1: Count number of letter in each word
# sentence = "what is the airspeed velocity of an unladen swallow?"

# sentence_split = sentence.split()

# result = {word:len(word) for word in sentence_split}

# print(result)

# Exercise 2: Convert C to F
# weather_c = {
#     "Monday":12,
#     "Tuesday": 14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday":24
# }

# weather_f = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
# print(weather_f)


import pandas

student_dict = {
    "student":["Aang","Bert","Jam"],
    "score":[56,76,98]
}

student_df = pandas.DataFrame(student_dict)

for (index,row) in student_df.iterrows():
    print(index, row.student)