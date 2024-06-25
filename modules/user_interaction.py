import pygame
import numpy as np

def initialize_interface():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # Increase window size
    pygame.display.set_caption("Magnetism Simulation")
    return screen

def handle_user_input(magnets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click to add a new magnet
                mouse_pos = np.array(pygame.mouse.get_pos())
                magnets.append({'position': mouse_pos, 'moment': np.array([0, 1, 0])})
            elif event.button == 3:  # Right click to remove the nearest magnet
                mouse_pos = np.array(pygame.mouse.get_pos())
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    magnets.pop(nearest_magnet_index)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left click and drag to move a magnet
                mouse_pos = np.array(pygame.mouse.get_pos())
                if magnets:
                    distances = [np.linalg.norm(m['position'] - mouse_pos) for m in magnets]
                    nearest_magnet_index = np.argmin(distances)
                    magnets[nearest_magnet_index]['position'] = mouse_pos

    return True
