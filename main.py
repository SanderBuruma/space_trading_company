import pygame
from classes.entity import Entity
from classes.celestial_body import CelestialBody
from classes.planet import Planet
from classes.star import Star


def main():
    # Initialize PyGame
    pygame.init()

    # Set the window size
    window_size = (640, 480)

    # Create the window
    screen = pygame.display.set_mode(window_size)

    # Set the window title
    pygame.display.set_caption("Rocket Trading Company")

    # Set up the game clock
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check if left-alt + q was pressed
                if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_LALT:
                    running = False
            # Handle other events as needed

        # Update game state

        # Draw the screen
        screen.fill((255, 255, 255))  # Clear the screen to white
        # Draw other game elements as needed
        pygame.display.flip()

        # Limit the frame rate
        tick = clock.tick(60)
        print(tick)

    # Quit PyGame
    pygame.quit()






if __name__ == '__main__':
    main()
