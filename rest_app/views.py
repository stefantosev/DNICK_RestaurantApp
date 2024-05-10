from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from rest_app.models import *
from rest_app.forms import *


# Create your views here.
def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurants.html", {"restaurants": restaurants, "new_var": 1})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return HttpResponse(f"<p>Restaurant details for restaurant with id= {restaurant_id}.</p>"
                        f"<p>Restaurant name: {restaurant.name}, capacity: {restaurant.capacity}</p>")

def index(request):
    if request.method == "GET":
        form = NameForm(request.POST)
        if form.is_valid():
            request.session['your_name'] = form.cleaned_data['your_name']

    #if it's a GET method
    else:
        form = NameForm()

    #ako ne si najaven da te prikazue kako anonymous
    if 'your_name' not in request.session:
        your_name = "Anonymous"
    else:
        your_name = request.session['your_name']

    return render(request, "index.html", {"form": form, "your_name": your_name})

def dishes(request):
    dishes = Dish.objects.all()
    return render(request, "dishes.html", {"dishes": dishes, "count": len(dishes)})

def dish_detail(request, dish_id):
    try:
        dish = Dish.objects.get(id=dish_id)
    except Dish.DoesNotExist:
        raise Http404("Dish not found")
    return HttpResponse(dish)

def employees(request):
    employees = Employee.objects.all()
    return render(request, "employees.html", {"employees" : employees} )

#Rabota so forms
def add_restaurant(request):
    if request.method == "POST":
        restaurant = RestaurantForm(request.POST)
        if restaurant.is_valid():
            restaurant.save()
    else:
        restaurant = RestaurantForm()
    return render(request, "add_restaurants.html", {"form": restaurant})


# TODO: DOES NOT WORK
def add_dish(request):
    if request.method == "POST":
        dish = DishForm(request.POST)
        if dish.is_valid():
            dish.save()
    else:
        dish = DishForm()
    return render(request, "add_dish.html", {"form": dish})

def add_employee(request):
    if request.method == "POST":
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            if not request.user.is_anonymous:
                employee.instance.user = request.user
                employee.save()
                employee = EmployeeForm()
            else:
                employee.add_error(None, "You must log in.")
        else:
            print(employee.errors)  #console print
    else:
        employee = EmployeeForm()
    return render(request, "add_employee.html", {"form": employee})