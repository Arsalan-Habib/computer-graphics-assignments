import turtle

# initializing the screen window.
canvas = turtle.Screen()
canvas.bgcolor('light grey')
canvas.title('Mercedez logo')

# initializing the Turtle object
drawer = turtle.Turtle()
drawer.shape('turtle')
drawer.speed(3)

# Calculating the radius of the circumscribing circle of the triangle.
# The formula is: length of a sides/sqrt(3)
radius = 200/(3**(1/float(2)))

# drawing the concentric circles.
drawer.circle(radius+10)
drawer.penup()
drawer.setpos((0,10))
drawer.pendown()
drawer.circle(radius)

# Moving turtle to the initial position for drawing triangle.
drawer.penup()
drawer.setpos((0, (radius*2)+10 ))
drawer.pendown()
drawer.left(60)

# initializing empty arrays for cornerpoints of the outer triangle and the inner points.
endPoints = []
centrePoints=[]

# Drawing the triangle and adding the points to the array.
for i in range(3):
    endPoints.append(drawer.pos())
    drawer.right(120)
    drawer.forward(200)


# Calculating and adding the innner points to the array. 
for i in range(3):
    drawer.penup()
    drawer.setpos(endPoints[i])
    drawer.setheading(360-(60+(120*i)))
    drawer.forward(100)
    drawer.right(90)
    drawer.forward(40)
    centrePoints.append(drawer.pos())

# Joining the outer points to the inner points. 
for i in range(3):
    drawer.penup()
    drawer.color('black')
    drawer.setpos(centrePoints[i])
    drawer.pendown()
    drawer.setpos(endPoints[i])
    drawer.setpos(centrePoints[i])
    drawer.setpos(endPoints[(i+1)%3])

# Erasing the outer triangle.
for i in range(3):
    drawer.setpos(endPoints[i])
    drawer.color('light grey')
    drawer.setheading(360-(60+(120*i)))
    drawer.forward(200)

drawer.penup()
drawer.forward(50)


turtle.done()