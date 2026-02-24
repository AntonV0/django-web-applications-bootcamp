from django.shortcuts import render, redirect
from .forms import Empform
from .models import Emp_detail

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

def update_data(request, emp_id):
    # instead of E_id we can also use pk (primary key) if Ids are 1,2,3... and so on
    data = Emp_detail.objects.get(E_id=emp_id)
    form = Empform(instance=data)
    if request.method == 'POST':
        form = Empform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('displayData')
    else:
        form = Empform(instance=data)

    return render(request, "createform.html", {'form': form})

def delete_data(request, emp_id):
    data = Emp_detail.objects.get(E_id=emp_id)
    data.delete()
    return redirect('displayData')


