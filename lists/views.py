from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from rooms import models as room_models
from . import models

def toggle_room(request, room_pk):
    action = request.GET.get("action", None)
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None and action is not None:
        #tuple로 반환되는 것을 unpack하기 위해 두 변수로 지정
        the_list, created = models.List.objects.get_or_create(
            user=request.user, name="My Favorites Houses"
        )
        if action == 'add':
            the_list.rooms.add(room)
        elif action == 'remove':
            the_list.rooms.remove(room)
        return(redirect(reverse("rooms:detail", kwargs={"pk":room_pk})))

class SeeFavsVeiw(TemplateView):

    template_name = "lists/list_detail.html"