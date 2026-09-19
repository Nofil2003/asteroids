import pygame
import constants
from logger import log_state


def main() -> None:
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}"
    )

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
