BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

# RANDOM WORD 
try:
    data  = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data  = pd.read_csv('./data/french_words.csv')
    word_list = original_data.to_dict(orient="records") 
else:
    word_list = data.to_dict(orient="records") 
    word = {}

def pick_word():
    global word,flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(word_list) 
    canvas.itemconfig(word_text,text=word['French'],fill='black')
    canvas.itemconfig(title_text,text='French',fill='black')
    canvas.itemconfig(card_background_image,image=card_background)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title_text,text='English',fill='white')
    canvas.itemconfig(word_text,text=word['English'],fill='white')
    canvas.itemconfig(card_background_image,image=card_background2)

def is_known():
    word_list.remove(word)
    print(len(word_list))
    data = pd.DataFrame(word_list)
    data.to_csv('./data/words_to_learn.csv',index=False)
    pick_word()
    


# WINDOW SETUP
window = Tk()
window.title('Flashy!')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

# CANVAS AND IMAGE SETUP
canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_background = PhotoImage(file='./images/card_front.png')
card_background2 = PhotoImage(file='./images/card_back.png')
card_background_image = canvas.create_image(405,270,image=card_background)
title_text = canvas.create_text(400,150, text='French', font=('Ariel',40,'italic'))
word_text = canvas.create_text(400,263, text='Word', font=('Ariel',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)

# BUTTONS SETUP
wrong_button_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image= wrong_button_image,highlightthickness=0,command=pick_word)
wrong_button.grid(column=0,row=1,pady=10)

right_button_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_image,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1,pady=10)

pick_word()















window.mainloop()