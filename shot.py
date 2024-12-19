from circleshape import CircleShape
import pygame
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        radius = SHOT_RADIUS

        super().__init__(x, y, radius)
        self.velocity = velocity
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

   
    def update(self, dt):
        screen_width = SCREEN_WIDTH  
        screen_height = SCREEN_HEIGHT

        self.position += self.velocity * dt

        if (self.position.x + self.radius < 0 or
            self.position.x - self.radius > SCREEN_WIDTH or
            self.position.y + self.radius < 0 or
                self.position.y - self.radius > SCREEN_HEIGHT):
            self.kill()
            return

        super().update(dt)  
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, 'white',
                           (self.radius, self.radius),
                           self.radius, 2)
        self.rect.center = self.position
