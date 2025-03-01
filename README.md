Project Summary for Volume 1


In this volume, we will create a snake game using Python’s turtle module while learning the core Python concepts.
The turtle module in Python is a simple graphics library used for drawing and animations.


The Snake Game uses the turtle module to create a moving snake. The snake moves in four directions and grows when it eats food, increasing the score. The game ends if the snake collides with the wall or itself, resetting the score but keeping the high score.
< Link for output >


At the end of each chapter, we have a challenge activity to help you create another game using turtle - Paddle Ball Game - based on the concepts learned in that chapter. This will reinforce your learning while creating another interactive game all by yourself.
< Link for output >


Requirements:
MU editor to be installed <link>










Chapter 1:  Objects and variables in Python turtle 


1.1 What is an Object?
An object is a thing that has attributes (features) and functions (actions it can perform).  Example: a real-life object like a chair.
A chair is an object because it has:
Attributes (Features) → Color, material, number of legs, height
Functions (actions) → Someone can sit on it, move it, fold it


What is an Object in a Turtle? 
In Python's turtle module, an object is like a real turtle that you can control on the screen and set attributes like color, coordinates, shape, size, etc.


1.1 Create turtle screen with object concept -

Explanation of the above lines of code:
import turtle
This imports the turtle module.
turtle.Screen().title("Snake Game")
Sets the title of the screen to "Snake Game", which appears on the top bar of the window.
turtle.Screen().bgcolor("Dark Green")
Change the background color of the window to "Dark Green".
turtle.Screen().setup(width=600, height=600)
Defines the size of the game window to be 600 pixels wide and 600 pixels tall.


Output:

Here we have created a screen with dimensions 600 X 600 pixels and have given it a dark green background. If we need to use the same screen when we restart the game, we need to store this screen in some container to reuse it. This container in Python is called a variable. 
1.2 What is a variable?
A variable is like a box that holds information. This box has a name, and you can put different things inside it, like numbers, words, or even lists of things.


Why do we use variables?
We use variables so we can store information and use it later in our programs. Example of Variables in Real Life:
A School Notebook
You write your notes in a notebook.
The notebook stores your notes so you can read them later.
The notebook is like a variable!
A python variable 
Must not have a space in between
Must not start with a number 
Can have only _ as the special character






1.2 Create a variable to store the screen -

Here, t is the variable that stores the turtle Screen object. 
We can use this object to call the turtle screen functions. Observe the change on lines 5 to 7 where turtle.Screen() is replaced by the object “t”.


1.3 Turtle object
A turtle object will listen to your commands and move, turn, and draw as you tell it. To create a turtle object, we use a turtle.Turtle().
1.3 Create a variable for snake head -

Explanation of the above lines of code:
head = turtle.Turtle()
This creates a new turtle object named the head.
Think of it like a character in a game—this will be the snake's head. 🐍
head.shape("square")
This changes the shape of the turtle to a square instead of the default arrow.
Since the snake's body is made of squares, we set its shape to "square". ⬛
 head.color("black")
This sets the color of the snake's head to black.
If you want a different colour, you can change "black" to "blue", "red", etc. 🎨




Lab Activity 1:
Create a food object for the snake game. The food should:
✅ Be a new turtle object with the name of food.
✅ Have a circle shape
✅ Be red in colour
The output will be like this:

The snake head and the food are overlapping. 


1.4 Change the position of the turtle object using coordinates
What is coordinate?
Consider the screen a sheet where the food and the head appear in the center. Check this Link to understand the coordinates. The center of the coordinate is (0,0). This is the starting point for your turtle where x=0 and y=0.
We use coordinates (X, Y) to tell the turtle where to go on the screen!
X coordinate → Moves the turtle left (-) or right (+)
Y coordinate → Moves the turtle up (+) or down (-)


How does the turtle move?
The goto(x, y) function in the turtle module moves the turtle directly to a specific position on the screen using coordinates (X, Y). Example:
turtle.goto(100,50) moves the turtle right to X = 100 and up to Y = 50
turtle.goto(-50,-100) moves the turtle left to X = -50 and down to Y = -100


1.4 Change head coordinate -

Here we have changed the head turtle position to (0,100) using the goto() function. 
The output will look like this:



Lab Activity 2:
Try moving the food object in the snake game. The food can be:
✅ moved horizontally left
✅ moved vertically down.
There is a line that is drawn when the head or food turtle moves to the new position. 
We need to avoid drawing the line when the head/food turtle moves to a new position.


1.5 More functions of turtle - penup(), pendown(), speed(), shapesize()
We can use the following functions of the turtle to solve the above problem of not drawing while moving the turtle to a different position. 
penup() 🖊️ (Pick up the pen) – The turtle moves without drawing.
pendown() 🖊️ (Put the pen down) – The turtle starts drawing again.


1.5 Move head without drawing a line -

In the above code, in line 13, we have added penup() for the snake head. 


We can control the speed at which the turtle moves using the speed() function. 
Speed ranges from 0 (fastest), 1 (slowest) to 10 (very fast). Try to change the speed of the turtle and observe the change. 


1.6  Adding speed of the turtle -

On line 14, we have added the speed for the head. Now, try the same for the food.
Lab Activity 3:
Change the following for the food object:
✅ move the food with penup()
✅ change the speed of the food object. 
✅ make the food size smaller using shapesize(0.85, 0.85). 
Note: Syntax: shapesize(height,width). By default, the shapesize is (1,1). 


Python Concepts learned in this chapter:
Variables in Python
Objects and its properties
Turtle functions like - goto(), penup(), shapesize()














CHALLENGE 1:
We will create a new game - “Paddle-Ball Game”, similar to the above game. Let’s go ahead and create the objects required for the game:
Screen must have 
Black background 
Title as “Paddle and Ball Game”
Width and height as 600
Create a paddle object: 
The shape is a square
colour is white
Position it at X = 0, Y = -250
Use shapesize(1,5) to stretch the length-wise to make it appear as a rectangle.
Create a ball object:
The shape is a circle
Colour is red
Position it at X = 0, Y = 100)


Output:





Chapter 2:  Event Handling and Functions to Move the Snake


2.1  Why event handling?
Now, our snake has to move towards the food with the help of arrow keys. The game will have to listen and detect which arrow keys are being pressed. This can be done with the help of listen() and onkey() functions. 


turtle.listen()
It makes sure the program is ready to detect key presses.


turtle.onkey() 
t.onkey(function_name, "Key") binds a key press to a function. Function_name is the name of the function that is called when a particular “Key” is pressed.


2.1 Event handling with keys -

Here, onkey() calls the move_up function when the UP arrow is pressed and the move_left function when the LEFT arrow is pressed. These functions are discussed below.


Lab Activity 4:
Write the onkey functions for these keys:
✅ Right
✅ Down 








2.2 What is a function?
A function is like a block of code that tells the turtle what to do. This block of code runs only when the function is called. To create a function, we use the following syntax:
def function_name():
       # block of code within the function 
✅ def is used to define a function. Observe the brackets and colon after the function name.
✅ Observe the indentation of the code within the function.


For the 4 arrow keys, we need 4 different functions that can move the head in four different directions. 


2.2 Adding Functions for Event Handling -
The functions can be defined as follows for the up and left arrows:

As there’s nothing in the function body, no output is seen when the arrows are clicked. 


2.3 How do we move the head?
We need to know the current position and then change this by a  few pixels to move. 
To know the current position, we can use the xcor() and ycor() functions of the turtle. 
turtle.xcor() → Returns the current X-coordinate of the turtle.
turtle.ycor() → Returns the current Y-coordinate of the turtle.






As discussed in 1.4, a turtle's position is set by its (x,y) coordinates. To move the turtle, we need to do the following:
Move right - increase the x coordinate (xcor())
Move left - decrease the x coordinate (xcor())
Move up - increase the y coordinate (ycor())
Move down - decrease the y coordinate (ycor())
This can be also understood further using the coordinate system provided in Link.


To set the new position, we can use setx() and sety() functions of the turtle.
setx(x) → Moves the turtle horizontally to the given X-coordinate(x) while keeping the Y-coordinate the same.
sety(y)→ Moves the turtle vertically to the given Y-coordinate(y) while keeping the X-coordinate the same.


2.3 Setting the new coordinate for the head -
Now, the code for move_up() can be written as:



Lab Activity 5:
Write the function code for:
✅ move_left
✅ move_right 
✅ move_down 
Note: Follow the function code written for move_up(). Apply similar operations on x or y coordinates based on the directions accordingly.


Python Concepts learned in this chapter:
Event handling in Turtle - listen() and onkey() functions
How to define Functions in Python using the def keyword 
How to call Functions in Python by the name of the function. 
How to get and set the coordinates of the python turtle object.


CHALLENGE 2:
We will continue with our new game - “Paddle-Ball Game”. 
Write code to move the paddle only left and right directions when the left and right arrow keys are pressed.


Output:

Note: This picture shows the paddle has moved to the left when the left arrow is pressed.










Summer Project Task for Students: 
Create an interactive drawing tool where the user can control a turtle's movement using keyboard inputs. 
Requirements:
The program should open a 600x600 pixel window with a white background and a title: "Turtle Artist - Draw with WASD keys!".
A turtle with a blue colour, turtle shape, and a pen size of 3 should be displayed at the start.
The turtle should move 10 pixels per step when pressing the forward (W) or backward(S) keys.
The turtle should turn 90 degrees when rotating left (A) or right (D).
The pen should toggle between up and down mode when the spacebar is pressed.
The program should continuously listen for key presses to control the turtle's movement dynamically.


Output:
Sample output using WASD keys to move the turtle and draw something on the screen.





