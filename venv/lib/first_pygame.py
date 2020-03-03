import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

car_speed = 0
car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome To My First Pygame')
clock = pygame.time.Clock()

crashed = False
carImg = pygame.image.load("racecar.png")

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:" +str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

    game_loop()


def crash():
    message_display('You Crashed')
    pygame.quit()
    quit()

def which_way(x, thing_startx, thing_width):
    if (x > 727):
        return -((x + car_width) - thing_startx)
    elif(x < 73):
        return ((thing_startx + thing_width) - x)
    elif(x + 36 < thing_startx + thing_width/2):
        return -((x + car_width) - thing_startx)
    else:
        return ((thing_startx + thing_width) - x)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)


    thing_width = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600
    thing_speed = 7
    thing_height = 100

    dodged = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
            x += which_way(x, thing_startx, thing_width)
            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0"""

        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x <= 0:
            crash()

        if y > thing_starty+thing_height:
            """print('y crossover')"""
            if x > thing_startx and x < thing_startx + thing_width:
                crash()
            if (x + car_width) > thing_startx and (x + car_width) < (thing_startx + thing_width):
                crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, int(display_width - thing_width))
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * .5)

        pygame.display.update()
        clock.tick(60)
game_loop()

