import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable,)   
    asteroidfield = AsteroidField()                        
    
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT /2)
    asteroid = Asteroid(100, 100, 20)
    print(f"Is asteroid in groups? Asteroids: {asteroid in asteroids}, Drawable: {asteroid in drawable}")
    print(updatable)
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    print(f"Number of asteroids: {len(asteroids)}")
    print(f"Number of updatable objects: {len(updatable)}")
    print(f"Number of drawable objects: {len(drawable)}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                pygame.QUIT
                return
        drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        




if __name__ == '__main__':
    main()