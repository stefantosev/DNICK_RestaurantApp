from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from rest_app.models import *


# Create your views here.
def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurants.html", {"restaurants": restaurants, "new_var": 1})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return HttpResponse(f"<p>Restaurant details for restaurant with id= {restaurant_id}.</p>"
                        f"<p>Restaurant name: {restaurant.name}, capacity: {restaurant.capacity}</p>")

def index(request):
    return render(request, "index.html")

def dishes(request):
    dishes = Dish.objects.all()
    return render(request, "dishes.html", {"dishes": dishes, "count": len(dishes)})

def dish_detail(request, dish_id):
    try:
        dish = Dish.objects.get(id=dish_id)
    except Dish.DoesNotExist:
        raise Http404("Dish not found")
    return HttpResponse(dish)