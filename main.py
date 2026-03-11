import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """
    The main entry point for the Asteroids game.
    Initializes Pygame, sets up the game world, and runs the main loop.
    """
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create sprite groups for managing game objects
    updatable = pygame.sprite.Group()  # Objects that need to update every frame
    drawable = pygame.sprite.Group()   # Objects that need to be drawn every frame
    asteroids = pygame.sprite.Group()  # All asteroids
    shots = pygame.sprite.Group()      # All projectiles

    # Set up containers for automatic group membership
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initialize game objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    running = True
    while running:
        # Log the current game state for analysis
        log_state()
        
        # Handle events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the background
        screen.fill("black")

        # Update all active objects
        updatable.update(dt)

        # Check for collisions: Asteroid vs Player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Check for collisions: Asteroid vs Shots
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        
        # Draw all active objects
        for dr in drawable:
            dr.draw(screen)
        
        # Refresh the display
        pygame.display.flip()

        # Update timing and get the next delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
