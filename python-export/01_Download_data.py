#!/usr/bin/env python
# coding: utf-8

# # https://developers.arcgis.com/labs/python/download-data/
# # Download data by python

# In[23]:


#imports
from arcgis.gis import GIS

#Python Standard Library Modules
from pathlib import Path
from zipfile import ZipFile

#El código original da el error FileNotFoundError: [Errno 2] No such file or directory: 'data\\LA_Hub_Datasets.zip'
import os

#ID pública de datos en ESRI
public_data_item_id = 'a04933c045714492bda6886f355416f2'

#Usar conexión anónima
anon_gis = GIS()

#Usar el get() para hacer una solicitud de ArcGIS REST API sobre el contenido (ContentManager)
data_item = anon_gis.content.get(public_data_item_id)

#ContentManaget.get regresa None, si el Id adjunto no es un Id valido
data_item

#Descarga de datos
data_path = Path('./data')

if not data_path.exists():
    data_path.mkdir()

#El nombre original del archivo según la guía es "LA_Hub_Datasets.zip"; sin embargo, el nombre es "LAHubDatasets.zip"
zip_path = data_path.joinpath('LAHubDatasets.zip')
extract_path = data_path.joinpath('LA_Hub_datasets')

data_item.download(save_path = data_path)

#Extracción de datos
#C:\Users\USER_NAME\ArcGIS\python
filepath = os.path.join('C:\\', 'Users', 'USER_NAME', 'ArcGIS', 'python', 'data', 'LAHubDatasets.zip')

zip_file = ZipFile(filepath)
zip_file.extractall(path = extract_path)

#Listar el contenido de lo extraído
# Original:
#list(file.name for file in extract_path.glob('*'))

#Extra
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            
list_files(extract_path)


# In[ ]:




