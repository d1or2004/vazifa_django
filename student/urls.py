from django.urls import path
from .views import student, data

urlpatterns = [
    path('student/', student),
    path('data/', data),
]
