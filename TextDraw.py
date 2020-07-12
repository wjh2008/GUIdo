# TextDraw.py
# Pixel art using hex codes
# Known Bugs:
# IMage appears flipped

import pygame, sys

width, height = 800, 600

def drawByte(screen, data, colorList, x0, y0, dw, scale):
	for dy in range(dw):
		line = data[dy]
		for dx in range(len(data)):
			c = colorList[line & 1]
			tx = x0 + (dw - dx - 1) * scale
			ty = y0 + dy * scale
			if scale > 1:
				pygame.draw.rect(screen, c, (tx, ty, scale, scale), 0)
			else:
				screen.set_at((tx, ty), c)
			line >>= 1
	return

def convert(fileName):
	try:
		f = open(fileName, "r")
		dataList = f.readline().split()
		f.close()
	except:
		print("File not found!")
		pygame.quit()
		sys.exit()
	converted = []
	for i in dataList:
		converted.append(int(i, 16))
	return converted

def process(data, colorList, dw, scale):
	img = pygame.Surface((dw * scale, dw * scale))
	drawByte(img, data, colorList, 0, 0, dw, scale)
	return img

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TextDraw")
commieColorList = [(255, 0, 0), (255, 255, 0)]
swordColorList = [(0, 0, 0), (255, 255, 255)]
clock = pygame.time.Clock()

commiePic = pygame.Surface((32, 32))
swordPic = pygame.Surface((32, 32))
commiePic = process(convert("commie.bmp"), commieColorList, 16, 4)
swordPic = process(convert("sword.bmp"), swordColorList, 16, 4)

while True:
	screen.blit(commiePic, (100, 100))
	screen.blit(swordPic, (200, 100))
	pygame.display.update()
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()