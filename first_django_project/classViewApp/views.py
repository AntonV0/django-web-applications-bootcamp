from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from .models import Emp_class_view_model
from django.urls import reverse_lazy

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

class EmployeeCreateView(CreateView):
    model = Emp_class_view_model
    fields = ['name', 'age', 'place']
    template_name = 'employeeCreate.html'
    success_url = reverse_lazy('employee_list')  # Redirect to the employee list view after successful creation

# redirect(), reverse(), reverse_lazy() are used to redirect to a different URL after a successful operation.
# reverse_lazy() is used in class-based views because it allows us to reference the URL pattern
# by its name without needing to import the URL configuration at the top of the file. This is particularly useful
# when the URL patterns are defined in a different module or when there are circular imports. reverse is used in
# function-based views where we can directly import the URL configuration and reference the URL pattern by its name.
# redirect() is used to perform an immediate redirect to a different URL, while reverse() and reverse_lazy() are
# used to generate the URL based on the URL pattern name.