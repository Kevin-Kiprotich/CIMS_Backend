from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Counties_2021


counties_mapping = {
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

county_shp =  "shapes/shapes/data/counties_2021.shp"


def run(verbose=True):
    lm = LayerMapping(Counties_2021,county_shp, counties_mapping)
    lm.save(strict=True, verbose=verbose)