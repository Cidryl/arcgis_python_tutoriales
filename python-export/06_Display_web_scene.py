#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/display-a-web-scene/
# # Display a web scene

# In[1]:


#imports
from arcgis.gis import GIS
from arcgis.mapping import WebScene
from IPython.display import display

gis = GIS()

webscene_search = gis.content.search(query = "LA Trails *", item_type = "Web Scene")
display(webscene_search)


# In[2]:


webscene_item = webscene_search[0]
display(webscene_item)


# In[3]:


la_trails = WebScene(webscene_item)
la_trails


# In[4]:


#Desafío


# In[5]:


operational_layers = la_trails['operationalLayers']
n = len(operational_layers)
print("The web scene has {} layers.".format(n))


# In[6]:


for layer in operational_layers:
    layers = layer['layers']
    for l in layers:
        print("{}\n\t{}".format(l['title'], l['url']))

