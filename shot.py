from constants import SHOT_RADIUS, LINE_WIDTH
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    """
    Represents a projectile (shot) fired by the player's ship.
    """
    def __init__(self, x, y, radius):
        """
        Initializes a new shot.

        Args:
            x (float): Initial x-position.
            y (float): Initial y-position.
            radius (float): Radius of the projectile.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the shot on the screen.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        """
        Updates the shot's position based on its velocity.

        Args:
            dt (float): Time delta.
        """
        self.position += self.velocity * dt