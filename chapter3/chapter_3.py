"""Matplotlib for Python Developers - Chapter 3.

Styling in matplotlib."""

import matplotlib.pyplot as plt
import numpy as np


def controlling_colors():
    """Control the colors of the lines drawn."""
    y = np.arange(1, 3)
    plt.plot(y, 'y')
    plt.plot(y + 1, 'm')
    plt.plot(y + 2, 'c')
    # plt.plot(y, 'y', y + 1, 'm', y + 2, 'c')
    plt.show()


def controlling_line_styles():
    """Control the style of each line."""
    y = np.arange(1, 3)
    plt.plot(y, '--', y + 1, '-.', y + 2, ':')
    plt.show()


def controlling_markers():
    """Control the style of each marker.

    When defining the marker, the line will be omitted unless specified."""
    y = np.arange(1, 3, 0.2)
    plt.plot(y, 'x', y + 0.5, 'o', y + 1, 'D', y + 1.5, '^', y + 2, 's')
    plt.show()


def controlling_all_at_once():
    """Color, style and marker can be defined all at once."""
    y = np.arange(1, 3, 0.3)
    plt.plot(y, 'cx--', y + 1, 'mo:', y + 2, 'kp-.')
    plt.show()


if __name__ == '__main__':
    controlling_colors()
    controlling_line_styles()
    controlling_markers()
    controlling_all_at_once()
