import random

import pygame
from pygame import Surface

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: "Surface") -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        val = random.uniform(20, 50)
        vec = self.velocity.rotate(val)
        vec2 = self.velocity.rotate(-val)
        rad = self.radius - ASTEROID_MIN_RADIUS
        astr1 = Asteroid(self.position.x, self.position.y, rad)
        astr2 = Asteroid(self.position.x, self.position.y, rad)
        astr1.velocity = vec * 1.2
        astr2.velocity = vec2 * 1.2
