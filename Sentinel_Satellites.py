# A Python library that allows to extract data from sentinel satellites, exploiting multi-threading and relying on Google Earth Engine APIs.

# https://github.com/Amatofrancesco99/master-thesis/tree/main/Notebooks
# https://pypi.org/project/sentinel-satellites/

# pip install sentinel-satellites


# First you have to initialize and authorize the Google Earth Engine APIs.
import ee, sentinel_satellites


ee.Authenticate()
ee.Initialize()
