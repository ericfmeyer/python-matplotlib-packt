"""Matplotlib for Python Developers - Chapter 2."""

import matplotlib.pyplot as plt
import numpy as np


def first_plots():
    """Plot 4 points."""
    plt.plot([1, 3, 2, 4])
    plt.title("Plotting single values")
    plt.show()


def quadratic_plot():
    """Plot a quadratic function."""
    values = range(6)
    plt.plot(values, [x ** 2 for x in values])
    plt.title("Quadratic function")
    plt.show()


def better_quadratic_plot():
    """Plot a quadratic function using NumPy array."""
    values = np.arange(0.0, 6.0, 0.1)
    plt.plot(values, [x ** 2 for x in values])
    plt.title("Better Quadratic function with NumPy arange()")
    plt.show()


def multiline_plots():
    """Plot multiple lines."""
    values = range(1, 5)
    plt.plot(values, [x * 1.5 for x in values],
             values, [x * 3 for x in values],
             values, [x / 3 for x in values])
    plt.title("Multiple lines with normal range()")
    plt.show()


def better_multiline_plots():
    """Plot multiple lines using NumPy array."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    plt.title("Multiple lines with NumPy arange()")
    plt.show()


def adding_a_grid():
    """Plot on a figure with grid enabled."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    plt.grid(True)
    plt.title("With a grid")
    plt.show()


def setting_an_axis():
    """Plot on a figure with set axis limits."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    print("Axis: {}".format(plt.axis()))
    plt.axis([0, 5, -1, 13])
    plt.title("With Axis set")
    plt.show()


if __name__ == '__main__':
    first_plots()
    quadratic_plot()
    better_quadratic_plot()
    multiline_plots()
    better_multiline_plots()
    adding_a_grid()
    setting_an_axis()
