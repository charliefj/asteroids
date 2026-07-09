import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self)-> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vector_split1 = self.velocity.rotate(angle)
            vector_split2 = self.velocity.rotate(-1*angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = vector_split1*1.2
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = vector_split2*1.2

