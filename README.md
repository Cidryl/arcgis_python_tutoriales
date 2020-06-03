# esri-python-training
ArcGIS API for Python

Tutoriales basados en:
https://developers.arcgis.com/labs/browse/?product=python&topic=any

Pasos para Instalación de jupyter notebook y API Python de ArcGIS:

1. Instalar Anaconda (ver pdf) : https://www.anaconda.com/distribution/
2. Descargar archivo  : https://anaconda.org/Esri/arcgis/files
3. con Anaconda Prompt: (Administrador)

```
conda config --set offline True
conda activate base
conda install /path_to_package_download_folder/platform/arcgis-x.x.x-pyZZyyyyyyy-y.tar.bz2
```
La instalación ya cuenta con jupyter notebook instalado, pero no el API Python de ArcGIS
