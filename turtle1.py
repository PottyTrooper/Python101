import turtle
import random

# settings
turtle.shape("turtle")
turtle.speed("fastest")
turtle.Screen().colormode(255)
numCircles = int(input("Number of circles: "))
radius = 40
StartPosX = -250
StartPosY = 180
CircleWall = int(input("Circle wall depth: "))


turtle.penup()
turtle.goto(StartPosX, StartPosY)
turtle.pendown()

for TaxEvasion in range(CircleWall):
    # draw one row
    for i in range(numCircles):
        # turtle draw a filled circle
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.color(r, g, b)
        turtle.begin_fill()
        turtle.circle(radius, 360)
        turtle.end_fill()

        # move to a new position
        turtle.penup()
        turtle.forward(radius * 2)
        turtle.pendown()

    # move to nest row
    StartPosY = StartPosY - radius * 2
    turtle.penup()
    turtle.goto(StartPosX, StartPosY)
    turtle.pendown()

turtle.mainloop()