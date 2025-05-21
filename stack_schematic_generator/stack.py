from .coordinate import Coordinate
import matplotlib.pyplot as plt
import numpy as np
from .layer import Layer

class Stack(object):
    """
    Stack class for managing and plotting a collection of layers.

    Attributes
    ----------
    layers : list
        List of Layer objects representing the stack.
    """

    def __init__(self, layers: list[Layer]):
        """
        Initialize the Stack with a list of layers.

        Parameters
        ----------
        layers : list
            List of Layer objects to be managed in the stack.
        """
        self.layers:list[Layer] = layers

    def get_height(self) -> float:
        """
        Calculate and return the total height of the stack.

        Returns
        -------
        float
            The sum of the heights and positive slopes of all layers in the stack.
        """
        return np.sum([layer.hight+np.max([layer.slope, 0]) for layer in self.layers])

    def plot(
            self,
            fig: plt.Figure = None,
            ax: plt.Axes = None,
            delta_figsize: tuple[float, float] = (1.6, 0.3)
    ) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot the stack using matplotlib.

        Parameters
        ----------
        fig : tuple, optional
            figure to plot on. If None, a new figure and axes are created.
        ax : tuple, optional
            axes to plot on. If None, a new figure and axes are created.
        delta_figsize : tuple, optional
            Size scaling factors for the figure.

        Returns
        -------
        fig : matplotlib.figure.Figure
            The matplotlib figure object.
        ax : matplotlib.axes.Axes
            The matplotlib axes object.
        """
        if (fig is None) or (ax is None):
            fig, ax = plt.subplots(figsize=(delta_figsize[0], delta_figsize[1] * self.get_height()))

        xy = Coordinate(0, 0, 1, 0)

        for i, layer in enumerate(self.layers):
            layer.plot(ax, xy, delta_figsize)

        ax.set_xlim(0, xy.get_x_max())
        ax.set_ylim(0, xy.get_y_max())
        ax.set_axis_off()

        return fig, ax