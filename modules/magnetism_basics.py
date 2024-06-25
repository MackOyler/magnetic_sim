import numpy as np
import matplotlib.pyplot as plt

MU_0 = 4 * np.pi * 1e-7  # Permeability of free space

def calculate_magnetic_field(magnet_position, magnet_moment, point):
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

def visualize_field_lines(magnets, grid_size=100, grid_extent=5):
    x = np.linspace(-grid_extent, grid_extent, grid_size)
    y = np.linspace(-grid_extent, grid_extent, grid_size)
    X, Y = np.meshgrid(x, y)
    U, V = np.zeros_like(X), np.zeros_like(Y)
    
    for i in range(grid_size):
        for j in range(grid_size):
            point = np.array([X[i, j], Y[i, j], 0])
            B = np.zeros(3)
            for magnet in magnets:
                B += calculate_magnetic_field(magnet['position'], magnet['moment'], point)
            U[i, j], V[i, j] = B[0], B[1]
    
    fig, ax = plt.subplots()
    ax.streamplot(X, Y, U, V, color=np.log(np.hypot(U, V)), cmap='viridis')
    ax.set_aspect('equal')
    plt.show()

# Example usage
if __name__ == "__main__":
    magnets = [
        {'position': np.array([0, 0, 0]), 'moment': np.array([0, 1, 0])}
    ]
    visualize_field_lines(magnets)
