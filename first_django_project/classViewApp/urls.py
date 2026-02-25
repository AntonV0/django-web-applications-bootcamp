from django.urls import path
from . import views

urlpatterns = [
    path("template_view/", views.HomeClassView.as_view(), name="home"),
    path("list_view/", views.EmployeeListView.as_view(), name="employee_list"),
    path("create_view/", views.EmployeeCreateView.as_view(), name="employee_create"),
]