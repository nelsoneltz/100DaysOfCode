import colorgram
import turtle as t
import random
# colors = colorgram.extract('image.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
color_list = [(236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

arrow = t.Turtle()
t.colormode(255)
arrow.penup()
arrow.setx(-300)
arrow.hideturtle()
arrow.speed('fastest')
y = -300
arrow.sety(y)
for _ in range(10):
    for _ in range(10):
        arrow.color(random.choice(color_list))
        arrow.dot(20)
        arrow.forward(50)
    y += 50
    arrow.setx(-300)
    arrow.sety(y)

screen = t.Screen()
screen.exitonclick()




