#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/display-a-web-map/
# # Display a web map

# In[1]:


#imports
from arcgis.gis import GIS
from arcgis.mapping import WebMap
from IPython.display import display

gis = GIS()

webmap = gis.content.get('41281c51f9de45edaf1c8ed44bb10e30')
display(webmap)

la_parks_trails = WebMap(webmap)
la_parks_trails


# In[ ]:


# Desafío


# In[2]:


operational_layers = la_parks_trails.layers
n = len(operational_layers)
print ("El Webmap tiene {} capas".format(n))


# In[3]:


for layer in operational_layers:
    print("{}\n\t{}".format(layer['id'], layer['url']))


# In[ ]:




