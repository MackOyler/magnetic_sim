import pygame
import numpy as np

MU_0 = 4 * np.pi * 1e-7  # Permeability of free space

def calculate_magnetic_field(magnet_position, magnet_moment, point):
    r = point - magnet_position
    r_norm = r.length()
    if r_norm == 0:
        return pygame.Vector2(0, 0)
    r_hat = r / r_norm
    m_dot_r = magnet_moment.dot(r_hat)
    term1 = 3 * r_hat * m_dot_r / r_norm**3
    term2 = magnet_moment / r_norm**3
    B = (MU_0 / (4 * np.pi)) * (term1 - term2)
    return pygame.Vector2(B[0], B[1])
