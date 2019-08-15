import pandas as pd
from math import pi
from bokeh.plotting import figure, output_file, show
from bokeh.models.ranges import Range1d
from bokeh.models import LinearAxis

df = pd.read_csv("Movies2018MarketShare.csv");
marketShare = df.MarketShare*100
output_file("line_bar.html")

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
p = figure(x_range=df.Distributor, plot_width=800, title="Top 38 Market share in 2018 ",
           tools=TOOLS, toolbar_location='below',x_axis_label='Distributor', y_axis_label='% of Market Share',
           tooltips=[('Distributor', '@x'), ('% of Market Share', '@top'), ('No. of Movies',"@y")])

# add a line renderer
p.line(x=df.Distributor, y=df.Movies, line_width=2, legend="No. of Movies",y_range_name='No. of Movies')
p.extra_y_ranges = {"No. of Movies": Range1d(start=0, end=100)}
p.add_layout(LinearAxis(y_range_name="No. of Movies",axis_label='No. of Movies'), 'right' )
# add bar renderer
p.vbar(x=df.Distributor, top=marketShare, width=0.4, color="#CAB2D6", legend= "% of Market Share")

# Setting the y  axis range   
p.y_range = Range1d(0, 100)
p.xaxis.major_label_orientation = pi / 2

show(p)