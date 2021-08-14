# GeoViews - GeoViews is a Python library that makes it easy to explore and visualize geographical, meteorological, and
#            oceanographic datasets, such as those used in weather, climate, and remote sensing research.

# PyPi: https://pypi.org/project/geoviews/
# HomePage: https://geoviews.org/

# pip install geoviews

# Simple Example
import xarray as xr
import geoviews as gv
import geoviews.feature as gf
from cartopy import crs


# gv.extension('bokeh', 'matplotlib')

dataset = gv.Dataset(xr.open_dataset('./data/ensemble.nc'))
ensemble = dataset.to(gv.Image, ['longitude', 'latitude'], 'surface_temperature')

# gv.output(ensemble.opts(cmap='viridis', colorbar=True, fig_size=200, backend='matplotlib') * gf.coastline(), backend='matplotlib')

import geopandas as gpd

# gv.Polygons(gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')),vdims=['pop_est',
# ('name', 'Country')]).opts(tools=['hover'], width=600, projection=crs.Robinson())
