<<<<<<< HEAD
import requests
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from show_weather.models import added_cities
from django.contrib import messages



def index(request):
    return render(request, 'home.html')


def add_city(request):
    city = request.POST['city']
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=APIKEY'
    r = requests.get(url .format(city))
    if r.status_code==404:
        messages.success(request,"Belə şəhər tapılmadı")
        return render(request,'home.html')
    elif r.status_code==200:
        cities_weather = json.loads(r.text)
        city_weather = {
        'city': city,
        'temprature': cities_weather['main']['temp'],
        'description': cities_weather['weather'][0]['description'],
        'icon': cities_weather['weather'][0]['icon'],
        }
        context = {'city_weather': city_weather}
        return render(request, 'home.html',context)

=======
import requests
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from show_weather.models import added_cities
from django import VERSION


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=APIKEY'
    # cities = added_cities.objects.order_by('-added_time')
    # all_cities = added_cities.objects.all()

    first_city = added_cities.objects.all()[0].city_name

    city = first_city
    r = requests.get(url.format(city))
    cities_weather = json.loads(r.text)
    city_weather = {
        'city': city,
        'temprature': cities_weather['main']['temp'],
        'description': cities_weather['weather'][0]['description'],
        'icon': cities_weather['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}
    return render(request, 'home.html', context)


def add_city(request):
    added_cities.objects.all().delete()
    city = request.POST['city']
    current_time = timezone.now()
    added_cities.objects.create(added_time=current_time, city_name=city)
    return HttpResponseRedirect('/')
>>>>>>> 2001d54b7f6aa08db2779480e425bd1c54579a2f
