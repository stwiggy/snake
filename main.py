import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_width = 50
player_height = 50
player_speed = 1
player_pos_x = 25
player_pox_y = 575
player_direction = "up"
player_rotate_requested = False
#player = pygame.Rect((player_pos_x, player_pox_y, player_width, player_height))
player = pygame.image.load("snake-head.png").convert_alpha()

def elongate():
    global player_height, player
    player_height += 10
    player = pygame.Rect((player_pos_x, player_pox_y, player_width, player_height))
    
def rotatePlayer(direction, angle):
    global player_direction, player_rotate_requested, player
    if player_direction != direction:
        if player_direction == "up":
            player = pygame.transform.rotate(player, 0)
        elif player_direction == "right":
            player = pygame.transform.rotate(player, 0 - 90)
        elif player_direction == "down":
            player = pygame.transform.rotate(player, 0 - 180)
        else:
            player = pygame.transform.rotate(player, 0 - 270)
    player_direction = direction
    return player

food_size = 20

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((food_size, food_size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 780), random.randint(0, 580))

        self.hitbox_size = 10
        self.hitbox = pygame.Rect(self.rect.centerx - self.hitbox_size // 2, self.rect.centery - self.hitbox_size // 2, self.hitbox_size, self.hitbox_size)

    def update(self):
        self.hitbox.center = self.rect.center

    def hide(self):
        self.kill()

def generateFood():
    return Food()

foods = pygame.sprite.Group()
food = Food()
foods.add(food)

run = True

while run:
    screen.fill((0, 0, 0))
    player_rect = player.get_rect(center= (player_pos_x, player_pox_y))
    screen.blit(player, player_rect)

    foods.update()
    foods.draw(screen)

    if food.hitbox.colliderect(player.get_rect()):
        food.hide()
        #elongate()
        food = Food()
        foods.add(food)

    #pygame.draw.rect(screen, (0, 255, 0), player)

    key = pygame.key.get_pressed()

    #player.bottomleft = (player_pos_x, player_pox_y)

    if key[pygame.K_a] == True:
        player_pos_x -= player_speed
        player = rotatePlayer("left", -90)

    elif key[pygame.K_d] == True:
        player_pos_x += player_speed
        player = rotatePlayer("right", 0)

    elif key[pygame.K_s] == True:
        player_pox_y += player_speed
        player = rotatePlayer("down", 90)

    elif key[pygame.K_w] == True:
        player_pox_y -= player_speed
        player = rotatePlayer("up", 180)


    if player_pos_x < 0:
        player_pos_x = 0
    elif player_pos_x + player_width > SCREEN_WIDTH:
        player_pos_x = SCREEN_WIDTH - player_width

    if player_pox_y < 0:
        player_pox_y = 0
    elif player_pox_y + player_height > SCREEN_HEIGHT:
        player_pox_y = SCREEN_HEIGHT - player_height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()

#i put graphics
#tmr: WHAT THE HECK IS GOING ON WITH ROTATION LOGIC
#weird bounds
#make collisions
#growth