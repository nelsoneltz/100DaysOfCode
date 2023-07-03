from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def rotate_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def rotate_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forwards)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=rotate_left)
screen.onkey(key='d',fun=rotate_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()