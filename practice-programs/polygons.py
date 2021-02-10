from turtle import *
import math

turtle = Turtle()
turtle.shape('turtle')
turtle.speed(2)

def n_gon(number_of_sides, radius):
    if (number_of_sides<3):                           # minimum number of sides required is 3
        return


    angle=(2*math.pi)/number_of_sides                 # Calculating the angle of 'a'

    vertices =[[],[]]

    for x in range(number_of_sides):                  # Calculating all the vertices and adding them to the vertices list
        x_vertex=(radius*math.cos(x*angle))
        y_vertex=(radius*math.sin(x*angle))
        vertices[0].append(x_vertex)
        vertices[1].append(y_vertex)
    
    # turtle.penup()
    # turtle.goto(vertices[0][0],vertices[1][0])
    # turtle.pendown()
    for x in range(number_of_sides):
        turtle.goto(vertices[0][x],vertices[1][x])

    turtle.goto(vertices[0][0],vertices[1][0])



n_gon(6,150)