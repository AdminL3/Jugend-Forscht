import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go

# Generate some sample data
np.random.seed(42)
x = np.random.rand(100, 1) * 10
y = 2.5 * x + np.random.randn(100, 1) * 2

# Create a DataFrame
data = pd.DataFrame({'x': x.flatten(), 'y': y.flatten()})

# Fit a linear regression model
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
# Assuming the DataFrame has columns 'feature' and 'target'
x = data[['x']]
y = data['y']

# Fit a linear regression model
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# Create a scatter plot with regression line using Plotly
fig = px.scatter(data, x='x', y='y', title='Scatter Plot with Regression Line')
fig.add_trace(go.Scatter(x=data['x'], y=y_pred.flatten(), mode='lines', name='Regression line'))

# Display the plot in Streamlit
st.plotly_chart(fig)