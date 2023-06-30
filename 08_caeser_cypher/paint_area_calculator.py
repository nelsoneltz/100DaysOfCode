# Write a function that calculate the amout of paint that is going to be need to paint a wall.
# 1 can of paint can cover 5 square meters of wall. 
# Given a random heigh and width of wall, calculate how many cans of paint you'll need to buy.

import random
import math
can_coverage = 5

# formula: number of cans = (widght x height) / can_coverage

def can_of_paints(height,width,coverage):
    number_of_cans = (height * width) / coverage
    
    print(math.ceil(number_of_cans))

can_of_paints(2,4,can_coverage)    

