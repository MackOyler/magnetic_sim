import pygame
from modules.user_interaction import initialize_interface, handle_user_input
from modules.magnetism_basics import visualize_field_lines
from modules.solar_magnetism import visualize_sun_magnetic_field

def main():
    # Initialize interface
    initialize_interface()
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle user input
        handle_user_input()
        
        # Call your visualization functions
        visualize_field_lines()
        visualize_sun_magnetic_field()
        
        # Update the display
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
