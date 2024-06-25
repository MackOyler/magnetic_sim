import pygame
import pygame_gui
from pygame_gui.elements import UIHorizontalSlider, UILabel
from modules.user_interaction import initialize_interface, handle_user_input, draw_buttons, check_button_click
from modules.magnetism_basics import calculate_magnetic_field

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    manager = pygame_gui.UIManager((1200, 800))
    
    magnet_strength_slider = UIHorizontalSlider(pygame.Rect((100, 50), (200, 30)), 1, (0, 10), manager)
    magnet_strength_label = UILabel(pygame.Rect((100, 20), (200, 30)), "Magnet Strength", manager)
    
    magnets = [{'position': pygame.Vector2(400, 300), 'moment': pygame.Vector2(0, 1)}]
    
    # Draw buttons and assign them to variables
    clear_button, reset_button = draw_buttons(screen)
    
    running = True
    while running:
        time_delta = pygame.time.Clock().tick(30) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)
            check_button_click(event, magnets, clear_button, reset_button)
        
        screen.fill((255, 255, 255))
        
        manager.update(time_delta)
        
        # Handle user input
        running, selected_magnet_index = handle_user_input(magnets)
        
        # Draw buttons
        clear_button, reset_button = draw_buttons(screen)
        
        # Draw magnets and field lines
        draw_magnets(screen, magnets)
        draw_field_lines(screen, magnets)
        
        manager.draw_ui(screen)
        
        pygame.display.flip()

    pygame.quit()

def draw_magnets(screen, magnets):
    for magnet in magnets:
        pygame.draw.circle(screen, (255, 0, 0), (int(magnet['position'].x), int(magnet['position'].y)), 10)

def draw_field_lines(screen, magnets):
    width, height = screen.get_size()
    for x in range(0, width, 20):
        for y in range(0, height, 20):
            B = sum((calculate_magnetic_field(magnet['position'], magnet['moment'], pygame.Vector2(x, y)) for magnet in magnets), pygame.Vector2(0, 0))
            end_point = pygame.Vector2(x, y) + B * 50  # Scale the magnetic field for better visualization
            pygame.draw.line(screen, (0, 0, 255), (x, y), (end_point.x, end_point.y), 1)

if __name__ == '__main__':
    main()
