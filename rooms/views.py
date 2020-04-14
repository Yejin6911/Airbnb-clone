# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage

from django.utils import timezone
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
    page_kwarg = 'page' # page인자값 이름
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context