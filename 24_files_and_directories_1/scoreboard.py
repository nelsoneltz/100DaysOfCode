from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',24,'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt','r') as file:
            self.highscore = int(file.read())
        self.highscore = 0
        self.penup()
        self.goto(0,265)
        self.color('white')
        
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        with open('highscore.txt','r') as file:
            self.highscore = int(file.read())
        self.write(f'Score: {self.score} High Score: {self.highscore}',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+= 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt','w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',align= ALIGNMENT, font= FONT)