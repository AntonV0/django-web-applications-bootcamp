from django.db import models

# Create your models here.
class Emp_detail(models.Model):
    E_name = models.CharField(max_length=100)
    E_id = models.CharField(max_length=50, unique=True)
    E_address = models.CharField(max_length=100)
    E_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.E_name