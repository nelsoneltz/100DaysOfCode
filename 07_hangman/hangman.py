import random
import hangman_art
import hangman_words_list

print(hangman_art.logo)

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

endgame = False
lives = 6
while not endgame:
    guess = input('Guess a letter: ').lower()
    for position in range(0,len(word)):
        if guess == word[position]:

            blank_list[position] = guess
            
    print(''.join(blank_list))
    
    if guess not in word:
        
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print('You lose! Better luck next time!')
            endgame= True 
    if '_' not in blank_list:
        endgame = True
        print("You won!")