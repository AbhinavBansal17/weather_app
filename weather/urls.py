from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("featured_weather", views.featured_weather, name="featured_weather"),
    path("get_weather/<str:location>", views.get_weather, name="get_weather"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("find_weather", views.find_weather, name="find_weather"),
    path("profile_page", views.profile_page, name="profile_page"),
    path("change_location", views.change_location, name="change_location"),
    path("change_password", views.change_password, name="change_password"),
    path("weather_maps", views.weather_maps, name="weather_maps"),
    path("find_map", views.find_map, name="find_map"),

]