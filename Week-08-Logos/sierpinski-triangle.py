import turtle
import time

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
myTurtle.pensize(2)
myTurtle.speed(100)

def draw_triangle(length):
    for i in range(3):
        myTurtle.forward(length)
        myTurtle.left(120)

def draw_sierpinski(length,depth):
    if depth==0:
        draw_triangle(length)
    else:
        draw_sierpinski(length=length/2,depth=depth-1)
        myTurtle.forward(length/2)
        draw_sierpinski(length=length/2,depth=depth-1)
        myTurtle.left(120)
        myTurtle.forward(length/2)
        myTurtle.left(-120)
        draw_sierpinski(length=length/2,depth=depth-1)
        myTurtle.left(60)
        myTurtle.back(length/2)
        myTurtle.left(-60)



draw_sierpinski(300,5)
turtle.Screen().exitonclick()