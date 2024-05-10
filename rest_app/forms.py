from django import forms
from rest_app.models import *


#obicna forma bez da nasledue od models
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=20)


#forma za dodavanje na restaurants
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ["user"]

class DishForm(forms.ModelForm):
    class Meta:
        model: Dish
        fields = "__all__"