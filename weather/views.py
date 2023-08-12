from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import requests
from .models import User
from datetime import datetime
# Create your views here.



def index(request):
     if not request.user.is_authenticated:
         return HttpResponseRedirect(reverse("login"))

     if request.user.is_authenticated:
        user = request.user

     location = user.location

     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=48797763c27bebcb04070c1c53182618'.format(location)

     res = requests.get(url)

     data = res.json()

     main = data['weather'][0]['main']

     description = data['weather'][0]['description']

     return render(request, 'FinalProject/index.html', {"data": data, "main": main,"description": description, "datetime": datetime.now().strftime("%d %b %Y | %I:%M:%S %p")})


def featured_weather(request):
     if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
     return render(request, 'FinalProject/news.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "FinalProject/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "FinalProject/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "FinalProject/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "FinalProject/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "FinalProject/register.html")


def find_weather(request):
     if request.method == "POST":
          location = request.POST["location"]

     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=48797763c27bebcb04070c1c53182618'.format(location)

     res = requests.get(url)

     data = res.json()

     main = data['weather'][0]['main']

     description = data['weather'][0]['description']

     return render(request, "FinalProject/find_weather.html", {"data": data, "location": location, "main": main, "datetime": datetime.now().strftime("%d %b %Y | %I:%M:%S %p")})


def get_weather(request, location):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=48797763c27bebcb04070c1c53182618'.format(location)

    res = requests.get(url)

    data = res.json()

    main = data['weather'][0]['main']

    description = data['weather'][0]['description']

    return render(request, "FinalProject/find_weather.html", {"data": data, "location": location, "main": main, "datetime": datetime.now().strftime("%d %b %Y | %I:%M:%S %p")})


@login_required
def profile_page(request):
    return render(request, "FinalProject/profile_page.html")


def change_location(request):
    if request.user.is_authenticated:
        user = request.user
    if request.method == "POST":
        location = request.POST["new-location"]

    user.location = location
    user.save()


    return HttpResponseRedirect(reverse("profile_page"))


def change_password(request):
    if request.user.is_authenticated:
        user = request.user
    if request.method == "POST":
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

    if password == confirm_password:
        user.password = password
        user.save()
    else:
        return render(request, "FinalProject/profile_page.html", {"message": "Passwords do not match."})

    return render(request, "FinalProject/profile_page.html", {"message": "Password changed successfully."})


def weather_maps(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "FinalProject/weather_maps.html", {"map_name": "wind_new"})


def find_map(request):
    if request.method == "POST":
        weather_map = request.POST["weather_map"]

    return render(request, "FinalProject/weather_maps.html", {"map_name": weather_map})
