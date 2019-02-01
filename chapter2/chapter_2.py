"""Matplotlib for Python Developers - Chapter 2."""

import matplotlib.pyplot as plt
import numpy as np


def helper_decorate_plot(the_plot, title="", xlabel="", ylabel=""):
    """Helper function to set title, x and y labels."""
    the_plot.title(title)
    the_plot.xlabel(xlabel)
    the_plot.ylabel(ylabel)


def first_plots():
    """Plot 4 points."""
    plt.plot([1, 3, 2, 4])
    helper_decorate_plot(plt, "Plotting single values")
    plt.show()


def quadratic_plot():
    """Plot a quadratic function."""
    values = range(6)
    plt.plot(values, [x ** 2 for x in values])
    helper_decorate_plot(plt, "Quadratic function")
    plt.show()


def better_quadratic_plot():
    """Plot a quadratic function using NumPy array."""
    values = np.arange(0.0, 6.0, 0.1)
    plt.plot(values, [x ** 2 for x in values])
    helper_decorate_plot(plt, "Better Quadratic function with NumPy arange()")
    plt.show()


def multiline_plots():
    """Plot multiple lines."""
    values = range(1, 5)
    plt.plot(values, [x * 1.5 for x in values],
             values, [x * 3 for x in values],
             values, [x / 3 for x in values])
    helper_decorate_plot(plt, "Multiple lines with normal range()")
    plt.show()


def better_multiline_plots():
    """Plot multiple lines using NumPy array."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    helper_decorate_plot(plt, "Multiple lines with NumPy arange()")
    plt.show()


def adding_a_grid():
    """Plot on a figure with grid enabled."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    plt.grid(True)
    helper_decorate_plot(plt, "With a grid")
    plt.show()


def setting_an_axis_and_labels():
    """Plot on a figure with set axis limits."""
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5,
             values, values * 3,
             values, values / 3)
    print("Axis: {}".format(plt.axis()))
    plt.axis([0, 5, -1, 13])
    helper_decorate_plot(plt, title="With Axis set",
                         xlabel="This is the X axis",
                         ylabel="This is the Y axis")
    plt.show()


def displaying_the_legend():
    values = np.arange(1, 5)
    plt.plot(values, values * 1.5, label='Normal')
    plt.plot(values, values * 3, label='Fast')
    plt.plot(values, values / 3, label='Slow')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    first_plots()
    quadratic_plot()
    better_quadratic_plot()
    multiline_plots()
    better_multiline_plots()
    adding_a_grid()
    setting_an_axis_and_labels()
    displaying_the_legend()
