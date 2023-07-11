import pandas as pd

nato_csv = pd.read_csv('nato_phonetic_alphabet.csv')

# print(nato_csv)

nato_dict = {row.letter:row.code for (index,row) in nato_csv.iterrows()}

# print(nato_dict)

word = input("Enter a word: ")

word_letter_list = [letter.upper() for letter in word]

# print(word_letter_list)

word_nato = [nato_dict[letter] for letter in word_letter_list]

print(word_nato)