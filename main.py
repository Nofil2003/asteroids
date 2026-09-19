import pygame
import constants


def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(
        f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}"
    )


if __name__ == "__main__":
    main()
