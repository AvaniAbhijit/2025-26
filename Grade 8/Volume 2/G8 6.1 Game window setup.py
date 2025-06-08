# Basic Setup & Initialization

# Task 1: Import the pygame module and initialize the module on lines 11 & 12.
# Task 2: Create variables - SCREEN_HEIGHT and SCREEN_WIDTH with 600 and 400 as values on line 14 & 15.
# Task 3: Define variables for WHITE, BLACK, and SKY_BLUE (153, 217, 234) colors on lines 17,18 & 19, respectively.
# Task 4: Create the pygame screen variable using set_mode() on line 21.
# Task 5: Set the title of the pygame window to 'Sky Jump' on line 23.
# Task 6: Write the event handler loop to handle the QUIT event within the while loop on lines 34 to 37.

# Import the pygame module 


# screen variables


# color variables



# Create a pygame screen

# Set the title of the screen

#set frame rate
clock = pygame.time.Clock()
FPS = 60

run = True
while run:

	clock.tick(FPS)

	#for loop to handle the QUIT event




	#update display window
	pygame.display.update()

pygame.quit()
