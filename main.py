import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    

    # Game loop
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")

        updatable.update(dt)

        for dr in drawable:
            dr.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        


if __name__ == "__main__":
    main()
