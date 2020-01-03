#  Python Toolbox for Geographic Visualizations !!!

#  pip install geoplotlib

# User  Guide  - https://github.com/andrea-cuttone/geoplotlib/wiki/User-Guide

# simple example
import geoplotlib

data = geoplotlib.utils.read_csv('file_name.csv')
geoplotlib.dot(data)
geoplotlib.show()
