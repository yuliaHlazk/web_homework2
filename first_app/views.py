from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import numpy as np
from .destinations import get_place
from .forms import NewPlaceForm


def all_places_session(request):
    user_session = request.session.get("places", [])
    return user_session + get_place


def index(request):
    a = get_place
    weights = np.array([p["rating"] for p in a])
    weights = weights / weights.sum()
    selected_place = np.random.choice(a, p=weights)

    return render(request, "first_app/index.html", {"place": selected_place})


def places(request):
    return render(
        request, "first_app/allplaces.html", {"places": all_places_session(request)}
    )


def first_page(request):
    return render(request, "first_app/first_page.html")


def more_details(request):
    if request.method == "GET":
        name = request.GET.get("name")

        for place in all_places_session(request):
            if place["name"] == name:
                return render(request, "first_app/more_details.html", {"place": place})


def add(request):
    if request.method == "POST":
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            # task = form.cleaned_data['task']
            place = {
                "name": form.cleaned_data["name"],
                "location": form.cleaned_data["location"],
                "description": form.cleaned_data["description"],
                "type": form.cleaned_data["type"],
                "rating": form.cleaned_data["rating"],
                "date_created": date.today().strftime("%Y-%m-%d"),
            }

            if "places" not in request.session:
                request.session["places"] = []
            request.session["places"].append(place)

            request.session.modified = True  # уточнити за зберігання

            return HttpResponseRedirect(reverse("first_app:second_page"))
        else:
            return render(request, "first_app/addplace.html", {"form": form})
    return render(request, "first_app/addplace.html", {"form": NewPlaceForm()})
