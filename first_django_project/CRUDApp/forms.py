from django import forms
from .models import Emp_detail

class Empform(forms.ModelForm):
    class Meta:
        model = Emp_detail
        fields = ['E_name', 'E_id', 'E_address', 'E_salary']
        # or you can use fields = '__all__' to include all fields