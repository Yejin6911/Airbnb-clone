from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """
    fieldsets = (
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "Basic Info",
            {"fields": ("name", "description","country","address","price")}
        ),
        (
            "Times",
            {"fields": ("check_in","check_out","instant_book")}
        ),
        (
            "More About the Space",
            {
                "classes":("collapse",),
                "fields":("amenities","facilities","house_rules")
            }
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        ),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

   # ordering = ('name','price','bedrooms')

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city","^host__username",) #foreignkey로 host의 username 접금할 때 다음과 같이 사용

    filter_horizontal = ("amenities","facilities","house_rules",)

    def count_amenities(self, obj):
        return len(obj.amenities.all())

    count_amenities.short_description = "amenities"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """
    pass