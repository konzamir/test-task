from django.shortcuts import render

# Create your views here.

def display(request, *a, **k):
    return render(request, 'swagger/index.html', {})