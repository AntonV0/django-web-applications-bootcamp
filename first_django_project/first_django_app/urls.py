from django.urls import path
from . import views

# ? Here, we are routing using URL patterns.
# When the user visits the root URL (''), the home view will be called.
# To see the home view in the live server/browser, we need to add the URL pattern to the end of the URL.
# For example, add /home to http://127.0.0.1:8000/home/

urlpatterns = [
    # Dynamic URL pattern with parameters (name1 and place1) that will be passed to the home view.
    # e.g. http://127.0.0.1:8000/home/Anton/United%20Kingdom/ will pass "Anton" as name1 and "United Kingdom" as place1.
    path('home/<str:name1>/<str:place1>/', views.home, name='home1'),
    path('about/', views.about, name='about1'),
    path('contact/', views.contact, name='contact1'),
]

# ? URL requests user can send to the server:
# GET - this is the most common type of request, used to retrieve data from the server.
# When a user visits a URL in their browser, they are sending a GET request to the server.
# E.g. GET home/Anton/United%20Kingdom/ will call the home view with name1="Anton" and place1="United Kingdom".

# POST - this type of request is used to send data to the server, often when submitting a form.
# PUT - this type of request is used to update existing data on the server.
# DELETE - this type of request is used to delete data from the server.
# PATCH - this type of request is used to partially update existing data on the server.