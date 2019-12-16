#  http://geopandas.org/data_structures.html  - Data structures in geopandas and basic actions !

#  installation :  http://geopandas.org/install.html
#  pip install geopandas

# VERY important , check all dependencies !!!  http://geopandas.org/install.html#dependencies

# simple example , taked from official website

import geopandas

# adding a  background map to plots
df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

# more info here :  http://geopandas.org/gallery/plotting_basemap_background.html#sphx-glr-gallery-plotting-basemap-background-py
