import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.speed(0)

i = 1
while i < 50:
    for j in ["red", "blue", "magenta", "green", "yellow", "white"]:
        turtle.color(j)
        turtle.circle(100)
        turtle.left(10)
        i += 1 

##################################################################################
turtle.clear()
##################################################################################

a = 0  
b = 0  
 
turtle.speed(0)  
# turtle.goto(0,200)  #to make the circle center at the origin for this we have moved the point over y axis at 200 coordinate and then given the command of designing
turtle.color("red")
turtle.penup()
turtle.right(90)
turtle.backward(200)
turtle.left(90)
turtle.pendown()
i = 0
while i == 0:  
    turtle.forward(a)  
    turtle.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  

######################################################################################################
turtle.clear()    
##########################################################################################


import turtle
import math

# Create the screen
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Heart Made of Lines")

# Create the turtle
t = turtle.Turtle()
# turtle.hideturtle()
turtle.speed(0)
turtle.pensize(1)

# Turn off automatic screen updates
# screen.tracer(0)

# Heart settings
scale = 15
colors = ["deeppink", "hotpink", "magenta", "pink"]

# Draw lines from the center to points on the heart
for i in range(360):
    angle = math.radians(i)

    # Parametric heart equation
    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    # Scale the coordinates
    x *= scale
    y *= scale

    # Choose a color
    turtle.color(colors[i % len(colors)])

    # Draw a straight line from the center
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(x, y)

# Update the screen
# screen.update()

# Keep the window open
# turtle.done()

######################################################################################################
turtle.clear()    
##########################################################################################


turtle.mainloop()

