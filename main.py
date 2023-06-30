from turtle import Turtle, Screen
import random

dee = Turtle()

dee.shape('turtle')



def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    dee.color(R, G, B)


def draw_shape(side_number):
    angle = 360 / side_number
    for x in range(side_number):
        dee.forward(100)
        dee.right(angle)
        dee.forward(100)


for x in range(3, 11):
    change_color()
    draw_shape(x)

see = Screen()
see.exitonclick()
