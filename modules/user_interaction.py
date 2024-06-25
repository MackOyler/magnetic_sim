import pygame
import numpy as np

def initialize_interface():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Magnetism Simulation")
    return screen

def handle_user_input(magnets):
    selected_magnet_index = None
    for event in pygame.event.get():
        print(f"Event: {event}")  # Debugging print
        if event.type == pygame.QUIT:
            return False, selected_magnet_index

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = np.array(pygame.mouse.get_pos()) - [0, 50]  # Adjust for button area
            print(f"Mouse Position: {mouse_pos}, Button: {event.button}")  # Debugging print
            if event.button == 1:  # Left click to add a new magnet
                magnets.append({'position': mouse_pos, 'moment': np.array([0, 1, 0])})
                print(f"Added Magnet: {magnets[-1]}")  # Debugging print
            elif event.button == 3:  # Right click to remove the nearest magnet
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    if distances[nearest_magnet_index] < 20:  # Only remove if close enough
                        removed_magnet = magnets.pop(nearest_magnet_index)
                        print(f"Removed Magnet: {removed_magnet}")  # Debugging print

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left click and drag to move a magnet
                mouse_pos = np.array(pygame.mouse.get_pos()) - [0, 50]  # Adjust for button area
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    if distances[nearest_magnet_index] < 20:  # Only move if close enough
                        magnets[nearest_magnet_index]['position'] = mouse_pos
                        selected_magnet_index = nearest_magnet_index
                        print(f"Moved Magnet: {magnets[nearest_magnet_index]}")  # Debugging print

    return True, selected_magnet_index

def draw_buttons(screen):
    clear_button = pygame.Rect(10, 10, 80, 30)
    reset_button = pygame.Rect(100, 10, 80, 30)
    
    pygame.draw.rect(screen, (0, 255, 0), clear_button)
    pygame.draw.rect(screen, (255, 0, 0), reset_button)
    
    font = pygame.font.Font(None, 24)
    clear_text = font.render('Clear', True, (0, 0, 0))
    reset_text = font.render('Reset', True, (0, 0, 0))
    screen.blit(clear_text, (clear_button.x + 10, clear_button.y + 5))
    screen.blit(reset_text, (reset_button.x + 10, reset_button.y + 5))
    
    return clear_button, reset_button

def check_button_click(event, magnets, clear_button, reset_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if clear_button.collidepoint(event.pos):
            magnets.clear()
            print("Cleared Magnets")  # Debugging print
        if reset_button.collidepoint(event.pos):
            magnets.clear()
            magnets.append({'position': np.array([400, 300]), 'moment': np.array([0, 1, 0])})
            print("Reset Magnets")  # Debugging print
