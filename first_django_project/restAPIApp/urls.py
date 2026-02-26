from django.urls import path
from . import views
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetails.as_view(), name='book-details'),
]