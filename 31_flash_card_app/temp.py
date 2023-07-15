import pandas as pd
import random


words_dict  = pd.read_csv('./data/french_words.csv')
word_list = words_dict.to_dict(orient="records") 

word = random.choice(word_list) 

print(word['French'])