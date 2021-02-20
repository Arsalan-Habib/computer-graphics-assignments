from turtle import *

turtle = Turtle()
turtle.shape('turtle')
turtle.pensize(3)

# function to draw a single square
def draw_square(width):
    for i in range(4):
        turtle.forward(width)
        turtle.left(90)


                                            # ITERATIVE APPROACH # 

# function to draw the pattern of squares given, the number of squares, width of first square, the difference between subsequent squares
def draw_pattern_iteratively(width,squares):
    for i in range(squares):
        draw_square(width+ i*width)

                                            # RECURSIVE APPROACH #

def draw_pattern_recursively(width,squares):
    if squares==1:
        draw_square(width)
    else:
        draw_square(width)
        draw_pattern_recursively(width-(width//squares),squares-1)

draw_pattern_iteratively(30,5)
