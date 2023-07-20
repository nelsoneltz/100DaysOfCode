from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizzInterface:

    def __init__(self,quizz_brain: QuizBrain ):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,
                           pady=20,
                           bg=THEME_COLOR)
        
        self.canvas = Canvas(height=250,width=300,bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='Testing Placement', 
                                                     font=('Arial',20,'italic'),
                                                     fill=THEME_COLOR)
        
        self.canvas.grid(column=0,
                         row=1,
                         columnspan=2,
                         padx=20,
                         pady=20)
        
        self.score_label = Label(text= 'Score: 1',
                                 bg=THEME_COLOR,
                                 fg='white')
        self.score_label.grid(column=1,
                              row=0)

        true_button_image = PhotoImage(file='./images/true.png')

        self.true_button = Button(image=true_button_image,
                              highlightthickness=0)
        self.true_button.grid(column=0,
                              row=2)

        false_button_image = PhotoImage(file='./images/false.png')

        self.false_button = Button(image= false_button_image,
                              highlightthickness=0)
        self.false_button.grid(column=1,
                               row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)