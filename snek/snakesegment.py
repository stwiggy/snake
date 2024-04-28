import pygame

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = (177, 255, 87)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.next_segment = None
        self.x = x
        self.y = y
        self.prev_pos = (x, y)

    def rotate(self, angle):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        self.color = (0, 0, 255)