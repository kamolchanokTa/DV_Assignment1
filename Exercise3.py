import pandas as pd
from math import pi
from bokeh.plotting import figure, output_file, show
from datetime import datetime
from bokeh.models import NumeralTickFormatter
from pandas.core.frame import DataFrame
import numpy as np

df = pd.read_csv("Successofgenres.csv");
# 
output_file("Top30MoviesByYear.html")
df.LifetimeGross= [float(s.replace(',', '')) for s in df.LifetimeGross]
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
format_str = '%m/%d/%Y'
df.date = [str(datetime.strptime(date, format_str).year) for date in df.date]
 
newDF= DataFrame({"Movies":df.Title,"Year": df.date, "LifetimeGross":df.LifetimeGross} )
groupYearDF =newDF.groupby('Year');
GrossGrouped = groupYearDF.agg(np.sum).reset_index()
newDFSum = DataFrame({'Year': GrossGrouped.Year, 'LifetimeGross': GrossGrouped.LifetimeGross})
print(newDFSum)
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
p = figure(x_range=newDFSum.Year, plot_width=800, title="Top 30 Movies in Action - Action - Buddy Comedy",
           tools=TOOLS, toolbar_location='below',x_axis_label='Year', y_axis_label='Lifetime Gross',
           tooltips=[('Year', '@x'), ('Lifetime Gross', '@y')])
p.line(x=newDFSum.Year, y=newDFSum.LifetimeGross, line_width=2, legend= "Lifetime Gross") 
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")
p.xaxis.major_label_orientation = pi / 2
show(p)