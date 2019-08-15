import pandas as pd
from math import pi
from bokeh.plotting import show
from bokeh.models import NumeralTickFormatter
from bokeh.models import ColumnDataSource, ranges, LabelSet

df = pd.read_csv("X-Men2011.csv", encoding = "iso-8859-1");
 
from bokeh.io import show, output_file
from bokeh.plotting import figure
unDf= df
y = list(zip(df.Rank, df.WeeklyGross))
output_file("bars.html")
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
source = ColumnDataSource(dict(x=df.Date,rank=df.Rank))
p = figure(x_range=df.Date,  plot_width=800, title="Weekly Gross of X-Men:First Class in 2011",
           tools=TOOLS, toolbar_location='below', x_axis_label='Date time', y_axis_label='Weekly gross',
           tooltips=[('date', '@x'), ('weekly gross', '@top')])
labels = LabelSet(x='x', y='rank', text='rank', level='glyph',
        x_offset=-13.5, y_offset=400, source=source, render_mode='canvas')


for index, row in df.iterrows():
    if(row.Rank <= 10): 
        unDf = unDf.drop([index])
    else:
        df=df.drop([index])
# print(df)
p.vbar(x=df.Date, top=df.WeeklyGross, width=0.9, color="#bd0026",legend="Top 10")
p.vbar(x=unDf.Date, top=unDf.WeeklyGross, width=0.9, color="#fed976",legend="Below than Top 10" )
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")
p.xaxis.major_label_orientation = pi / 3
p.add_layout(labels)
show(p)