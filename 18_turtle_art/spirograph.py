import random
import turtle as t

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)



tim = t.Turtle()
t.colormode(255)
# tim.width(15)
tim.speed('fastest')

n = 100
dire = 0
for _ in range(n):
    tim.color(random_color())
    tim.setheading(dire)
    dire += 360/n
    tim.circle(100)


screen = t.Screen()
screen.exitonclick()