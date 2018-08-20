# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
#extra import to open csv file and read it
import csv
import plotly.tools as pt
import numpy as np
import pandas as pd
#api credentials
pt.set_credentials_file(username='ambikavohra136', api_key='uafwNR1xvc9LNOZw774x')

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
# Create new lists for words and their frequencies

#read csv file
df = pd.read_csv('noun_data.csv')

#create data trace for bar chart
data = [go.Bar(
                    x=df['Noun'], y=df['Number'], # Data
                    name='Most Frequently Used Nouns' # Additional options
                   )]

layout = go.Layout(title="Most Frequently Used Nouns")
n_figure = go.Figure(data=data, layout=layout)

py.plot(data, filename='part4_viz_image')
py.image.save_as(n_figure, filename='part4_viz_image.png')
