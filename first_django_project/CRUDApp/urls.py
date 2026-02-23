from django.urls import path
from . import views

urlpatterns = [
    path('createdata/', views.createdata, name='createdata'),
]