import pandas as pd
from math import pi
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

df = pd.read_csv("Successofgenres.csv");
# 
output_file("Top30Movies.html")
df.Title = df.date + ' - ' + df.Title
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
p = figure(x_range=df.Title, plot_width=800, title="Top 30 Movies in Action - Action - Buddy Comedy",
           tools=TOOLS, toolbar_location='below',x_axis_label='Date - movie name', y_axis_label='Lifetime Gross',
           tooltips=[('Date - movie name', '@x'), ('Lifetime Gross', '@top')])
df.LifetimeGross= [float(s.replace(',', '')) for s in df.LifetimeGross]
print(df.LifetimeGross)
p.vbar(x=df.Title, top=df.LifetimeGross, width=0.4, color="#CAB2D6", legend= "Lifetime Gross")
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")
p.xaxis.major_label_orientation = pi / 2
 
show(p)


