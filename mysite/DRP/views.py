from django.shortcuts import render

# Create your views here.
def DRP_app(request):
    return render(request, 'DRP/DRP_app.html')