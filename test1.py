# Archivo .py para clase PullRequest

import pandas as pd
import numpy as np

# Crear data Frame y gráfico

import plotly.express as px

# Create a list of dates
dates = pd.date_range('2023-06-03', periods=10)

# Create a list of values
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a dataframe
df = pd.DataFrame({'Date': dates, 'Value': values})

# Plot the dataframe in Plotly
fig = px.line(df, x='Date', y='Value')
fig.show()