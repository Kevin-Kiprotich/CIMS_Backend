from django.contrib.gis import admin
from .models import Counties_2021

# Register your models here.
class Counties_2021Admin(admin.ModelAdmin):
    list_display=("county","county_id",)
admin.site.register(Counties_2021,Counties_2021Admin)