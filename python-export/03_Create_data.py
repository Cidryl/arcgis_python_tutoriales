#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/create-data/
# # Create Data

# In[1]:


#imports
from arcgis.gis import GIS

#Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile
from IPython.display import display

import os
import passwords

#conexión con usuario
gis = GIS("https://www.arcgis.com", passwords.user_name, passwords.password)

query = 'title: "Parks*" AND type: "Feature Service"'
search_results = gis.content.search(query=query, max_items=10)
display(search_results)

csv_data = search_results[0]
display(csv_data)


# In[2]:


feature_layers = csv_data.layers
trailheads_layer = feature_layers[0]
trailheads_layer.properties.name

for field in trailheads_layer.properties['fields']:
    print ('Name: {:16s}\tType: {}'.format(field['name'], field['actualType']))


# In[3]:


#Escriba una función de devolución de llamada para el método on_click del widget de mapa
from arcgis import geometry
from arcgis import features

def create_feature(_map, location):
    try:
        object_id = 1
        point = geometry.Point(location)
        feature = features.Feature(
            geometry = point,
            attributes = {
                'OBJECTID': object_id,
                'PARK_NAME': 'My Park',
                'TRL_NAME': 'Foobar Trail',
                'ELEV_FT': '5000'
            }
        )
        
        trailheads_layer.edit_features(adds = [feature])
        _map.draw(point)
        
    except Exception as e:
        print ("No pudo crear el feature. {}".format(str(e)))


# In[4]:


m = gis.map()

#esperar que el mapa cargue para luego personalizar
m.center = [34.09042, -118.71511] #`[latitud, longitud]`
m.zoom = 11
m.on_click(create_feature)

m.clear_graphics()

m.add_layer(trailheads_layer)

m


# In[ ]:




