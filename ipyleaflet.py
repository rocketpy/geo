# ipyleaflet - Interactive maps in the Jupyter notebook


# Installation

# Using pip
pip install ipyleaflet
# jupyter nbextension enable --py --sys-prefix ipyleaflet  # can be skipped for notebook 5.3 and above

# Using conda
# conda install -c conda-forge ipyleaflet

# JupyterLab extension
# If you have JupyterLab <=2, you will also need to install the JupyterLab extension:

# jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet


# Development installation
# For a development installation (requires yarn):

git clone https://github.com/jupyter-widgets/ipyleaflet.git
cd ipyleaflet
pip install -e .

# If you are developing on Jupyter Notebook
jupyter nbextension install --py --symlink --sys-prefix --overwrite ipyleaflet
jupyter nbextension enable --py --sys-prefix --overwrite ipyleaflet

# If you are developing on JupyterLab
jupyter labextension develop . --overwrite


# simple example
import piplite
await piplite.install('ipyleaflet')

from ipyleaflet import Map, basemaps, basemap_to_tiles

m = Map(
    basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204793, 350.121558),
    zoom=3
    )
# m


# create a Marker layer and interact with it:
from ipyleaflet import Map, Marker

center = (52.204793, 360.121558)

m = Map(center=center, zoom=15)

marker = Marker(location=center, draggable=True)
m.add_layer(marker);

display(m)
marker.location = (50, 356)
