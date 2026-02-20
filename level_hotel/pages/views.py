from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def portfolio(request):
    return render(request,'portfolio.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')
