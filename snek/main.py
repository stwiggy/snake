import pygame
from food import Food
from snake import Snake
from snakesegment import SnakeSegment

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Snake()

foods = pygame.sprite.Group()
food = Food()
foods.add(food)

clock = pygame.time.Clock()

run = True

thing = SnakeSegment(100, 100)

while run:
    pygame.display.set_caption("Snake Game")
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player.color, player)
    pygame.draw.rect(screen, thing.color, thing)
    # #player.draw(screen)
    # for segment in player.segments:
    #     pygame.draw.rect(screen, (0, 255, 0), segment)
    #     #screen.blit(segment.image, segment.rect)
    #     #print(len(player.segments))


    foods.update()
    foods.draw(screen)

    if food.hitbox.colliderect(player):
        food.hide()
        #player.elongate()
        food = Food()
        foods.add(food)

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        thing.rotate(90)
        print(thing.x, thing.y)

    elif key[pygame.K_a] or key[pygame.K_LEFT]:
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

    clock.tick(100) #change to adjust difficulty and stuff

pygame.quit()