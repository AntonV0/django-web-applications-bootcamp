from django.urls import path
from . import views

urlpatterns = [
    path('createdata/', views.createdata, name='createData'),
    path('displayData/', views.get_all_data, name='displayData'),
    path('update/<emp_id>', views.update_data, name='update'),
    path('delete/<emp_id>', views.delete_data, name='delete')
]