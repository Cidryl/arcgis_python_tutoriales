#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/find-places/
# # Find places

# In[1]:


from arcgis.gis import GIS
from arcgis.geocoding import geocode
from IPython.display import display

gis = GIS()

geocode_fs = geocode(
    address       = None,
    location      = [-118.71511, 34.09042],
    #category      = "Coffee shop",
    category      = "Coffee shop, Gas station, Food, Hotel",
    out_fields    = "Place_addr, PlaceName",
    max_locations = 25,
    as_featureset = True
)

# Convierta los resultados en un marco de datos de Pandas 
# llamando a la propiedad sdf de un FeatureSet y muestre 
# las dos primeras ubicaciones.

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

geocode_df = geocode_fs.sdf
geocode_df.head(2)

m = gis.map()
m.center = [34.09042, -118.71511] # `[latitud, longitud]`
m.zoom = 11

m.draw(geocode_fs)

m

