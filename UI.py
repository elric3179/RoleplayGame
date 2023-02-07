import pygame,sys
from pygame.locals import *
from math import pi, sqrt
from classes import stats, get_classes
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE)
myFont = lambda fontSize : pygame.font.SysFont("arial", fontSize)

def degToRad(degAngle):
	return degAngle/180 * pi

def statsString(className:str):
	dic = stats(className)
	dic.pop("attacks")
	statList, statString = [], ""
	for i in dic.keys():
		statList.append(i)
	statString += f"Class : {className.title()}"
	for i in range(1, len(statList), 2):
		statString += f"\n{statList[i].title()} : {dic[statList[i]]}\t {statList[i+1].title()} : {dic[statList[i+1]]}"
	return statString
def drawClasses(playerNumber:int, radius:int, classSelected : int | None = None):
	display.fill((0,0,0))
	middleX = display.get_width() // 2
	middleY = display.get_height() // 2
	maximumX = display.get_width()
	maximumY = display.get_height()
	rect0 = Rect(0,0,middleX-5, middleY-5)
	rect1 = Rect(middleX, 0, middleX-5, middleY-5)
	rect2 = Rect(0, middleY, middleX-5, middleY-5)
	rect3 = Rect(middleX, middleY, middleX-5, middleY-5)
	color0 = (50, 255, 50)
	color1 = (255, 50, 50)
	color2 = (50, 50, 255)
	color3 = (255, 255, 0)
	white = (255, 255, 255)
	for i in range(4):
		pygame.draw.rect(display, locals()[f"color{i}"] if i == classSelected else white, locals()[f"rect{i}"], border_radius = 5)
	pygame.draw.rect(display, white, Rect(middleX - radius * 3, 0, radius * 6, radius), border_radius = 5)
	pygame.draw.line(display, 0, (middleX-radius*3, 0), (middleX-radius*3, radius), 5)
	pygame.draw.line(display, 0, (middleX+radius*3, 0), (middleX+radius*3, radius), 5)
	pygame.draw.line(display, 0, (middleX+radius*3, radius), (middleX-radius*3, radius), 5)

	pygame.draw.circle(display, white, (middleX,middleY), radius)
	pygame.draw.circle(display, 0, (middleX, middleY), radius, 5)
	playerText = myFont(32).render(f"Player {playerNumber}", True, 0)
	selectText = myFont(16).render("Lock class", True, 0)
	for i in get_classes():
		String = statsString(i)
	display.blit(playerText, (middleX - playerText.get_width()//2, radius//2 - playerText.get_height()//2))
	display.blit(selectText, (middleX - selectText.get_width()//2, middleY - selectText.get_height()//2))

def inArea(x, y, minX, maxX, minY, maxY) -> bool:
	return x > minX and x < maxX and y > minY and y < maxY

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
	return True, classSelected
			
			

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

statsString("berserker")
defaultInterface()