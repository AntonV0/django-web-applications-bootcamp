from django.shortcuts import render
from .models import EmployeePage
from django.core.paginator import Paginator

# Create your views here.
def employee_list(request):
    employees = EmployeePage.objects.all().order_by('id')

    paginator = Paginator(employees, 6)  # Show 6 employees per page

    page_number = request.GET.get('page')

    page_data = paginator.get_page(page_number)

    return render(request, 'employee.html', {'page_data': page_data})