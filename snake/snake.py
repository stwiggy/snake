import pygame
from snakesegment import SnakeSegment

PLAYING_SCREEN_WIDTH = 800
PLAYING_SCREEN_HEIGHT = 600

player_width = 50
player_height = 50
player_speed = 1.5
player_pos_x = 25
player_pox_y = 575
player_movement_started = False

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.head = SnakeSegment(player_pos_x, player_pox_y)
        self.segments = [self.head]
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (375, 300)
        self.speed = 1
        self.direction = "up"
        self.wantedDirection = "up"
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

            current_segment = self.head
            while current_segment.next_segment:
                current_segment.x = current_segment.next_segment
                current_segment.y = current_segment.next_segment
                current_segment = current_segment.next_segment


    def elongate(self):
        last_segment = self.segments[-1]
        new_segment = SnakeSegment(last_segment.rect.x, last_segment.rect.y)
        last_segment.next_segment = new_segment
        self.segments.append(new_segment)

    def prevent_reverse_movement(self):
        #if self.started:
            if self.wantedDirection == "up" and self.direction == "down":
                self.direction = "down"
            elif self.wantedDirection == "down" and self.direction == "up":
                self.direction = "up"
            elif self.wantedDirection == "left" and self.direction == "right":
                self.direction = "right"
            elif self.wantedDirection == "right" and self.direction == "left":
                self.direction = "left"
            else:
                self.direction = self.wantedDirection

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), segment.rect)
            #screen.blit(segment.image, segment.rect)
