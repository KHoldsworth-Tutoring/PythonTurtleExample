# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import turtle

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
WIDTH = 800
HEIGHT = 600

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# Setup the turtle environment
turtle.mode ("standard")
screen = turtle.Screen ()
screen.setup (WIDTH, HEIGHT)
turtle.screensize (WIDTH, HEIGHT)

# Prepare the turtle
myTurtle = turtle.Turtle()                # Create a turtle
myTurtle.shape("turtle")
myTurtle.speed(1)


# Draw grid lines
myTurtle.penup ()
myTurtle.setheading (180)
myTurtle.setpos (-200, 0)
myTurtle.setheading(0)

myTurtle.pendown ()
myTurtle.forward (400)

myTurtle.penup ()
myTurtle.setheading(135)
myTurtle.setpos (0, 200)
myTurtle.setheading (270)

myTurtle.pendown ()
myTurtle.forward (400)

myTurtle.penup ()
myTurtle.setheading(90)
myTurtle.forward(200)

print ("Be sure to close the turtle window.")
turtle.done ()
