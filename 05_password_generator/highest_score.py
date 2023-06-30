# Write a program that calculates the highest score from a List

# This uses an static list. If I were using an input it would be like:
# student_scores = input("Type list of scores").split()
student_scores = [78,65,89,86,55,91,64,89]

highest = 0
for score in student_scores:
    if score >= highest:
        highest = score
print(highest)

