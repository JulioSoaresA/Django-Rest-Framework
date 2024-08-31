from django.urls import path
from .views import estudantes

urlpatterns = [
    path('estudantes/', estudantes)
]
