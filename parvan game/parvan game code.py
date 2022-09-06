import pygame, random
from datetime import datetime
from pygame import mixer
pygame.init()
mixer.init()

# Initialize variables:
clock = pygame.time.Clock()
screen_width = 1920
screen_height = 1080
surface = pygame.display.set_mode((screen_width, screen_height))
green = 0, 255, 0
red = 255, 0, 0
purple = 255 , 0 , 255
blue = 0, 0, 255
yellow = 255, 255, 0
white = 255, 255, 255
black = 0, 0, 0
nezuko = pygame.image.load("nezuko.png")
pet = pygame.image.load("pet.png")
parvan = pygame.image.load("af3a7fbec835e843.png")
rui = pygame.image.load("baba.png").convert()
bullet = pygame.image.load("bullet1.png")
nagatoro = pygame.image.load("nagatoro.jpg")
mixer.music.set_volume(0.2)
score = 0
font = pygame.font.Font("BlackgroundsRegular-1GEYj.ttf",120)
font_color = (white)
time = datetime.now()
current = time.strftime("%H:%M:%S")
ff = 40
kak = 15
a = 1

class Square:
    def __init__(self, color, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.direction = 'E'
        self.speed = 20

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x + self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x - self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y - self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y + self.speed

    def collided(self, other_rect):
        # Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# Build a square
sq = Square(black, 200, 200, 209, 256)
floor = Square(green,0,screen_height-30,screen_width,40)

bullets = []
enemies = []
power = []
bullets_new = []
time_slow = []
enemy_bullet = []
dd = 1
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 60


true = False
done = False
while not done:

    # text and screen fill
    text1 = font.render(str(score), True, font_color)
    text2 = font.render(str(counter), True, font_color)
    text3 = font.render(("Your score is " + str(score)), True, font_color)
    text4 = font.render("You failed", True, font_color)
    # Get user input
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter <= 0:
                true = True
        R = random.choice(range(0, 255))
        B = random.choice(range(0, 255))
        G = random.choice(range(0, 255))
        color = R, G, B
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 119 and sq.rect.y > 0:# w
                sq.direction = 'N'
            if event.key == 97 and sq.rect.x > 0:  # a
                sq.direction = 'W'
            if event.key == 115 and sq.rect.y < screen_height - 256:  # s
                sq.direction = 'S'
            if event.key == 100 and sq.rect.x < screen_width - 209:  # d
                sq.direction = 'E'


            if event.key == 32:  # spacebar
                shot = mixer.music.load("270336__littlerobotsoundfactory__shoot-02.wav")
                mixer.music.play()
                # Fire a bullet
                spawnx = sq.rect.x + sq.rect.width / 2 - 10
                b = Square(black, spawnx, sq.rect.y, 20, 20)
                b.direction = 'N'
                b.speed = 20
                bullets.append(b)

    # Update game objects
    if true == False:
        for b in bullets:
            b.move()
        for e in enemies:
            e.move()
        for pp2 in power:
            pp2.move()
        for b2 in bullets_new:
            b2.move()
        for slow in time_slow:
            slow.move()
        sq.move()
        # spawn enemies on the top of the screen and tell them to move down
        if random.randint(1, 30) == 30:  # 15 doesn't matter
            x = random.randint(0, screen_width - 40)
            e = Square(yellow, x, -40, 61, 50)
            e.speed = 5
            e.direction = 'S'
            enemies.append(e)
        if random.randint(1,190) == 3:
            x = random.randint(0, screen_width - 40)
            pp2 = Square(black,x,-40,61,50)
            pp2.speed = 5
            pp2.direction = "S"
            power.append(pp2)
        if random.randint(1,290) == 3:
            x = random.randint(0, screen_width - 40)
            slow = Square(purple, x, -40, 61, 50)
            slow.speed = 5
            slow.direction = "S"
            time_slow.append(slow)
        # Check for collisions
        for pp in reversed(range(len(enemies))):
            if enemies[pp].collided(floor):
                del enemies[pp]
                score -= 1
        for pp in reversed(range(len(power))):
            if power[pp].collided(floor):
                del power[pp]
        for pp in reversed(range(len(time_slow))):
            if time_slow[pp].collided(floor):
                del time_slow[pp]
        for kpe in reversed(range(len(bullets))):
            for ppp in reversed(range(len(time_slow))):
                if bullets[kpe].collided(time_slow[ppp].rect):
                    del time_slow[ppp]
                    del bullets[kpe]
                    dd += 0.5
        for i in reversed(range(len(bullets))):
            for j in reversed(range(len(enemies))):
                if bullets[i].collided(enemies[j].rect):
                    # e.color = white #TESTING
                    score += 1
                    hit = mixer.music.load("Neco-Arc sound effect.wav")
                    mixer.music.play()
                    del enemies[j]
                    del bullets[i]
                    break
        for i in reversed(range(len(bullets))):
            for ooo in reversed(range(len(power))):
                if bullets[i].collided(power[ooo].rect):
                    del power[ooo]
                    spawnx2 = sq.rect.x + sq.rect.width / 2 - 40
                    b2 = Square(green, spawnx2, sq.rect.y, 400, 400)
                    b2.direction = 'N'
                    b2.speed = 20
                    bullets_new.append(b2)
        for i in reversed(range(len(bullets_new))):
            for j in reversed(range(len(enemies))):
                if bullets_new[i].collided(enemies[j].rect):
                    del enemies[j]
                    score += 1

        if dd == int(dd):
            surface.fill(black)
            sq.speed = 20
        elif dd == float(dd):
            surface.fill(color)
            clock.tick(R + 20)
            sq.speed = 40

    # All the drawing

    if true == False:
        for b in bullets:
            b.draw(surface)
            surface.blit(bullet,b)
        for e in enemies:
            e.draw(surface)
            surface.blit(rui,e)
        for pp2 in power:
            pp2.draw(surface)
            surface.blit(nagatoro,pp2)
        for b2 in bullets_new:
            b2.draw(surface)
            surface.blit(nezuko,b2)
        for slow in time_slow:
            slow.draw(surface)
        surface.blit(text1, (50, 50))
        surface.blit(text2, (1770, 50))
        floor.draw(surface)
        sq.draw(surface)
        surface.blit(parvan, sq)
    elif true == True:
        surface.fill(black)
        boss = Square(red,100, 0, 1800, 500)
        sq.draw(surface)
        surface.blit(parvan, sq)
        sq.move()
        if random.randint(1,6) == 3:
            x_enem = random.randint(100, 1900)
            b_enem = Square(green,x_enem,450,30,30)
            b_enem.direction = "S"
            b_enem.speed = 4
            enemy_bullet.append(b_enem)
        for b in bullets:
            b.draw(surface)
            surface.blit(bullet,b)
        for b_enem in enemy_bullet:
            b_enem.draw(surface)
        for b in bullets:
            b.move()
        for b_enem in enemy_bullet:
            b_enem.move()
        boss.draw(surface)
        surface.blit(pet,boss)
        for i in reversed(range(len(bullets))):
                if bullets[i].collided(boss.rect):
                    del bullets[i]
                    ff -= 1
        if ff <= 0:
            surface.fill(black)
            surface.blit(text3, (600, 500))
            for z in reversed(range(len(enemy_bullet))):
                if enemy_bullet[z].collided(sq.rect):
                    kak += 1
        for z in reversed(range(len(enemy_bullet))):
            if enemy_bullet[z].collided(sq.rect):
                kak -= 1
                del enemy_bullet[z]
        if kak <= 0:
            score = 0
            surface.fill(black)
            surface.blit(text4, (600, 500))
    if done == True:
        result = open("demofile2.txt", "a")
        result.write("\n" + current + " == " + str(score) + "\n")
        result.close()

    pygame.display.flip()
    clock.tick(30)  # 30 FPS
pygame.quit()
exit()