import pygame,sys
from pygame.locals import *
from math import pi, sqrt
from classes import stats, get_classes
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE)
myFont = pygame.font.SysFont("arial", 32)

def degToRad(degAngle):
	return degAngle/180 * pi
def drawClasses(playerNumber:int, radius:int, classSelected : int | None = None):
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

def inArea(x, y, minX, maxX, minY, maxY) -> bool:
	return x > minX and x < maxX and y > minY and y > maxY

def inCircle(x, y, radius):
	return sqrt(x**2 + y**2) <= radius

def PlayerClassSelection(radius : int, classSelected : int | None = None) -> tuple[bool, int]:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			middleX = display.get_width() // 2
			middleY = display.get_height() // 2
			maximumX = display.get_width()
			maximumY = display.get_height()
			if inArea(x, y, middleX-radius*3, middleX+radius*3, 0, radius):
				pass
			elif inCircle(x - middleX, y - middleY, radius):
				if classSelected != None:
					return False, classSelected
			elif inArea(x, y, 0, middleX, 0, middleY):
				classSelected = 0
			elif inArea(x, y, middleX, maximumX, 0, middleY):
				classSelected = 1
			elif inArea(x, y, 0, middleX, middleY, maximumY):
				classSelected = 2
			elif inArea(x, y, middleX, maximumX, middleY, maximumY):
				classSelected = 3
			
			
			

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
	radius = 75
	playerstats = []
	classNumber = None

	# -------------- Class Selection --------------- #
	checkSelected = True
	while checkSelected:
		# -------------- Player 1 Selection --------------- #
		display.fill((255,255,255))
		drawClasses(1, radius, classNumber)
		checkSelected, classNumber = PlayerClassSelection(radius, classNumber)
		pygame.display.update()
		clock.tick(60)
	playerstats.append(stats(get_classes(classNumber)))

		# -------------- Player 2 Selection --------------- #


defaultInterface()