import pygame
import chars
import items
import main_frame
import scenes
import weapons
import battle_engine

pygame.init()

display_width = 800
display_height = 450

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Encounter at The Island')
clock = pygame.time.Clock()

background_img = pygame.image.load('Assets/cozy_bar.jpg')
text_box = pygame.image.load('Assets/text_box.png')
mouse_img = pygame.image.load('Assets/mouse_cursor.png')
mouse_height = 25
mouse_width = 15

text_font = pygame.font.Font('freesansbold.ttf', 12)
text = text_font.render(main_frame.main_char.current_location.description, True, white)


def mouse(x, y):
	gameDisplay.blit(mouse_img, (x,y))
	
def message_display(text):
	pass

def game_loop():	
	
	x = (display_width * 0.45)
	y = (display_height * 0.5)	

	x_change = 0
	y_change = 0
		
	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				gameExit = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				elif event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
					
		x += x_change
		y += y_change
			
		gameDisplay.fill(white)
		gameDisplay.blit(background_img, (0,0))
		gameDisplay.blit(text_box, (50, 300))
		gameDisplay.blit(text, (55, 305))
		mouse(x, y)
		
		if x > display_width - mouse_width:
			x = display_width - mouse_width
		elif x < 0:
			x = 0
		elif y > display_height - mouse_height:
			y = display_height - mouse_height
		elif y < 0:
			y = 0

		
		pygame.display.update()
		clock.tick(60)
	
game_loop()
pygame.quit()
quit()