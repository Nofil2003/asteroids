from circleshape import CircleShape
import constants
import pygame
from logger import log_event
import random


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

    def split(self) -> None:
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)  # angle
            new_vector = self.velocity.rotate(
                rand
            )  # vector to be passed to first asteroid object
            new_vector2 = self.velocity.rotate(
                -1 * rand
            )  # vector to be passed to second asteroid object
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            a = Asteroid(
                self.position.x, self.position.y, new_radius
            )  # first asteroid object
            a2 = Asteroid(
                self.position.x, self.position.y, new_radius
            )  # second asteroid object
            a.velocity = new_vector * 1.2
            a2.velocity = new_vector2 * 1.2
