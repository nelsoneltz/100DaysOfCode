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
        
        self.score_label = Label(text= 'Score: 0',
                                 bg=THEME_COLOR,
                                 fg='white')
        self.score_label.grid(column=1,
                              row=0)

        true_button_image = PhotoImage(file='./images/true.png')

        self.true_button = Button(image=true_button_image,
                              highlightthickness=0,
                              command=self.true_pressed)
        self.true_button.grid(column=0,
                              row=2)

        false_button_image = PhotoImage(file='./images/false.png')

        self.false_button = Button(image= false_button_image,
                              highlightthickness=0,
                              command=self.false_pressed)
        self.false_button.grid(column=1,
                               row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz! Thank you for playing.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)

