from django.core.serializers import serialize
from rest_framework.views import APIView
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from .models import Counties_2021
import json
# Create your views here.


class sendPoly(APIView):
    def get(self,request):
        poly=serialize('geojson',Counties_2021.objects.all(),geometry_field='geom',fields=('county', 'county_id', 'homicide', 'robbery', 'breakings', 'stock_thef', 'stealing', 'vehicle_th', 'economic_c', 'corruption', 'population', 'crimes', 'crime_inde', 'd_drugs'))
        geom=poly
        return Response({"result":geom})
