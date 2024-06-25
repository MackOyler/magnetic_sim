import pygame
import numpy as np

def initialize_interface():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Magnetism Simulation")
    return screen

def handle_user_input(event, magnets):
    selected_magnet_index = None
    if event.type == pygame.QUIT:
        return False, selected_magnet_index

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        if event.button == 1:  # Left click to add a new magnet
            # Check if the click is not on a button or slider
            if not (10 <= mouse_pos.x <= 90 and 10 <= mouse_pos.y <= 40) and not (100 <= mouse_pos.x <= 180 and 10 <= mouse_pos.y <= 40) and not (100 <= mouse_pos.x <= 300 and 60 <= mouse_pos.y <= 120):
                magnets.append({'position': mouse_pos, 'moment': pygame.Vector2(0, 1)})
        elif event.button == 3:  # Right click to remove the nearest magnet
            if magnets:
                distances = [magnet['position'].distance_to(mouse_pos) for magnet in magnets]
                nearest_magnet_index = np.argmin(distances)
                if distances[nearest_magnet_index] < 20:  # Only remove if close enough
                    magnets.pop(nearest_magnet_index)

    if event.type == pygame.MOUSEMOTION:
        if pygame.mouse.get_pressed()[0]:  # Left click and drag to move a magnet
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            if magnets:
                distances = [magnet['position'].distance_to(mouse_pos) for magnet in magnets]
                nearest_magnet_index = np.argmin(distances)
                if distances[nearest_magnet_index] < 20:  # Only move if close enough
                    magnets[nearest_magnet_index]['position'] = mouse_pos
                    selected_magnet_index = nearest_magnet_index

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
        if reset_button.collidepoint(event.pos):
            magnets.clear()
            magnets.append({'position': pygame.Vector2(400, 300), 'moment': pygame.Vector2(0, 1)})
