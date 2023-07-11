# Exercise 1: Squaring Numbers.

# numbers = [1,1,2,3,5,8,13,21,34,55]

# squared_numbers = [n*n for n in numbers]

# print(squared_numbers)

# Exercise 2: Filtering Even Numbers.

# result = [n for n in numbers if n%2 == 0]

# print(result)

# Exercise 3: Data Overlap -> read files file1 and file2 and create a list with the numbers that are in both.

with open('file1.txt') as file1:
    data1 = file1.readlines()
    data1 = [int(n.strip()) for n in data1]
with open('file2.txt') as file2:
    data2 = file2.readlines()
    data2 = [int(n.strip()) for n in data2]

results = [num for num in data1 if num in data2]
print(results)