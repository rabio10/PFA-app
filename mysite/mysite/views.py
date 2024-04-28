from django.http import HttpResponse
from django.shortcuts import render     #allow us to render a html template

def home(request):
    #return HttpResponse("about")
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')