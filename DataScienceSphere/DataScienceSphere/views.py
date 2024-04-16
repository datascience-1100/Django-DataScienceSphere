from django.http import HttpResponse
from django.shortcuts import render
 

def homepage(request):
    data={
        'title': "Home New",
    }
    return render(request, "index.html", data)

def python(request):
    return render(request, "python.html")

 
 