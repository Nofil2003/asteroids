import pygame
from pygame.display import update
import constants
from player import Player
from logger import log_event, log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from shot import Shot


def main() -> None:
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    player1 = Player(
        constants.SCREEN_WIDTH / 2,
        constants.SCREEN_HEIGHT / 2,
    )
    new_asteroidfield = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}"
    )

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:  # game loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    print("collision!")
                    asteroid.split()
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
