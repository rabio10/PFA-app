import plotly.graph_objs as go
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from . import forms

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/generale.html')

def generale(request):
    return render(request, 'DRP/generale.html')

def prevision(request):
    return render(request, 'DRP/prevision.html')

def historique(request):
    return render(request, 'DRP/historique.html')

def planification(request):
    return render(request, 'DRP/planification.html')

def parametre(request):
    return render(request, 'DRP/parametre.html')

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

# for the entrepot central form
def create_entrepot_central(request):
    if request.method == 'POST':
        form = forms.EntrepotCentralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = EntrepotCentralForm()
    
    return render(request, 'create_entrepot_central.html', {'form': form})