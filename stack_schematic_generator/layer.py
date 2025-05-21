from .coordinate import Coordinate

class Layer(object):
    """
    Represents a single layer in the stack schematic.

    Attributes
    ----------
    label : str
        The label of the layer.
    color : str
        The color of the layer.
    width : float
        The width of the layer.
    height : float
        The height of the layer.
    slope : float
        The slope of the layer.
    """

    def __init__(self, label:str, color:str, width:float=1, height:float=1, slope:float=0):
        """
        Initialize the Layer object.

        Parameters
        ----------
        label : str
            The label of the layer.
        color : str
            The color of the layer.
        width : float, optional
            The width of the layer (default is 1).
        height : float, optional
            The height of the layer (default is 1).
        slope : float, optional
            The slope of the layer (default is 0).
        """
        self.label = label
        self.color = color
        self.width = width
        self.height = height
        self.slope = slope

    def plot(self, ax, xy:Coordinate, delta_figsize:list, font_size="small"):
        """
        Plot the layer as a polygon and add its label to the given axes.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axes on which to plot the layer.
        xy : Coordinate
            The coordinate object defining the position and orientation.
        delta_figsize : list
            The change in figure size [width, height].
        font_size : str or int, optional
            The font size for the label (default is "small").
        """
        if self.label is not None:
            ax.add_patch(xy.get_polygon(self, delta_figsize))
            ax.text(xy.x_center, xy.y_center, self.label, va="center", ha="center", size=font_size, rotation=xy.rotation)