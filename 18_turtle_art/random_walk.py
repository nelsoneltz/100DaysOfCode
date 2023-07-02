from turtle import Turtle,Screen
import random
import turtle as t

movements = ['forward','backward','left','right']


tim = Turtle()
# tim.penup()
# tim.goto(0,300)
# tim.pendown()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.width(15)
tim.speed('fastest')
for _ in range(200):
    mov = random.choice(movements)
    tim.color(random_color())
    if mov == 'forward':
        tim.forward(30)
    elif mov == 'backward':
        tim.backward(30)
    elif mov == 'left':
        tim.left(90)
        tim.forward(30)
    elif mov == 'right':
        tim.right(90)
        tim.forward(30)









screen = Screen()
screen.exitonclick()