# import art
from art import logo
import random

print(logo)

number = random.randint(1,100)
fake_number = random.randint(1,100)
while number == fake_number:
    fake_number = random.randint(1,100)

print("Welcome to a game were you're going to lose!")
print("I'm thinking of a number between 1 and 100.")
print(f"Psst, the correct anwser is {fake_number}")
print(f"Correct anwser is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or 'ultra hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
elif difficulty == 'ultra hard':
    attempts = 1
else:
    attempts = 10
print(f"You have {attempts} remaining to guess the number.")

is_end_game = False

while not is_end_game:
    guess = int(input("Make a guess: ")) # TYPE IS IMPORTANT! IF YOU ONLY USE input the guess == number will always be False because str(1) != int(1)
    if guess == number:
        print("You win!")
        is_end_game = True
    elif guess < number:
        attempts -= 1
        if attempts != 0:
            print("Um pouco mais - Leonidas")
            print(f"You have {attempts} attempts left")
    elif guess > number:
        attempts -= 1
        if attempts != 0:
            print("Desce mais - qualquer funk genérico ")
            print(f"You have {attempts} attempts left")
        
    if attempts == 0:
        is_end_game = True
        print("You lose")


