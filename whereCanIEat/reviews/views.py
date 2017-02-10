from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .models import Restaurant, Review


def index(request):
    return render(request, 'reviews/index.html', {})

def city(request, city):
    restaurant_list = Restaurant.objects.filter(city_name=city.capitalize())
    final_list = []
    for restaurant in restaurant_list:
        reviews = Review.objects.filter(name=restaurant.name)
        final_list.append({"name": restaurant.name, "food_type": restaurant.food_type, "comments": reviews})
    print final_list
    context = {'restaurant_list': final_list, 'city': city}
    return render(request, 'reviews/restaurants.html', context)

def add(request):
    return render(request, 'reviews/add.html')
