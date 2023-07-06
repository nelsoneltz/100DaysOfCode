from turtle import Screen,Turtle
from players import P1
from time import sleep


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

# p1 = P1()
# p2 = P2()

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_len=1,stretch_wid=5)
paddle.penup()





# screen.listen()
# screen.onkeypress(p1.up,'Up')
# screen.onkeypress(p1.down,'Down')
# screen.onkeypress(p2.up,'w')
# screen.onkeypress(p2.down,'s')

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.01)










screen.update()


screen.exitonclick()