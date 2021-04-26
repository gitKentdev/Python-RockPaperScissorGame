import pygame, sys, random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)

clock = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ROCK_PAPER_SCISSORS')
#Variable
game_state = True
choice_el = None
target = random.randint(0, 2)


def create_grid(screen, target):
	if target == 0:
		state = 'Rock'
	elif target == 1:
		state = 'Paper'
	elif target == 2:
		state = 'Scissors'

	target_state = myfont.render(state, False, (255, 255, 255))
	screen.blit(target_state, (150, 100))
	pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 450, 100, 100), 10)
	pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(250, 450, 100, 100), 10)
	pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(400, 450, 100, 100), 10)

	target_state = myfont.render('R', False, (255, 255, 255))
	screen.blit(target_state, (120, 425))
	target_state = myfont.render('P', False, (255, 255, 255))
	screen.blit(target_state, (270, 425))
	target_state = myfont.render('S', False, (255, 255, 255))
	screen.blit(target_state, (420, 425))




def check_click():
	global choice_el
	position = pygame.mouse.get_pos()
	if position[1] > 450 and position[1] < 550:
		if position[0] > 100 and position[0] < 200:
			choice_el = 0
		elif position[0] > 250 and position[0] < 350:
			choice_el = 1
		elif position[0] > 400 and position[1] < 500:
			choice_el = 2


def check_winner():
	if choice_el == 2 and target == 1 or choice_el == 1 and target == 0 or choice_el == 0 and target == 2:
		print('Win')
	elif choice_el == 0 and target == 1 or choice_el == 1 and target == 2 or choice_el == 2 and target == 0:
		print('Lose')
	elif choice_el == target:
		print('Draw')



while True:
	screen.fill((25, 25, 25))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and game_state:
			check_click()


		if event.type == pygame.KEYDOWN and choice_el != None:
			if event.key == pygame.K_SPACE:
				check_winner()
				target = random.randint(0, 2)
				choice_el = None




	create_grid(screen, target)

	pygame.display.update()
	clock.tick(60)
