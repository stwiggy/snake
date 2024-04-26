import pygame
from food import Food
from snake import Snake

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

movement_started = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Snake()

foods = pygame.sprite.Group()
food = Food()
foods.add(food)

run = True

while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    foods.update()
    foods.draw(screen)

    if food.hitbox.colliderect(player):
         food.hide()
         food = Food()
         foods.add(food)

    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        player.direction = "left"
        player.started = True

    elif key[pygame.K_d]:
        player.direction = "right"
        player.started = True

    elif key[pygame.K_s]:
        player.direction = "down"
        player.started = True

    elif key[pygame.K_w]:
        player.direction = "up"
        player.started = True
    
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()