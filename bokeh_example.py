# Data handling
import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnarDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

output_file("empty_1.html", title="Empty Bokeh Figure")
output_notebook()
fig = figure()

show(fig)