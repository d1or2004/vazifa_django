from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def liblary(request):
    return HttpResponse("Hello, world. You're at the")


def about(request):
    return HttpResponse("Hi developpers. You're at the")
