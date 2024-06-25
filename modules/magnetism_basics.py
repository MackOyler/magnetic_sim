import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

MU_0 = 4 * np.pi * 1e-7  # Permeability of free space

def calculate_magnetic_field(magnet_position, magnet_moment, point):
    if len(magnet_position) == 2:
        magnet_position = np.append(magnet_position, 0)
    if len(magnet_moment) == 2:
        magnet_moment = np.append(magnet_moment, 0)
    if len(point) == 2:
        point = np.append(point, 0)

    r = point - magnet_position
    r_norm = np.linalg.norm(r)
    if r_norm == 0:
        return np.zeros(3)
    r_hat = r / r_norm
    m_dot_r = np.dot(magnet_moment, r_hat)
    term1 = 3 * r_hat * m_dot_r / r_norm**3
    term2 = magnet_moment / r_norm**3
    B = (MU_0 / (4 * np.pi)) * (term1 - term2)
    return B

def visualize_field_lines(magnets, width, height, grid_size=100, grid_extent=5):
    dpi = 100  # Set DPI to match screen resolution
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    
    x = np.linspace(-grid_extent, grid_extent, grid_size)
    y = np.linspace(-grid_extent, grid_extent, grid_size)
    X, Y = np.meshgrid(x, y)
    U, V = np.zeros_like(X), np.zeros_like(Y)

    for i in range(grid_size):
        for j in range(grid_size):
            point = np.array([X[i, j], Y[i, j]])
            B = np.zeros(3)
            for magnet in magnets:
                B += calculate_magnetic_field(magnet['position'], magnet['moment'], point)
            U[i, j], V[i, j] = B[0], B[1]

    ax.streamplot(X, Y, U, V, color=np.log(np.hypot(U, V)), cmap='viridis')
    ax.set_xlim(-grid_extent, grid_extent)  # Set x limits
    ax.set_ylim(-grid_extent, grid_extent)  # Set y limits
    ax.set_aspect('equal')  # Maintain aspect ratio

    canvas = FigureCanvas(fig)
    canvas.draw()
    raw_data = canvas.buffer_rgba()
    plt.close(fig)

    return raw_data, canvas.get_width_height()
