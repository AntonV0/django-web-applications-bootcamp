from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Book
from .serializer import BookSerializer

class BookList(APIView):
    # ? APIView is a base class provided by Django REST Framework to create class-based APIs.
    # ? It is used to:
    # 1. Handle HTTP methods (GET, POST, PUT, DELETE) in a class-based manner.
    # 2. Parse JSON to Python data and vice versa.
    # 3. Return proper API responses with status codes and content types.
    # 4. Handle authentication and permissions for API endpoints.

    def get(self, request):
        # ? The get method is used to handle GET requests to the API endpoint. It retrieves data from the database,
        # ? serializes it, and returns it in the response.

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer:", serializer.data)
        return Response(serializer.data)

    def post(self, request):
        # ? The post method is used to handle POST requests to the API endpoint. It takes the data from the request,
        # ? deserializes it, validates it, and saves it to the database if it's valid.

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)