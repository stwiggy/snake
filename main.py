import pygame
from food import Food
from snake import Snake

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player.wantedDirection = "left"
        player.started = True

    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        player.wantedDirection = "right"
        player.started = True

    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        player.wantedDirection = "down"
        player.started = True

    elif key[pygame.K_w] or key[pygame.K_UP]:
        player.wantedDirection = "up"
        player.started = True
        
    player.prevent_reverse_movement()
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()