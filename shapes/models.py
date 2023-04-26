# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Counties_2021(models.Model):
    county = models.CharField(max_length=20)
    county_id = models.IntegerField()
    homicide = models.BigIntegerField()
    robbery = models.BigIntegerField()
    breakings = models.BigIntegerField()
    stock_thef = models.BigIntegerField()
    stealing = models.BigIntegerField()
    vehicle_th = models.BigIntegerField()
    economic_c = models.BigIntegerField()
    corruption = models.BigIntegerField()
    population = models.BigIntegerField()
    crimes = models.BigIntegerField()
    crime_inde = models.BigIntegerField()
    d_drugs = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    class Meta:
        verbose_name_plural="Counties_2021"


# Auto-generated `LayerMapping` dictionary for Counties_2021 model
counties_2021_mapping = {
    'county': 'COUNTY',
    'county_id': 'county_id',
    'homicide': 'HOMICIDE',
    'robbery': 'ROBBERY',
    'breakings': 'BREAKINGS',
    'stock_thef': 'STOCK_THEF',
    'stealing': 'STEALING',
    'vehicle_th': 'VEHICLE_TH',
    'economic_c': 'ECONOMIC_C',
    'corruption': 'CORRUPTION',
    'population': 'POPULATION',
    'crimes': 'CRIMES',
    'crime_inde': 'CRIME_INDE',
    'd_drugs': 'D_DRUGS',
    'geom': 'MULTIPOLYGON',
}
