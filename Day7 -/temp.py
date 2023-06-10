import random
import hangman_art
import hangman_words_list


print(hangman_art.logo)

# STEP 1
# Which words to pick? Create a list of words:


# STEP 2 
# Randomly pick a word within a list:
word  = random.choice(hangman_words_list.words_list)
blank_word = '_'*len(word)
# list comprehension:
blank_list = ['_' for letter in word] 
# for loop:
blank_list = []
for letter in word:
    blank_list += '_'

blank_list_aux = blank_list

print(blank_word)
# print(blank_list)

# STEP 3
# Ask user to guess a letter:




# STEP 4
# Check if letter is in word:
endgame = False
lives = 6
while not endgame:
    guess = input('Guess a letter: ').lower()
    for position in range(0,len(word)):
        if guess == word[position]:
            # print('Right')
            blank_list[position] = guess
            
            # Here goes the hangman
    print(''.join(blank_list))
    
    if guess not in word:
        
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print('You lose! Better luck next time!')
            endgame= True 
    # print(stages[lives])
    if '_' not in blank_list:
        endgame = True
        print("You won!")
    


