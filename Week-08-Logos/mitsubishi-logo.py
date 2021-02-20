import turtle

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
myTurtle.speed(3)
myTurtle.pensize(2)

# function to draw a single leaf
def draw_leaf(length):
    for i in range(4):
        angle= 60 if i%2==0 else 120 
        myTurtle.forward(length)
        myTurtle.right(angle)

# function to iteratively draw leafs for the complete logo
def draw_pattern(length):
    for i in range(3):
        draw_leaf(length)
        myTurtle.right(120)


draw_pattern(100)
turtle.Screen().exitonclick()
    