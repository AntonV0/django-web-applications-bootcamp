from django.db import models

# Create your models here.

# Models are Python classes that represent database tables. Each attribute of the model represents a database field.
# Django provides a variety of field types, such as CharField for strings, IntegerField for integers, DecimalField
# for decimal numbers, EmailField for email addresses, DateField for dates, etc.

# They have constraints such as primary key, unique, null, blank, etc.
# By default, Django adds an auto-incrementing primary key field called id to each model.

# Once migrated, this class will create a table in the database with the given columns.
class Employee(models.Model): # models.Model is the base class for all models in Django.
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    date = models.DateField()
    age = models.IntegerField()

    # This changes the name in Employees database (in Django admin panel) from "Employee object (1)" to the actual name.
    def __str__(self): # This method is used to return a string representation (employee name) of the object.
        return self.name