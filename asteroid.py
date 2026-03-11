import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.
    Can move through space and split into smaller ones when destroyed.
    """
    def __init__(self, x, y, radius):
        """
        Initializes a new asteroid.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            radius (float): Radius of the asteroid.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draws the asteroid on the screen as a circle.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity.

        Args:
            dt (float): Time delta.
        """
        self.position += self.velocity * dt

    def split(self):
        """
        Splits the asteroid into two smaller ones or destroys it if it's too small.
        """
        self.kill()

        # If it's already at the minimum size, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        # Calculate random angles for the new fragments
        random_angle = random.uniform(20, 50)
        first_new_asteroid_vel = self.velocity.rotate(random_angle)
        second_new_asteroid_vel = self.velocity.rotate(-random_angle)
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create new fragments
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        
        # Set their velocities (with a slight speed boost)
        first_new_asteroid.velocity = first_new_asteroid_vel * 1.2
        second_new_asteroid.velocity = second_new_asteroid_vel * 1.2
