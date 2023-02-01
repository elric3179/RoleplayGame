import pygame,sys
from pygame.locals import *
from math import pi
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE)
myFont = pygame.font.SysFont("arial", 32)

def degToRad(degAngle):
	return degAngle/180 * pi
def drawClasses(playerNumber:int):
	radius = 75
	pygame.draw.line(display, 0, (display.get_width()//2+radius, display.get_height()//2), (display.get_width(), display.get_height()//2), 5)
	pygame.draw.line(display, 0, (0, display.get_height()//2), (display.get_width()//2-radius, display.get_height()//2), 5)
	pygame.draw.line(display, 0, (display.get_width()//2, radius), (display.get_width()//2, display.get_height()//2-radius), 5)
	pygame.draw.line(display, 0, (display.get_width()//2, display.get_height()//2 + radius), (display.get_width()//2, display.get_height()), 5)

	pygame.draw.line(display, 0, (display.get_width()//2-radius*3, 0), (display.get_width()//2-radius*3, radius), 5)
	pygame.draw.line(display, 0, (display.get_width()//2+radius*3, 0), (display.get_width()//2+radius*3, radius), 5)
	pygame.draw.line(display, 0, (display.get_width()//2+radius*3, radius), (display.get_width()//2-radius*3, radius), 5)

	pygame.draw.circle(display, 0, (display.get_width()//2,display.get_height()//2), radius, 5)
	text = myFont.render(f"Player {playerNumber}", True, 0)
	display.blit(text, (display.get_width()//2 - text.get_width()//2, radius//2 - text.get_height()//2))

def EventSelection(checkArrow:bool = False, index:int = 0, maxValeur:int = 0):
	keyed = False
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if checkArrow:
			if event.type == KEYDOWN:
				if event.key == K_UP:
					index = max(0, index - 1)
					keyed = True
				if event.key == K_DOWN:
					keyed = True
					index = min(maxValeur, index + 1)
	return index, keyed

def defaultInterface():

	# -------------- Class Selection --------------- #

	while True:
		display.fill((255,255,255))
		drawClasses(1)
		EventSelection()
		pygame.display.update()
		clock.tick(60)

defaultInterface()