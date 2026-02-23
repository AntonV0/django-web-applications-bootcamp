from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_django_app.urls')),
    path("employee_list/", views.employee_list, name="employee_list"),
]