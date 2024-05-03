import plotly.graph_objs as go
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/DRP_app.html')

def visualize_data(request):
    # Your code to prepare the dataframe
    # Example:
    data = {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines+markers', name='Data'))

    # Update layout for animation and effects
    fig.update_layout(
        title='Interactive Data Visualization',
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        template='plotly_dark',  # Choose a template for dark mode
        hovermode='x',  # Show hover info on nearest point on X axis
        xaxis=dict(type='category'),  # Set X axis type to category for discrete data
        updatemenus=[{'type': 'buttons',
                      'buttons': [{'label': 'Play',
                                   'method': 'animate',
                                   'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                                  }]
                     }]
    )

    # Add frames for animation (if needed)

    # Render the plotly graph as HTML
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)

    # Render the template with the Plotly graph
    return render(request, 'DRP/vis.html', {'plot_html': plot_html})