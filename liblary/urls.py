from django.urls import path
from .views import liblary, about

urlpatterns = [
    path('library/', liblary),
    path('about/', about)
]
