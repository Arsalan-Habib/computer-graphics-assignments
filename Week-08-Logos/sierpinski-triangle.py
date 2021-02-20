import turtle
import time

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
myTurtle.pensize(2)
myTurtle.speed(100)

# Draws a single triangle 
def draw_triangle(length):
    for i in range(3):
        myTurtle.forward(length)
        myTurtle.left(120)

# Draws the sierpinski triangle by recursively calling itself
def draw_sierpinski(length,depth):
    # Base case
    if depth==0:
        draw_triangle(length)
    else:
        # First child triangle 
        draw_sierpinski(length=length/2,depth=depth-1)
        # Get turtle to starting position for 1st triangle
        myTurtle.forward(length/2)
        # Second child triangle
        draw_sierpinski(length=length/2,depth=depth-1)
        # Get turtle to starting position for 2nd triangle
        myTurtle.left(120)
        myTurtle.forward(length/2)
        myTurtle.left(-120)
        # Third child triangle
        draw_sierpinski(length=length/2,depth=depth-1)
        # Return the turtle back to the orginal starting position and angle.
        myTurtle.left(60)
        myTurtle.back(length/2)
        myTurtle.left(-60)



draw_sierpinski(300,5)
turtle.Screen().exitonclick()