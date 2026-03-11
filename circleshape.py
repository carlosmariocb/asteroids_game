import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """
    A base class for circular game objects.
    Inherits from pygame.sprite.Sprite and handles basic position, velocity, and collision.
    """
    def __init__(self, x, y, radius):
        """
        Initializes a new CircleShape.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            radius (float): Radius of the circular shape.
        """
        # Set up sprite containers if they are defined on the class
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """
        Draws the shape to the screen. To be overridden by subclasses.
        """
        pass

    def update(self, dt):
        """
        Updates the shape's state. To be overridden by subclasses.

        Args:
            dt (float): Time delta since the last frame.
        """
        pass
    
    def collides_with(self, other):
        """
        Checks for collision with another CircleShape object.

        Args:
            other (CircleShape): The other object to check collision against.

        Returns:
            bool: True if the shapes collide, False otherwise.
        """
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        return False