#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/search-for-an-address/
# # Search for an address

# In[1]:


# imports
from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point

# Python Standard Library Modules
from IPython.display import display

gis = GIS()

geocode_result = geocode(address = "Hollywood sign", as_featureset = True)

# A list of features
geocode_result.features


# In[2]:


m = gis.map("Los Angeles, CA", zoomlevel = 11)


# In[3]:


m.draw(geocode_result)
m.clear_graphics()

location = {
     'Y': 34.13419,        # `Y` es latitud
     'X': -118.29636,      # `X` es longitud
     'spatialReference': {
         'wkid':4326
     }
}
unknown_pt = Point(location)

address = reverse_geocode(location = unknown_pt)
address


# In[4]:


m.draw(address)
m


# In[5]:


# Desafío
# Geocode multiple puntos de interés


# In[6]:


fish_query_portland = {
  'Address': 'fish tacos',
  'City': 'Portland',
  'Region': 'OR'
}

mf = gis.map('Portland, Oregon', zoomlevel = 11)

fish_tacos_places = geocode(fish_query_portland)

display(fish_tacos_places)


# In[7]:


for fish_taco_place in fish_tacos_places:
    mf.draw(fish_taco_place['location'])
    
mf

