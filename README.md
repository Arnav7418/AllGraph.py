# AllGraph

AllGraph is a Python library for creating various types of charts and graphs, built on top of Matplotlib.

## Installation

You can install AllGraph via pip:

```bash
pip install allgraph


from allgraph import make_bar_graph, make_line_graph, make_histogram, make_pie_chart, make_scatter_plot

# Example data
data_x = [1, 2, 3, 4]
data_y = [10, 20, 30, 40]

# Create a bar graph
make_bar_graph(data_x, data_y, title='Sales Data', xlabel='Months', ylabel='Revenue', color='red', alpha=0.5, edgecolor='black', fontsize=14, legend=True)

# Create a line graph
make_line_graph(data_x, data_y, title='Sales Trend', xlabel='Months', ylabel='Revenue', color='blue', linestyle='--', marker='s', linewidth=2.0, alpha=0.8, markersize=8.0, markeredgecolor='red', markeredgewidth=2.0, markerfacecolor='green', fontsize=14)

# Create a histogram
make_histogram(data, title='Distribution of Scores', xlabel='Values', ylabel='Counts', color='green', bins=20, range=(0, 100), density=True, cumulative=True, histtype='step', align='left', orientation='horizontal', rwidth=0.8, fontsize=14)

# Create a pie chart
make_pie_chart(labels, sizes, title='Distribution of Scores', colors=['red', 'green', 'blue'], startangle=90, explode=(0, 0.1, 0), shadow=True, autopct='%.1f%%', pctdistance=0.8, labeldistance=1.2, radius=1.5, counterclock=False, wedgeprops={'linewidth': 2, 'edgecolor': 'black'}, textprops={'fontsize': 14, 'fontweight': 'bold'}, fontsize=14)

# Create a scatter plot
make_scatter_plot(data_x, data_y, title='Relationship between X and Y', xlabel='X Values', ylabel='Y Values', color='red', marker='s', s=50, alpha=0.8, edgecolors='black', linewidths=2.0, cmap='viridis', norm=None, vmin=None, vmax=None, fontsize=14)


