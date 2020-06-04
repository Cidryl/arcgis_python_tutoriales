# esri-python-training
ArcGIS API for Python

Tutoriales basados en:
https://developers.arcgis.com/labs/browse/?product=python&topic=any

## 🚀 Comenzando

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

* Clona o descarga el contenido
* Descomprimir y ubicar el contenido en un sitio donde pueda editar los archivos libremente (en mi caso, wwwroot de un IIS local con permisos sobre la carpeta)
* Anaconda para la edición de los proyectos *ipynb
* Editar el archivo passwords.py

### 📋 Pre-requisitos

* Tener instalado Anaconda
* Instalar el paquete arcgis Python API

### 🔧 Instalación

_Siguiente pasos para ejecutar el proyecto en un sitio_

Pasos para Instalación de jupyter notebook y API Python de ArcGIS:

1. Instalar Anaconda  : https://www.anaconda.com/distribution/
2. Descargar archivo  : https://anaconda.org/Esri/arcgis/files
3. con Anaconda Prompt: (Administrador)

```
conda config --set offline True
conda activate base
conda install /path_to_package_download_folder/platform/arcgis-x.x.x-pyZZyyyyyyy-y.tar.bz2
```
Refrescar la ventana de navegador de anaconda y verificar que el paquete "arcgis" esté instalado (en ambiente - Environments)
La instalación de anaconda ya cuenta con jupyter notebook instalado, pero no el API Python de ArcGIS

## 📦 Deployment 

Se puede ejecutar jupyter notebook la opción de "run cell", o bien al presionar "shift" + "Enter" para ejecutar todas las celdas

## 🛠️ Construido con 

_base inicial (en mi caso, los tutoriales dan error en ciertos puntos, por lo que tuve que realizar cambios):_

https://developers.arcgis.com/labs/browse/?product=python&topic=any

## 📌 Versionado

No cuenta con versionamiento, conforme se ejecutan los tutoriales, se iran guardando el proyecto y el archivo py


## 📄 Licencia

Este proyecto está bajo MIT License - mira el archivo [LICENSE.md](LICENSE) para detalles
