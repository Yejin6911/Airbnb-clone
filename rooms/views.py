from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

from django.views.generic import ListView
from . import models


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/room_list.html", context={"page": rooms})
#     except EmptyPage:
#         return redirect("/")

class HomeView(ListView):
    """ HomeView Definition  """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = 'page'  # page인자값 이름
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()

