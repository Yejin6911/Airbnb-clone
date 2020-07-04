from django.shortcuts import render, redirect
from django.urls import reverse

from rooms import models as room_models
from . import models

def save_room(request, room_pk):
     room = room_models.Room.objects.get_or_none(pk=room_pk)
     if room is not None:
         #tuple로 반환되는 것을 unpack하기 위해 두 변수로 지정
         the_list, created = models.List.objects.get_or_create(
             user=request.user, name="My Favorites Houses"
         )
         the_list.rooms.add(room)
         return(redirect(reverse("rooms:detail", kwargs={"pk":room_pk})))
