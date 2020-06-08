#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/share-maps-and-layers/
# # Share maps and layers

# In[1]:


# imports
from arcgis.gis import GIS

# Python Standard Library Modules
import os
import passwords
from IPython.display import display

# conexión con usuario
gis = GIS("https://www.arcgis.com", passwords.user_name, passwords.password)

search_results = gis.content.search(query = 'title: "Parks*" AND type: "Feature Service"')
display(search_results)


# In[2]:


feature_layer_item = search_results[0]
display(feature_layer_item)


# In[3]:


# Compartir de manera pública la capa
feature_layer_item.share(everyone = True)

