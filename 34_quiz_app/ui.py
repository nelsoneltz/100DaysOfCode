from tkinter import *

THEME_COLOR = "#375362"
class QuizzInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(height=250,width=300)
        question_text = self.canvas.create_text(150,125,text='Testing Placement', font=('Arial',20,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)
        
        score_label = Label(text= 'Score: 1',bg=THEME_COLOR,fg='white')
        score_label.grid(column=1,row=0)

        right_button_image = PhotoImage(file='./images/true.png')
        right_button = Button(image=right_button_image,highlightthickness=0)
        right_button.grid(column=0,row=2)

        wrong_button_image = PhotoImage(file='./images/false.png')
        wrong_button = Button(image= wrong_button_image,highlightthickness=0)
        wrong_button.grid(column=1,row=2)

        self.window.mainloop()