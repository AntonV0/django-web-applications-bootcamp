from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .models import Employee

# Create your views here.

# ? Views are functions that take a web request and return a web response.
# ? Urls are mapped to views in the urls.py file. When a user visits a URL,
#  the corresponding view is called and returns a response.

def home(request, name1, place1):
    # ? This view will return a simple HttpResponse with the text "Hello World" in green color:
    # return HttpResponse("<h1 style='color:green;'>Hello World</h1>")
    # ? Instead of returning a simple HttpResponse, we can render an HTML template. This allows us to separate the
    #  presentation logic from the business logic. The render function takes the request, the template name, and an
    #  optional context dictionary that can be used to pass data to the template.

    # name = name1 # Pass data to the template using a context dictionary.
    # place = place1 # Dynamic data (name1 and place1) instead of static (e.g. name = "John", place = "New York")

    # Better way to format the context dictionary:
    context = {
        'name': name1,
        'place': place1
    }

    return render(request, 'home.html', context)
    # ? The built-in render function is a shortcut that combines a template with a context dictionary and returns an
    #  HttpResponse object with that rendered text. In this case, we are rendering the home.html template without any
    #  context data.

def about(request):
    all_data = Employee.objects.all()
    # This will display output in the console:
    # for data in all_data:
    #     print(data.name, data.salary, data.email, data.date, data.age)

    # This will display output on the webpage:
    context = {
        'all_data': all_data
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        # Here, we are retrieving the data from the POST request using the request.POST dictionary

        dict = {
            "username": username,
            "age": age,
            "email": email
        }
        csrf_token = get_token(request)
        print("CSRF Token:", csrf_token)
        return render(request, 'contact.html', dict)
    return render(request, 'contact.html')