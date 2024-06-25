import numpy as np
import pygame
from modules.user_interaction import initialize_interface, handle_user_input
from modules.magnetism_basics import visualize_field_lines

def main():
    # Initialize interface
    screen = initialize_interface()
    width, height = screen.get_size()
    print(f"Pygame window size: {width}x{height}")
    
    # Main loop
    magnets = [{'position': np.array([400, 300]), 'moment': np.array([0, 1, 0])}]
    running = True
    
    while running:
        running = handle_user_input(magnets)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Call your visualization functions
        raw_data, (plot_width, plot_height) = visualize_field_lines(magnets, width, height)
        print(f"Plot size: {plot_width}x{plot_height}")
        
        # Convert raw data to a Pygame surface
        plot_surface = pygame.image.frombuffer(raw_data, (plot_width, plot_height), 'RGBA')
        plot_surface = pygame.transform.scale(plot_surface, (width, height))  # Scale to match Pygame window
        screen.blit(plot_surface, (0, 0))
        
        # Update the display
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
