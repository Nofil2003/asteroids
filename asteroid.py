from circleshape import CircleShape
import constants
import pygame


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, constants.LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
