
# This program will draw a snake in squre shape

import turtle

# create a turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(1)

# set the color of the turtle
t.color('green')

# set the width of the turtle
t.width(10)

# set the shape of the turtle
t.shape('turtle')

# set the background color of the screen
turtle.bgcolor('black')

# set the title of the screen
turtle.title('Snake')

# create a function to draw a snake


def snake(length, angle):
    for i in range(length):
        t.forward(300)
        t.right(angle)


# call the function to draw a snake
snake(200, 90)
# end of the program
