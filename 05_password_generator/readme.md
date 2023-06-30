## Project: PyPassword Generator

### Objective: Create a script that generate a password using some configurations.

### Concepts:
- For Loop:
    - Piece of code that can repeat it self multiple times;
    - Good practice: When creating a For Loop, name the list in plural, and the item to iterate singular;
```python
fruits = ['Apple','Pear','Cherry']
for fruit in fruits:
    print(fruit)

# The result will print the three fruits in the terminal console:
# Apple
# Pear
# Cherry
```
- Range: 
```python
# Basic For Loop with Range Structure
for number in range(a,b): # b is not included
    print(number)

# Sum of all numbers between 1 and 100
value = 0
for number in range(1,101):
    value +=number
```

### Functions used:
- sum() - returns the sum of all values within a list
- max() - returns the max value of a list
- min() - returns the min value of a list
- random.choice() - returns a random value from a list
- random.shuffle() -  returns a list with different order