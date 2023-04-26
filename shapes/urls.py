from django.urls import path
from . import views

urlpatterns = [
    path('geometry/', views.sendPoly.as_view()),
]
