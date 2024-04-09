import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_size = 50
player = pygame.Rect((0, 550, player_size, player_size))

food_size = 20
food = pygame.Rect((random.randint(0, 780), random.randint(0, 580), food_size, food_size))
food_hidden = False

def generateFood():
    return pygame.Rect((random.randint(0, 780), random.randint(0, 580), food_size, food_size))

run = True
while run:

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    if player.left < 0:
        player.left = 0
    elif player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH
    if player.top < 0:
        player.top = 0
    elif player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

    
    if player.colliderect(food):
        food_hidden = True

    if food_hidden:
        time.sleep(0.03)
        food = generateFood()
        food_hidden = False

    else:
        pygame.draw.rect(screen, (255, 0, 0), food)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

#make a timer for food to be collect and respawn
#make snake accelerate
#make the snake grow