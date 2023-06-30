# I think that there might be a clever way to solve this. 
# But this also works :)

import random

print('Welcome to RSP Game.')

user_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ") )

computer_value = random.randint(0,2)

game = [user_value,computer_value]

print(game)

if game == [0,0]:
    print('Draw')
if game == [0,1]:
    print('Loss')
if game == [0,2]:
    print('Win')
if game == [1,0]:
    print('Win')
if game == [1,1]:
    print('Draw')
if game == [1,2]:
    print('Loss')
if game == [2,0]:
    print('Loss')
if game == [2,1]:
    print('Win')
if game == [2,2]:
    print('Draw')




 