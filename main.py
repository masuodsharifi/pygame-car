import pygame
import time
import random

pygame.init()
muzic = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")
display_width = 800
display_hight = 600

black = (0, 0, 0)
White = (255, 255, 255)
Whitei = (255, 255, 255)
blue = (11, 0, 233)
red = (200, 0, 0)
redb = (255, 0, 0)
green = (0, 255, 0)
greeni = (0, 255, 0)
greenii = (0, 255, 0)
bgreen = (0, 200, 0)
bgreeni = (0, 200, 0)
color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))


gamedisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption('game WMASUODW  ')

clock = pygame.time.Clock()
carlmg = pygame.image.load('car.png')

car_width = 45


def bali(msy, x, y, w, h, ia, ac, akthon=None):
    mos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mos[0] > x and y + h > mos[1] > y:
        pygame.draw.rect(gamedisplay, ac, (x, y, w, h))
        if click[0] == 1 and akthon != None:
            if akthon == 'play':
                game()
            elif akthon == "quit":
                pygame.QUIT()
                quit()

    else:
        pygame.draw.rect(gamedisplay, ia, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)

    ts, tr = to(msy, smalltext)
    tr.center = ((x+(w/2)), (y+(h/2)))
    gamedisplay.blit(ts, tr)


def game_d():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(White)
        lt = pygame.font.Font('freesansbold.ttf', 115)
        ts, tr = to('let`s go', lt)
        tr.center = ((display_width/2), (display_hight/2))
        gamedisplay.blit(ts, tr)
        bali("play : ", 150, 450, 100, 50, greenii, bgreeni, 'play')
        bali("EXIT: ", 550, 450, 100, 50, red, redb, 'EXIT')
        pygame.display.update()


def sscore(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("score : "+str(count), True, red)
    gamedisplay.blit(text, (0, 0))


def sa(sx, sy, sw, sh, color):
    pygame.draw.rect(gamedisplay, color, [sx, sy, sw, sh])


def car(x, y):
    gamedisplay.blit(carlmg, (x, y))


def to(text, font):
    tsr = font.render(text, True, black)
    return tsr, tsr.get_rect()


def gd(text):
    lt = pygame.font.Font('freesansbold.ttf', 115)
    ts, tr = to(text, lt)
    tr.center = ((display_width/2), (display_hight/2))
    gamedisplay.blit(ts, tr)
    pygame.display.update()

    time.sleep(2)
    game()


def tesadof():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(muzic)
    lt = pygame.font.Font('freesansbold.ttf', 115)
    ts, tr = to('choose', lt)
    tr.center = ((display_width/2), (display_hight/2))
    gamedisplay.blit(ts, tr)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bali("try agian : ", 150, 450, 100, 50, greenii, bgreeni, 'play')
        bali("quit : ", 550, 450, 100, 50, red, redb, 'quit')

        pygame.display.update()


def game():
    x = (display_width * 0.45)
    y = (display_hight * 0.8)
    pygame.mixer.music.play(-1)

    x_chenge = 0
    stuff_stx = random.randrange(0, display_width)
    stuff_staty = -600
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100
    score = 0

    gexit = False

    while not gexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_chenge = -5
                elif event.key == pygame.K_RIGHT:
                    x_chenge = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                    x_chenge = 0

        x += x_chenge

        gamedisplay.fill(White)
        # sx,sy,sw,sh,color

        a = color
        sa(stuff_stx, stuff_staty,  stuff_width, stuff_height, a)

        stuff_staty += stuff_speed
        car(x, y)
        sscore(score)
        if x > display_width - car_width or x < 0:
            tesadof()
        if stuff_staty > display_hight:
            stuff_staty = 0 - stuff_height
            stuff_stx = random.randrange(0, display_width)
            score += 1

            if (score % 5 == 0):
                stuff_speed += 1

        if y < stuff_staty + stuff_height:
            if x > stuff_stx and x < stuff_stx + stuff_width or x + car_width > stuff_stx and x + car_width < stuff_stx + stuff_width:
                tesadof()

        pygame.display.update()
        clock.tick(60)


game_d()
game()
pygame.quit()
quit()
