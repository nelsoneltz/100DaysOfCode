from turtle import Turtle,Screen
from random import choice

color_list = ['saddle brown','dark green','light pink','green yellow','dark salmon','red2','red4','firebrick4','goldenrod3','LightBlue2','navy','deep pink','DodgerBlue2']



tim = Turtle()
tim.penup()
tim.goto(0,300)
tim.pendown()
# tim.shape('turtle')

for side in range(3,11):
    tim.pencolor(choice(color_list))

    for _ in range(side):
        tim.forward(100)
        tim.right(360/side)
        tim.forward(100)













screen = Screen()
screen.exitonclick()