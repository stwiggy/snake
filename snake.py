import pygame

PLAYING_SCREEN_WIDTH = 800
PLAYING_SCREEN_HEIGHT = 600

player_width = 50
player_height = 50
player_speed = 1
player_pos_x = 25
player_pox_y = 575
player_direction = "up"
player_movement_started = False

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, PLAYING_SCREEN_HEIGHT)
        self.speed = 1
        self.direction = "up"
        self.started = False

    def update(self):
        pass

    def move(self):
        if self.started:
            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed
            elif self.direction == "left":
                self.rect.x -= self.speed
            elif self.direction == "right":
                    self.rect.x += self.speed

            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > PLAYING_SCREEN_WIDTH:
                self.rect.right = PLAYING_SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > PLAYING_SCREEN_HEIGHT:
                self.rect.bottom = PLAYING_SCREEN_HEIGHT

    def elongate(self):
        global player_height
        player_height += 10
        self = pygame.Rect((player_pos_x, player_pox_y, player_width, player_height))