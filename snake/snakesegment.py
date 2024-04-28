import pygame

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((177, 255, 87))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.next_segment = None
        self.x = x
        self.y = y

    