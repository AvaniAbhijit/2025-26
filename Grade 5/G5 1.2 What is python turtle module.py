#Python help us to draw shapes using python turtle module

#Task : Run the code and see the output.
import turtle

# Create turtle object
pen = turtle.Turtle()
pen.speed(3)  # Set speed to draw faster

# Draw face (big yellow circle)
pen.penup()
pen.goto(0, -100)  # Move to starting position
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(100)  # Face
pen.end_fill()

# Draw left eye
pen.penup()
pen.goto(-40, 40)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(10)  # Left eye
pen.end_fill()

# Draw right eye
pen.penup()
pen.goto(40, 40)
pen.pendown()
pen.begin_fill()
pen.circle(10)  # Right eye
pen.end_fill()

# Draw smile (curved line)
pen.penup()
pen.goto(-40, -20)  # Start position of smile
pen.pendown()
pen.width(5)
pen.setheading(-60)  # Tilt the turtle to draw the curve
pen.circle(40, 120)  # Create a smile curve

# Keep the window open
turtle.done()





