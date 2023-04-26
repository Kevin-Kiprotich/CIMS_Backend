from django.contrib import admin
from .models import AppUser,ReportedCrimes

# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display=("username","email","phone_number","emergency_contact",)
class ReportedCrimesAdmin(admin.ModelAdmin):
    list_display=('username','gender','latitude','longitude','image','audio','record_time',)
admin.site.register(AppUser,AppUserAdmin)
admin.site.register(ReportedCrimes,ReportedCrimesAdmin)