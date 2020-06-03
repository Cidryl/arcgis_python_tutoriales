#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/import-data/
# # Import Data

# In[31]:


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

parks_properties = {
    'title': 'Parks and Open Space',
    'tags': 'parks, open data, tutorials',
    'type': 'Shapefile'
}

#Original
#data_file_location = 'data/LA_Hub_datasets/LA_Hub_Datasets/Parks_and_Open_Space.zip'
#USER_NAME
data_file_location = os.path.join('C:\\', 'Users', 'jchaconsa', 'ArcGIS', 'python', 'data', 'LA_Hub_datasets', 'LA_Hub_Datasets', 'Parks_and_Open_Space.zip')

search_result = gis.content.search('title:Parks and Open Space')

if not search_result:
    parks_shp = gis.content.add(parks_properties, data = data_file_location)
    parks_feature_layer_item = parks_shp.publish()
    parks_feature_layer_item.url
else:
    for item in search_result:
        display(item)


# In[ ]:




