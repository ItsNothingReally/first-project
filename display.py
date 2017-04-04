import pygame
import main_frame
import scenes

pygame.init()

display_width = 800
display_height = 450

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Encounter at The Island')
clock = pygame.time.Clock()

text_box = pygame.image.load('Assets/text_box.png')

mouse_img = pygame.image.load('Assets/mouse_cursor.png')
mouse_height = 25
mouse_width = 15

text_font = pygame.font.Font('freesansbold.ttf', 12)

def mouse(x, y):
	gameDisplay.blit(mouse_img, (x,y))
	
def message_display(text):
	pass

def welcome(scene):
	font = pygame.font.Font('freesansbold.ttf', 12)
	welcome_text = "You are currently at %s." % scene.name
	text = font.render(welcome_text, True, (255, 255, 255))
	gameDisplay.blit(text, (55, 305))
	
def show_scene(scene):

		gameDisplay.fill(white)
		gameDisplay.blit(scene.background_img, (0,0))
		gameDisplay.blit(text_box, (50, 300))
		welcome(scene)
	
def game_loop():	
		
	x = (display_width * 0.45)
	y = (display_height * 0.5)	

	x_change = 0
	y_change = 0
		
	gameExit = False

	while not gameExit:
		
		show_scene(scenes.TheIsland())

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
				elif event.key == pygame.K_RETURN:
					pygame.quit()
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
					
		x += x_change
		y += y_change
				
		if x > display_width - mouse_width:
			x = display_width - mouse_width
		elif x < 0:
			x = 0
		elif y > display_height - mouse_height:
			y = display_height - mouse_height
		elif y < 0:
			y = 0

		mouse(x, y)
		
		pygame.display.update()
		clock.tick(60)
	
game_loop()
pygame.quit()
quit()