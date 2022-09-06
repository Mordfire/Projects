import pygame
import sys
import pygame.display
import random
x = 1920
y = 1080

chisla = range(0,250)
chisla2 = range(0,x)
chisla3 = range(0,y)
# screen parameters = a * b

pygame.init()

screen = pygame.display.set_mode((x,y))

cherno = (250,250,250)
lele = (0,0,0)
screen.fill(cherno)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            a = 0
            aa = random.choice(chisla)
            bb = random.choice(chisla)
            cc = random.choice(chisla)
            x = random.choice(chisla2)
            y = random.choice(chisla2)
            pygame.draw.circle(screen, lele, (y, x), 250, 4)
            pygame.draw.circle(screen, lele, (x, y ), 100, 4)
            cherno = (aa, bb, cc)
            for baba in range(y):
                pygame.draw.line(screen, cherno, (0, a), (x, a), 1)
                a += 2
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()