from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Emp_class_view_model

class HomeClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to the Class-Based View in Django!'
        return context

class EmployeeListView(ListView):
    model = Emp_class_view_model
    template_name = 'employeeClass.html'
    context_object_name = 'employees'
