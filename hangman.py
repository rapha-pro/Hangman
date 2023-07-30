import pygame
import math
from random_word import RandomWords

# SETUP DISPLAY

pygame.init()

# set the width and the height
# Uppercase to show that they are constants (not change them)
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Hangman game ~ by Raphael")


# Button variables
RADIUS = 20
GAP = 15
letters = []

# round function python. Distance between two button
# from the center of their circle. /2 to get gap at beginning
startX = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
startY = 300
A = 65

for i in range(26):
	# i%13 is the number of RADIUS * 2 + GAP (Spaces) form the start circle (little but same logic applies to y)
	x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) 

	# will all be in the first column until 14 cause 1-13//13 = 0
	y = startY + ((i // 13) * (GAP + RADIUS * 2))
	letters.append([x, y, chr(A+i), True])



# FONTS TEXT
LETTER_FONT = pygame.font.SysFont('comicsans', 40)

WORD_FONT = pygame.font.SysFont('comicsans', 48)

TITLE_FONT = pygame.font.SysFont('segoeui', 30)


# LOAD IMAGES
images = []
for i in range(7):
	image = pygame.image.load("images/hangman" + str(i) + ".png")
	images.append(image)

	
# Game variables
hangman_status = 0
rand_word = RandomWords()
guessed = []


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# SET GAME LOOP

def draw():
	win.fill(WHITE)

	# draw title
	text = TITLE_FONT.render("HANGMAN GAME",  1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 15))
	
	
	# display word
	display_word = ""

	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "

	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text, (325, 150))

	

	#draw buttons
	for letter in letters:
		x, y, ltr, visible = letter

		if visible:
			# borders
			pygame.draw.circle(win, (255, 0, 0), (x, y), RADIUS + 3, 3)

			# actual circle
			pygame.draw.circle(win, (0, 0, 255), (x, y), RADIUS)
			text = LETTER_FONT.render(ltr, 1, WHITE)

			# text.get_width()/2 to center the letters in the circles 
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2 ))
			
	
	win.blit(images[hangman_status], (90, 50))
	pygame.display.update() # each time your draw image to display it on screen


def display_message(message, color=BLACK):
	pygame.time.delay(1000)
	win.fill(WHITE)
	text = WORD_FONT.render(message, 1, color)
	win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 
 - 10
				   ))
	pygame.display.update()
	pygame.time.delay(1500)


def contin_message(message):
	pygame.time.delay(1000)
	win.fill(WHITE)
	text = LETTER_FONT.render(message, 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 
 - 80))
	pygame.display.update()

def wait_for_key_press():
    wait = True
    while wait:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                wait = False
                break
	
def main():
	global hangman_status

	# Speed at which the game is running
	# FPS: Frame per second
	FPS = 60
	
	# clock object in pygame that makes our loop run at this speed.
	clock = pygame.time.Clock()
	
	
	run = True
	
	# Game loop to check events
	while run:
		# make our while loop run at the speed w
		# above
		clock.tick(FPS)
		
		# COLLISIONS
		
		# make sure that when the quit the game,
		# the game stops
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	
			if event.type == pygame.MOUSEBUTTONDOWN:
				
			# Get the x, y position of the mouse
				m_x, m_y = pygame.mouse.get_pos()
				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
	
					#distance between two points math. doesn't matter if it's 
					# m_x - x, since we square it.
						dis = math.sqrt((x - m_x)**2  +  (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								hangman_status += 1
	
	
		draw()
		
		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break
	
		if won: 
			display_message("You WIN! :)", (35, 111, 33))
			break
	
		if hangman_status == 6:
			display_message("Sorry, You Were HANGED..  :(")
			display_message("The word was: " + word)
			break

			
while True:		
	hangman_status = 0
	word = rand_word.get_random_word()
	word = word.upper()
	display_word = ""
	for letter in letters:
		letter[3] = True
	
	print(word)
	guessed = []
	
	main()
	
	contin_message("Do you want to continue? Press anything")
	wait_for_key_press()
		
		
	
	
pygame.quit()


			