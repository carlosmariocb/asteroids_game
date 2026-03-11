from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, 
    PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, 
    PLAYER_SHOOT_COOLDOWN_SECONDS
)
import pygame
from shot import Shot

class Player(CircleShape):
    """
    Represents the player-controlled spaceship.
    Handles movement, rotation, and weapon fire.
    """
    def __init__(self, x, y):
        """
        Initializes the player at the given coordinates.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self):
        """
        Calculates the vertices of the ship's triangle shape based on rotation.

        Returns:
            list[pygame.Vector2]: A list of three vectors defining the triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the player's ship on the screen.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        """
        Updates the ship's rotation.

        Args:
            dt (float): Time delta.
        """
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        """
        Updates the player's state based on input.

        Args:
            dt (float): Time delta.
        """
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt

        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # Handle movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        # Handle shooting
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer <= 0:
                self.shoot()
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            
    def move(self, dt):
        """
        Moves the ship forward or backward.

        Args:
            dt (float): Time delta.
        """
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        """
        Creates and fires a projectile from the front of the ship.
        """
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED