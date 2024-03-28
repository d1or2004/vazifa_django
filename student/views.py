from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def student(request):
    return render(request, 'data.html')


def data(request):
    return render(request, 'malumot.html')
