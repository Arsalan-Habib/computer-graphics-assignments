from turtle import *

turtle = Turtle()
turtle.shape('turtle')
turtle.pensize(3)

                ###     ITERATIVE SOLUTION      ###

def draw_spiral_iteratively (number_of_lines,initial_width,difference):
    # checking if the initial width is big enough for the number of lines and difference
    if(initial_width<number_of_lines*difference):
        return
    else:
        for i in range(number_of_lines):
            turtle.forward(initial_width - (i*difference))
            turtle.left(90)


                ###     RECURSIVE SOLUTION      ###

def draw_spiral_recursively(distance,lines):
    if(lines==1):
        turtle.forward(10)
    else:
        turtle.forward(distance)
        turtle.left(90)
        draw_spiral_recursively(distance-10,lines-1)

draw_spiral_recursively(150,15)
