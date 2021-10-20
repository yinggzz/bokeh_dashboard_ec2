import pandas as pd
import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource,Select, Title, Legend, LegendItem
from bokeh.plotting import figure, curdoc, show

#for authentication
x=True

if (curdoc().session_context.request.arguments!={'username': [b'nyc'], 'password': [b'iheartnyc']}):
   x=False

if (x==True):
    df = pd.read_csv('cleanData.csv')

    x_axis=[1,2,3,4,5,6,7,8,9]
    all_y=df["all"].to_list()
    zipcode1=df["10001"].to_list()
    zipcode2=df["10002"].to_list()

    source = ColumnDataSource(data=dict(
        x=x_axis,
        y1=all_y,
        y2=zipcode1,
        y3=zipcode2,
    ))
    plot = figure(title="NYC_311 Service Monthly Response Time", width=400, height=400)
    plot.add_layout(Title(text="Month", align="center"), "below")
    plot.add_layout(Title(text="Average Response Time (hour)", align="center"), "left")

    plot.vline_stack(['y1', 'y2', 'y3'], color=["firebrick", "blue", "black"],
                     legend_label=["all", "zipcode1", "zipcode2"], x='x', source=source)

#features + SELECTORS:

    all_zips=list(df.columns.values)
    all_zips.pop(0)
    all_zips.pop(0)

    #text = TextInput(title="Title", value='NYC_311 Service Monthly Response Time')
    select_zipcode1 = Select(title = 'Choose Zip Code 1 (blue line)',
                        value = "10001",
                        options = all_zips)

    select_zipcode2 = Select(title = 'Choose Zip Code 2 (black line)',
                        value = "10002",
                        options = all_zips)

####CALLBACK#####

# Set up callbacks

    def update_data(attrname, old, new):

    # Get the current selector values
        zipOne = select_zipcode1.value
        zipTwo = select_zipcode2.value

    # Generate the new curve
        zipcode1 = df[zipOne].to_list()
        zipcode2 = df[zipTwo].to_list()

        source.data =dict(
            x=x_axis,
            y1=all_y,
            y2=zipcode1,
            y3=zipcode2,
        )

    for w in [select_zipcode1, select_zipcode2]:
        w.on_change('value', update_data)

########

#features:
    inputs = column(select_zipcode1, select_zipcode2,)

    curdoc().add_root(column(inputs, plot, width=800))
    curdoc().title = "nyc_dash"
