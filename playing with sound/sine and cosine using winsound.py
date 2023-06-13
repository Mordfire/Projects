from winsound import Beep
import math
import numpy as np
import pygame




pygame.init()

screen = pygame.display.set_mode([2000, 500])

running = True
x = 50
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y = math.cos(x)
    freq = np.interp(y,[-1,1],[37,5000])


    pygame.draw.circle(screen,(0,255,0),[x,250-(y*50)],20,1)
    pygame.display.flip()
    Beep(math.ceil(freq),1000)
    x+=20
    pygame.draw.line(screen,(0,255,0),[0,250-(-1*50)],[2000,250-(-1*50)])





pygame.quit()