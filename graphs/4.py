from bokeh.plotting import figure, show
from bokeh.io import output_file

# Output to an HTML file
output_file("language_popularity.html")

# Data for the chart
x = ['Python', 'C++', 'Java', 'JavaScript']
y = [215, 130, 245, 210]

# Create a figure
p = figure(x_range=x, title="Language Popularity", toolbar_location=None, tools="")

# Add vertical bars
p.vbar(x=x, top=y, width=0.9)

# Show the plot in the browser
show(p)
