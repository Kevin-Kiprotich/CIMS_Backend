from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class AppUser(AbstractUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(null=False,blank=False)
    emergency_contact=models.CharField(null=True)
    platform=models.CharField(max_length=10,default="website")
    gender=models.CharField(max_length=20,default="male")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        app_label="users"
        verbose_name_plural="App Users"

class ReportedCrimes(models.Model):
    email=models.EmailField(null=True)
    username=models.CharField(max_length=50,null=True)
    record_time=models.DateTimeField(auto_now=True,)
    latitude=models.FloatField()
    longitude=models.FloatField()
    crimetype=models.CharField(null=True,max_length=30)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='media/Images',null=True)
    gender=models.CharField(max_length=10)
    audio=models.FileField(upload_to="media/Audio",null=True)
    platform=models.CharField(max_length=10,default="mobile")
    class Meta:
        verbose_name_plural="Reported Crimes"
