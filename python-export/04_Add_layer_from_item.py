#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/add-a-layer-from-an-item/
# # Add a layer from an item

# In[1]:


#imports
from arcgis.gis import GIS

#Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile
from IPython.display import display

trailheads_id = '883cedb8c9fe4524b64d47666ed234a7'

gis = GIS()

trailheads_item = gis.content.get(trailheads_id)
display(trailheads_item)


# In[2]:


#Agregar la capa
m = gis.map()
m.add_layer(trailheads_item)

m.center = [34.09042, -118.71511] # `[latitud, longitud]`
m.zoom = 11

m


# In[ ]:




