from django.urls import path
from . import views

urlpatterns = [
    path('createdata/', views.createdata, name='createData'),
    path('displayData/', views.get_all_data, name='displayData'),
]