import numpy as np
import matplotlib.pyplot as plt

def visualize_sun_magnetic_field():
    # Define a simple model for the sun's magnetic field
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + 0.2 * np.sin(4 * theta)  # A simple perturbation to simulate solar activity

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    plt.title("Sun's Magnetic Field")
    plt.show()
