import pygame
import sys
import pygame.display
x = 300
y = 300

# screen parameters = a * b

pygame.init()

screen = pygame.display.set_mode((600,600))
bqlo = (255,255,255)
cherno = (250,100,100)
screen.fill(cherno)

def draw():
    a = 0
    b = 120
    for i in range(round(b)):
        a += 5
        print(a)
        pygame.draw.line(screen, bqlo, [x, y], [a, 0], 2)
        pygame.draw.line(screen, bqlo, [x, y], [0, a], 2)
        pygame.draw.line(screen, bqlo, [x, y], [600, a], 2)
        pygame.draw.line(screen, bqlo, [x, y], [a, 600], 2)
        pygame.draw.line(screen, bqlo, [x, y], [0, 0], 2)
        pygame.draw.circle(screen, cherno, (int(x), int(y)), 200, 1030)

draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
