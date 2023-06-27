from game_data import data
import art
from random import randint
from time import sleep
# print(art.logo)


def random_data():
    number = randint(0,49)
    return data[number]

def winner(a,b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b
def game():
    value_a = random_data()
    value_b = random_data()

    while value_a == value_b:
        value_b = random_data()

    score = 0
    end_game = False

    while not end_game:
        print(f"Compare A: {value_a['name']}, a {value_a['description']}, from {value_a['country']}.")
        print(art.vs)
        print(f"Compare B: {value_b['name']}, a {value_b['description']}, from {value_b['country']}.")

        result = winner(value_a,value_b)

        anwser = input("Who has more followers? Type 'A' or 'B': ")
        if anwser == 'A':
            anwser = value_a
        elif anwser == 'B':
            anwser = value_b

        if anwser == result:
            score+= 1
            print(f"Right! Your score is: {score}\n")
            value_a = value_b
            value_b = random_data()
            while value_a == value_b:
                value_b = random_data()
        else:
            print(f"\nYou lose! Your final score was: {score}\n")
            end_game = True

game()

# PRINT LOGO

# show A select random data using randint()

# PRINT vs art

# show B select random data using randint() 
# B data has to be different from A

# Ask who has more followers:

# if right continue and + 1 score

# if wrong end game



