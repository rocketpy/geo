# Python interface to PROJ (cartographic projections and coordinate transformations library).

# GitHub: https://github.com/pyproj4/pyproj

# pip install pyproj
# Install pyproj: https://pyproj4.github.io/pyproj/stable/installation.html#install-pyproj


# Using CRS
from pyproj import CRS

crs = CRS.from_epsg(4326)
crs = CRS.from_string("epsg:4326")
crs = CRS.from_proj4("+proj=latlon")
crs = CRS.from_user_input(4326)
