from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition  """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = 'page'  # page인자값 이름
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition  """

    model = models.Room
    pk_url_kwarg = 'potato'

def search(request):
    city=request.GET.get("city", "Anywhere")
    city=str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(request, "rooms/search.html", {"city": city, "countries": countries, "room_types":room_types})
