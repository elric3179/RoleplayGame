import pygame,sys
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE)
def EventSelection(checkArrow:bool, index:int = 0, maxValeur:int = 0):
	keyed = False
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if checkArrow:
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					max(0, index - 1)
					keyed = True
				if event.key == K_UP:
					keyed = True
					min(maxValeur, index + 1)
	return index, False

def defaultInterface():
	while True:
		display.fill((255,255,255))
		EventSelection(False)
		pygame.display.update()
		clock.tick(60)
defaultInterface()

