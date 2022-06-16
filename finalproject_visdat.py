# -*- coding: utf-8 -*-
"""finalproject_visdat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bc6_4gb75EVXxPdvsvYweiT_CM-p2Xo9

---



---

**FINAL PROJECT VISUALISASI DATA**


Disusun Kelompok 2 :



*   Adhyaksa Diffa Maulana  ( )

*   Habib Alfarabi ( 1301194170 )

*   Tiara Febriyanti (  ) 


---



---
"""

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models.widgets.sliders import DateRangeSlider
from bokeh.layouts import row, column, gridplot
from bokeh.models import Slider, Select
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.models.widgets import Tabs, Panel

data = pd.read_csv("covid19.csv", parse_dates=['date'])
data.head()

data["Name"] = "DataCovid"
data

data['Name'].unique()

newDS1 = data
newDS1 = newDS1.sort_values(['date', 'Name'])
newDS1.head()

DataCovid = newDS1[newDS1['Name'] == 'DataCovid']
output_notebook()

DataCovid

curdoc().theme = "dark_minimal"
output_notebook()

output_file('index.html',
            title='data terkonfirmasi positif berdasarkan kurun waktu')
dt_covid = ColumnDataSource(DataCovid)

tooltips = [('Name', '@Name'), ('acc_confirmed', '@acc_confirmed'), ('new_confirmed', '@new_confirmed'),('acc_negative', '@acc_negative')]

covidFig = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='acc confirmed',  tooltips=tooltips)

covidFig2 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='new confirmed',  tooltips=tooltips)

covidFig3 = figure(x_axis_type= 'datetime',
                  plot_height=500, plot_width=1000,
                  title='data covid', 
                  x_axis_label='Tanggal', y_axis_label='acc negative',  tooltips=tooltips)

covidFig.line('date', 'acc_confirmed', 
         color='red', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig2.line('date', 'new_confirmed', 
         color='yellow', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig3.line('date', 'acc_negative', 
         color='green', legend_label='DataCovid',
         line_width=1, 
         source=dt_covid)

covidFig.legend.location = 'top_left'
covidFig2.legend.location = 'top_left'
covidFig3.legend.location = 'top_left'

covidFig.legend.click_policy = 'hide'
covidFig2.legend.click_policy = 'hide'
covidFig3.legend.click_policy = 'hide'

date_slider_acc = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_acc.js_link('value', covidFig.x_range, 'start', attr_selector=0)
date_slider_acc.js_link('value', covidFig.x_range, 'end', attr_selector=1)

date_slider_new = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_new.js_link('value', covidFig2.x_range, 'start', attr_selector=0)
date_slider_new.js_link('value', covidFig2.x_range, 'end', attr_selector=1)

date_slider_neg = DateRangeSlider(value=(min(newDS1['date']), max(newDS1['date'])),
                              start=min(newDS1['date']),end=max(newDS1['date']),width=300)
date_slider_neg.js_link('value', covidFig3.x_range, 'start', attr_selector=0)
date_slider_neg.js_link('value', covidFig3.x_range, 'end', attr_selector=1)

layout1 = row(date_slider_acc, covidFig)
layout2 = row(date_slider_new, covidFig2)
layout3 = row(date_slider_neg, covidFig3)

cv = Panel(child= layout1, title='acc_confirmed')
cv2 = Panel(child= layout2, title='new_confirmed')
cv3 = Panel(child= layout3, title='acc_negative')

tabs = Tabs(tabs=[cv, cv2, cv3])

curdoc().add_root(tabs)
show(tabs)