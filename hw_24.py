from bokeh.plotting import figure, output_file, show
from bokeh.models import widgets
from bokeh.io import output_notebook
import numpy as np

output_notebook()
import bokeh.sampledata
bokeh.sampledata.download()
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]


source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

p = figure(x_range=fruits, y_range=(0,9),plot_height=300,
           title="Fruit Counts",toolbar_location=None, tools="")
p.vbar(x="fruits",top="counts",width=0.5,color="color",legend_field="fruits",source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal" 
p.legend.location = "top_center"

show(p)from bokeh.models import FactorRange
from bokeh.transform import factor_cmap

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}


x = [ (fruit, year) for fruit in fruits for year in years ]
counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x,counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit Counts by Year")

p.vbar(x="x",top="counts",width=0.8,source=source,line_color="white",
       fill_color=factor_cmap('x', palette=["#99e0c5","#99d9e0","#99aae0"], factors=years, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = .1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
import bokeh.io
from bokeh.resources import INLINE
from bokeh.models import HoverTool
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show, output_notebook, ColumnDataSource
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd

bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)



hover = HoverTool(
    tooltips = [
        ("date", "@date"),
        ("close", "@open"),
        ("close", "@close"),
        ("high", "@high"),
        ("low", "@low"),
        ("volume","@volume")
    ], 
    formatters={"@date":"datetime"}
)



p = figure(
    plot_width=1000,
    plot_height=400,
    x_axis_type="datetime",
    tools=[hover,"pan,box_zoom,reset,save"]
)
p.title.text = 'Stock_Price--Click on legend entries to mute the corresponding lines and show daily details in hover'



for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    source = ColumnDataSource(df)
    p.line(x="date",y="close",line_width=2,color=color,
           muted_alpha=0.2,legend_label=name,source=source)


p.legend.location = "top_left"

p.legend.click_policy="mute"


show(p)
output_notebook()