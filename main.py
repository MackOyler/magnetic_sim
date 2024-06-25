import numpy as np
import pygame
from modules.user_interaction import initialize_interface, handle_user_input, draw_buttons, check_button_click
from modules.magnetism_basics import visualize_field_lines

def main():
    # Initialize interface
    screen = initialize_interface()
    width, height = screen.get_size()
    
    # Main loop
    magnets = [{'position': np.array([400, 300]), 'moment': np.array([0, 1, 0])}]
    running = True
    selected_magnet_index = None
    clear_button, reset_button = draw_buttons(screen)

    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                check_button_click(event, magnets, clear_button, reset_button)

            running, selected_magnet_index = handle_user_input(magnets)

            # Clear the screen
            screen.fill((255, 255, 255))

            # Call your visualization functions
            raw_data, (plot_width, plot_height) = visualize_field_lines(magnets, width, height, selected_magnet_index=selected_magnet_index)
            
            # Convert raw data to a Pygame surface
            plot_surface = pygame.image.frombuffer(raw_data, (plot_width, plot_height), 'RGBA')
            plot_surface = pygame.transform.scale(plot_surface, (width, height - 50))  # Scale to match Pygame window, leaving space for buttons
            screen.blit(plot_surface, (0, 50))  # Offset to avoid button area

            # Draw buttons
            clear_button, reset_button = draw_buttons(screen)
            
            # Update the display
            pygame.display.flip()
        except Exception as e:
            print(f"An error occurred: {e}")
            running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
