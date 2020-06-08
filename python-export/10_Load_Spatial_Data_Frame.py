#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/load-spatial-data-frame/
# # Load Spatial Data Frame

# In[1]:


from arcgis.gis import GIS
from arcgis.features import SpatialDataFrame
from IPython.display import display
import passwords

gis = GIS("https://www.arcgis.com", passwords.user_name, passwords.password)

search_results = gis.content.search(query='title: "Park*" AND type: "Feature Service"')
display(search_results)


# In[2]:


feature_service_item = search_results[0]
feature_layer = feature_service_item.layers[0]
display(feature_layer)


# In[3]:


# Search for an item and construct a Spatial Data Frame


# In[4]:


sdf = SpatialDataFrame.from_layer(feature_layer)
sdf.head()


# In[ ]:


# sdf.to_featureclass(out_location = 'path/to/save/data', out_name = 'file.shp')

