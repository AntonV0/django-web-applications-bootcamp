from django.shortcuts import render
from .forms import Empform

# Create your views here.
def createdata(request):
    form = Empform(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "createform.html")
    return render(request, "createform.html", {'form': form})
