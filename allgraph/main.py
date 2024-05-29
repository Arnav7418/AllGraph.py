

import matplotlib.pyplot as plt
from typing import List, Tuple, Union, Optional
from matplotlib.colors import Normalize


def make_bar_graph(data_x: List[float], data_y: List[float], title: str = 'Bar Graph', xlabel: str = 'X-axis', ylabel: str = 'Y-axis', color: str = 'blue', alpha: float = 1.0, edgecolor: str = 'black', fontsize: int = 12, legend: bool = False, **kwargs):
    """
    Create a bar graph.

    Parameters:
        data_x (List[float]): Values for the x-axis. Example: [1, 2, 3, 4]
        data_y (List[float]): Values for the y-axis. Example: [10, 20, 30, 40]
        title (str, optional): Title of the graph. Defaults to 'Bar Graph'. Example: 'Sales Data'
        xlabel (str, optional): Label for the x-axis. Defaults to 'X-axis'. Example: 'Months'
        ylabel (str, optional): Label for the y-axis. Defaults to 'Y-axis'. Example: 'Revenue'
        color (str, optional): Color of the bars. Defaults to 'blue'. Example: 'red'
        alpha (float, optional): Transparency of the bars. Defaults to 1.0. Example: 0.5
        edgecolor (str, optional): Color of the edges of the bars. Defaults to 'black'. Example: 'gray'
        fontsize (int, optional): Font size for text elements. Defaults to 12. Example: 14
        legend (bool, optional): Whether to display the legend. Defaults to False. Example: True
        **kwargs: Additional keyword arguments for matplotlib bar function.
    """
    # Validation
    if len(data_x) != len(data_y):
        raise ValueError("data_x and data_y must be of the same length")

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data_x, data_y, color=color, alpha=alpha, edgecolor=edgecolor, **kwargs)
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    if legend:
        plt.legend(bars, [f'Bar {i+1}' for i in range(len(data_x))], fontsize=fontsize)
    plt.grid(True)
    plt.show()


def make_line_graph(data_x: List[float], data_y: List[float], title: str = 'Line Graph', xlabel: str = 'X-axis', ylabel: str = 'Y-axis', color: str = 'blue', linestyle: str = '-', marker: str = 'o', linewidth: float = 1.0, alpha: float = 1.0, markersize: float = 6.0, markeredgecolor: str = 'black', markeredgewidth: float = 1.0, markerfacecolor: str = 'blue', fontsize: int = 12):
    """
    Create a line graph.

    Parameters:
        data_x (List[float]): Values for the x-axis. Example: [1, 2, 3, 4]
        data_y (List[float]): Values for the y-axis. Example: [10, 20, 30, 40]
        title (str, optional): Title of the graph. Defaults to 'Line Graph'. Example: 'Sales Trend'
        xlabel (str, optional): Label for the x-axis. Defaults to 'X-axis'. Example: 'Months'
        ylabel (str, optional): Label for the y-axis. Defaults to 'Y-axis'. Example: 'Revenue'
        color (str, optional): Color of the line. Defaults to 'blue'. Example: 'red'
        linestyle (str, optional): Style of the line. Defaults to '-'. Example: '--'
        marker (str, optional): Marker style. Defaults to 'o'. Example: 's'
        linewidth (float, optional): Width of the line. Defaults to 1.0. Example: 2.0
        alpha (float, optional): Transparency of the line. Defaults to 1.0. Example: 0.5
        markersize (float, optional): Size of markers. Defaults to 6.0. Example: 8.0
        markeredgecolor (str, optional): Color of marker edges. Defaults to 'black'. Example: 'red'
        markeredgewidth (float, optional): Width of marker edges. Defaults to 1.0. Example: 2.0
        markerfacecolor (str, optional): Color of marker faces. Defaults to 'blue'. Example: 'green'
        fontsize (int, optional): Font size for text elements. Defaults to 12. Example: 14
    """
    # Validation
    if len(data_x) != len(data_y):
        raise ValueError("data_x and data_y must be of the same length")

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data_x, data_y, color=color, linestyle=linestyle, marker=marker, linewidth=linewidth, alpha=alpha, markersize=markersize, markeredgecolor=markeredgecolor, markeredgewidth=markeredgewidth, markerfacecolor=markerfacecolor)
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.grid(True)
    plt.show()


def make_histogram(data: List[float], title: str = 'Histogram', xlabel: str = 'X-axis', ylabel: str = 'Frequency', color: str = 'blue', bins: Union[int, List[float], str] = 10, range: Optional[Tuple[float, float]] = None, density: bool = False, cumulative: bool = False, histtype: str = 'bar', align: str = 'mid', orientation: str = 'vertical', rwidth: Optional[float] = None, fontsize: int = 12):
    """
    Create a histogram.

    Parameters:
        data (List[float]): Input data for the histogram. Example: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        title (str, optional): Title of the graph. Defaults to 'Histogram'. Example: 'Distribution of Scores'
        xlabel (str, optional): Label for the x-axis. Defaults to 'X-axis'. Example: 'Values'
        ylabel (str, optional): Label for the y-axis. Defaults to 'Frequency'. Example: 'Counts'
        color (str, optional): Color of the bars. Defaults to 'blue'. Example: 'green'
        bins (Union[int, List[float], str], optional): Number of bins or bin edges. Defaults to 10. Example: 20
        range (Optional[Tuple[float, float]], optional): Range of the histogram bins. Example: (0, 100)
        density (bool, optional): If True, the first element of the return tuple will be the counts normalized to form a probability density. Defaults to False. Example: True
        cumulative (bool, optional): If True, then a histogram is computed where each bin gives the counts in that bin plus all bins for smaller values. Defaults to False. Example: True
        histtype (str, optional): Type of histogram. Defaults to 'bar'. Example: 'step'
        align (str, optional): Controls how bars are aligned relative to their bin centers. Defaults to 'mid'. Example: 'left'
        orientation (str, optional): Orientation of the histogram. Defaults to 'vertical'. Example: 'horizontal'
        rwidth (Optional[float], optional): Relative width of bars as a fraction of bin width. Defaults to None. Example: 0.8
        fontsize (int, optional): Font size for text elements. Defaults to 12. Example: 14
    """
    # Plot
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, range=range, density=density, cumulative=cumulative, histtype=histtype, align=align, orientation=orientation, color=color, rwidth=rwidth)
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.grid(True)
    plt.show()




def make_pie_chart(labels: List[str], sizes: List[float], title: str = 'Pie Chart', colors: Optional[List[str]] = None, startangle: float = 0, explode: Optional[Union[List[float], Tuple[float, ...]]] = None, shadow: bool = False, autopct: Optional[str] = '%1.1f%%', pctdistance: float = 0.6, labeldistance: float = 1.1, radius: float = 1, counterclock: bool = True, wedgeprops: Optional[dict] = None, textprops: Optional[dict] = None, fontsize: int = 12):
    """
    Create a pie chart.

    Parameters:
        labels (List[str]): Labels for each wedge of the pie. Example: ['A', 'B', 'C']
        sizes (List[float]): Sizes of each wedge. Example: [10, 20, 30]
        title (str, optional): Title of the graph. Defaults to 'Pie Chart'. Example: 'Distribution of Scores'
        colors (Optional[List[str]], optional): Colors for the wedges. Defaults to None. Example: ['red', 'green', 'blue']
        startangle (float, optional): Start angle for the pie chart. Defaults to 0. Example: 90
        explode (Optional[Union[List[float], Tuple[float, ...]]], optional): Fraction of the radius with which to offset each wedge. Defaults to None. Example: (0, 0.1, 0)
        shadow (bool, optional): If True, draws a shadow beneath the pie. Defaults to False. Example: True
        autopct (Optional[str], optional): Format string for the labels inside the wedges. Defaults to '%1.1f%%'. Example: '%.1f%%'
        pctdistance (float, optional): Distance from the center of each pie wedge at which the text should be drawn. Defaults to 0.6. Example: 0.8
        labeldistance (float, optional): Radial distance at which the pie labels are drawn. Defaults to 1.1. Example: 1.2
        radius (float, optional): Radius of the pie. Defaults to 1. Example: 1.5
        counterclock (bool, optional): If True, the wedges are drawn counterclockwise. Defaults to True. Example: False
        wedgeprops (Optional[dict], optional): Properties (like linewidth, edgecolor) of the wedge objects making up the pie. Defaults to None. Example: {'linewidth': 2, 'edgecolor': 'black'}
        textprops (Optional[dict], optional): Properties (like fontsize, fontweight) of the text objects for the labels. Defaults to None. Example: {'fontsize': 12, 'fontweight': 'bold'}
        fontsize (int, optional): Font size for text elements. Defaults to 12. Example: 14
    """
    # Plot
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, colors=colors, startangle=startangle, explode=explode, shadow=shadow, autopct=autopct, pctdistance=pctdistance, labeldistance=labeldistance, radius=radius, counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops)
    plt.title(title, fontsize=fontsize)
    plt.show()



def make_scatter_plot(data_x: List[float], data_y: List[float], title: str = 'Scatter Plot', xlabel: str = 'X-axis', ylabel: str = 'Y-axis', color: str = 'blue', marker: str = 'o', s: Optional[Union[int, List[int]]] = None, alpha: float = 1.0, edgecolors: str = 'none', linewidths: float = 1.0, cmap: Optional[str] = None, norm: Optional[Normalize] = None, vmin: Optional[float] = None, vmax: Optional[float] = None, fontsize: int = 12):
    """
    Create a scatter plot.

    Parameters:
        data_x (List[float]): Values for the x-axis. Example: [1, 2, 3, 4]
        data_y (List[float]): Values for the y-axis. Example: [10, 20, 30, 40]
        title (str, optional): Title of the graph. Defaults to 'Scatter Plot'. Example: 'Relationship between X and Y'
        xlabel (str, optional): Label for the x-axis. Defaults to 'X-axis'. Example: 'X Values'
        ylabel (str, optional): Label for the y-axis. Defaults to 'Y-axis'. Example: 'Y Values'
        color (str, optional): Color of the markers. Defaults to 'blue'. Example: 'red'
        marker (str, optional): Marker style for data points. Defaults to 'o'. Example: 's'
        s (Optional[Union[int, List[int]]], optional): Size of markers. Defaults to None. Example: 50
        alpha (float, optional): Transparency of markers. Defaults to 1.0. Example: 0.8
        edgecolors (str, optional): Color of marker edges. Defaults to 'none'. Example: 'black'
        linewidths (float, optional): Width of marker edges. Defaults to 1.0. Example: 2.0
        cmap (Optional[str], optional): Colormap for mapping scalar data to colors. Defaults to None. Example: 'viridis'
        norm (Optional[Normalize], optional): Normalization instance for scaling scalar data to the colormap. Defaults to None.
        vmin (Optional[float], optional): Minimum scalar value for colormap normalization. Defaults to None.
        vmax (Optional[float], optional): Maximum scalar value for colormap normalization. Defaults to None.
        fontsize (int, optional): Font size for text elements. Defaults to 12. Example: 14
    """
    # Plot
    plt.figure(figsize=(10, 6))
    sc = plt.scatter(data_x, data_y, c=color, marker=marker, s=s, alpha=alpha, edgecolors=edgecolors, linewidths=linewidths, cmap=cmap, norm=norm, vmin=vmin, vmax=vmax)
    plt.colorbar(sc)  # Add colorbar if colormap is specified
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.grid(True)
    plt.show()


