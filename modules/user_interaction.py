import pygame
import numpy as np

def initialize_interface():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Magnetism Simulation")
    return screen

def draw_buttons(screen):
    font = pygame.font.SysFont(None, 24)
    clear_button = pygame.Rect(10, 10, 100, 30)
    pygame.draw.rect(screen, [0, 255, 0], clear_button)
    screen.blit(font.render('Clear', True, (0, 0, 0)), (20, 15))
    
    reset_button = pygame.Rect(120, 10, 100, 30)
    pygame.draw.rect(screen, [255, 0, 0], reset_button)
    screen.blit(font.render('Reset', True, (0, 0, 0)), (130, 15))

    return clear_button, reset_button

def handle_user_input(magnets):
    selected_magnet_index = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, selected_magnet_index

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = np.array(pygame.mouse.get_pos())
            if event.button == 1:  # Left click to add a new magnet
                if mouse_pos[1] > 50:  # Avoid adding magnets in the button area
                    magnets.append({'position': mouse_pos, 'moment': np.array([0, 1, 0])})
            elif event.button == 3:  # Right click to remove the nearest magnet
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    if distances[nearest_magnet_index] < 20:  # Only remove if close enough
                        magnets.pop(nearest_magnet_index)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left click and drag to move a magnet
                mouse_pos = np.array(pygame.mouse.get_pos())
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    if distances[nearest_magnet_index] < 20:  # Only move if close enough
                        magnets[nearest_magnet_index]['position'] = mouse_pos
                        selected_magnet_index = nearest_magnet_index

    return True, selected_magnet_index
