#  High-level geospatial plotting for Python.

# Github: https://github.com/ResidentMario/geoplot
# Docs: https://residentmario.github.io/geoplot/installation.html

#  Important !!!  Requires: Python >=3.6.0
#  pip install geoplot

%matplotlib inline

import pandas as pd; pd.set_option('max_columns', 6)
import geopandas as gpd
import geoplot as gplt


usa_cities = gpd.read_file(gplt.datasets.get_path('usa_cities'))
usa_cities.head() 

# more examples: https://residentmario.github.io/geoplot/quickstart/quickstart.html 
