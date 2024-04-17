import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player_width = 50
player_height = 50
player_speed = 1
player_pos_x = 25
player_pox_y = 575
player_direction = "up"
player_rotate_requested = False

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("snake-head.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (player_pos_x, player_pox_y)

        self.hitbox_size = 50
        self.hitbox = pygame.Rect(self.rect.centerx - self.hitbox_size // 2, self.rect.centery - self.hitbox_size // 2, self.hitbox_size, self.hitbox_size)

    def getX(self):
        return player_pos_x

    def getY(self):
        return player_pos_y

    def moveX(self, direction):
        global player_pos_x
        player_pos_x = player_speed * direction

        if player_pos_x < 0:
            player_pos_x = 0
        elif player_pos_x + player_width > SCREEN_WIDTH:
            player_pos_x = SCREEN_WIDTH - player_width

    def moveY(self, direction):
        global player_pos_y
        player_pos_y = player_speed * direction

        if player_pox_y < 0:
            player_pox_y = 0
        elif player_pox_y + player_height > SCREEN_HEIGHT:
            player_pox_y = SCREEN_HEIGHT - player_height

    def elongate(self):
        global player_height
        player_height += 10
        self = pygame.Rect((player_pos_x, player_pox_y, player_width, player_height))

    def getRect(self):
        return self.image.get_rect(center=(player_pos_x, player_pox_y))