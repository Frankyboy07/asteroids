from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    # def draw(self, screen):
    #    pygame.draw.circle(screen, color='white',center=(self.x, self.y), radius=self.radius, width=2)

    def update(self, dt):
        screen_width = SCREEN_WIDTH  # make sure you have these constants
        screen_height = SCREEN_HEIGHT

        self.position += self.velocity * dt

        if (self.position.x + self.radius < 0 or
            self.position.x - self.radius > SCREEN_WIDTH or
            self.position.y + self.radius < 0 or
                self.position.y - self.radius > SCREEN_HEIGHT):
            self.kill()
            return

        super().update(dt)  # Make sure to call parent class update
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, 'white',
                           (self.radius, self.radius),
                           self.radius, 2)
        self.rect.center = self.position
