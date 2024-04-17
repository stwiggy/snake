import pygame
import random

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