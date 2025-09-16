from django.urls import path
from . import views

app_name = "first_app"
urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("getplace/", views.index, name="index"),
    path("place/", views.places, name="second_page"),
    path("details/", views.more_details, name="detailed_information"),
    path("add/", views.add, name="add_place"),
]
