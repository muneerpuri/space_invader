import pygame
import random
import math
from pygame import mixer
pygame.init()  # everytime ReQuiRed

bgimg = pygame.image.load('bgimg.jpg')
bgimg = pygame.transform.scale(bgimg, (800, 600))
bullet = pygame.image.load('laser.png')
bullet = pygame.transform.scale(bullet, (32, 32))
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"
mainsound = mixer.music.load('backmusic.mp3')
mainsound = mixer.music.play(-1)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space infinity War : By Muneer Puri")
iconLogo = pygame.image.load('rocket.png')
pygame.display.set_icon(iconLogo)
hero = pygame.image.load('spaceship3.png')
hero = pygame.transform.scale(hero, (64, 64))
hero_x = 370
hero_y = 500
herox_change = 0

enemy = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change = []
NOE = 5
for i in range(NOE):
    enemy.append(pygame.transform.scale(pygame.image.load('enemy.png'), (64, 64)))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemyx_change.append(3)
    enemyy_change.append(40)

# score = 0
scoreval = 0
font = pygame.font.Font('freesansbold.ttf' , 32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf' , 64)


def GOT():
    GO = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(GO, (200, 250))
    mainsound = mixer.music.stop()


def showscore(x,y):
    score= font.render(f"SCORE: {scoreval}", True, (255,0,0))
    screen.blit(score, (x, y))

def heropos(x, y):
    screen.blit(hero, (x, y))


def enemypos(x, y , i):
    screen.blit(enemy[i], (x, y))


def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


def isCol(enemy_x, enemy_y, bullet_x, bullet_y):
    dis = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if dis < 27:
        return True
    else:
        return False


gamebegin = True
while gamebegin:
    screen.fill((255, 0, 0))
    screen.blit(bgimg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamebegin = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                herox_change = 5
            if event.key == pygame.K_LEFT:
                herox_change = -5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    b_sound = mixer.Sound('lasersound.aiff')
                    b_sound.play()
                    bullet_x = hero_x
                    firebullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                herox_change = 0

    hero_x += herox_change
    if hero_x <= 0:
        hero_x = 0
    elif hero_x >= 736:
        hero_x = 736

    for i in range(NOE):
        if enemy_y[i] > 440:
            for j in range(NOE):
                enemy_y[j] = 2000
            GOT()
            break

        enemy_x[i] += enemyx_change[i]
        if enemy_x[i] <= 0:
            enemyx_change[i] = 3
            enemy_y[i] += enemyy_change[i]
        elif enemy_x[i] >= 736:
            enemyx_change[i] = -3
            enemy_y[i] += enemyy_change[i]
        col = isCol(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if col:
            e_sound = mixer.Sound('boomsound.wav')
            e_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            scoreval += 10

            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemypos(enemy_x[i] , enemy_y[i] , i)

    # WHen we want something to get updated continuously
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        firebullet(bullet_x, bullet_y)
        bullet_y -= bullety_change


    showscore(textx,texty)
    heropos(hero_x, hero_y)
    pygame.display.update()
