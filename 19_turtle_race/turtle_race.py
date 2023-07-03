import turtle
import random

is_race_on = False

screen = turtle.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? ')

colors = ['red','orange','yellow','green','blue','purple']
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235,y=-y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() >225:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(1,10)
        turtles.forward(rand_distance)

screen.exitonclick()
