#  Cartopy is a cartographic python library with Matplotlib support for visualisation !
#  Docs :  https://scitools.org.uk/cartopy/docs/latest/

#  pip install Cartopy

#  Cartopy projection list : https://scitools.org.uk/cartopy/docs/latest/crs/projections.html

"""
Mercator like example

class cartopy.crs.Mercator(central_longitude=0.0, min_latitude=-80.0, max_latitude=84.0, globe=None, latitude_true_scale=None,
false_easting=0.0, false_northing=0.0, scale_factor=None)[source]


# Parameters
central_longitude (optional) – The central longitude. Defaults to 0.

min_latitude (optional) – The maximum southerly extent of the projection. Defaults to -80 degrees.

max_latitude (optional) – The maximum northerly extent of the projection. Defaults to 84 degrees.

globe (A cartopy.crs.Globe, optional) – If omitted, a default globe is created.

latitude_true_scale (optional) – The latitude where the scale is 1. Defaults to 0 degrees.

false_easting (optional) – X offset from the planar origin in metres. Defaults to 0.

false_northing (optional) – Y offset from the planar origin in metres. Defaults to 0.

scale_factor (optional) – Scale factor at natural origin. Defaults to unused.

Notes

Only one of latitude_true_scale and scale_factor should be included.
"""
