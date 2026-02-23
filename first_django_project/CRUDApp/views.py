from django.shortcuts import render
from .forms import Empform
from .models import Emp_detail
from django.shortcuts import redirect

# Create your views here.
def createdata(request):
    form = Empform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('displayData')
    return render(request, "createform.html", {'form': form})

def get_all_data(request):
    data = Emp_detail.objects.all()
    return render(request, "displayEmp.html", {'data': data})