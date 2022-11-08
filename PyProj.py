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


# Converting CRS to a different format
from pyproj import CRS


crs = CRS.from_epsg(4326)
print(crs.to_epsg())
# 4326

print(crs.to_authority())
# ('EPSG', '4326')

crs = CRS.from_proj4("+proj=omerc +lat_0=-36 +lonc=147 +alpha=-54 +k=1 +x_0=0 +y_0=0 +gamma=0 +ellps=WGS84 +towgs84=0,0,0,0,0,0,0")
print(crs)
print(crs.to_wkt(pretty=True))

from pyproj.enums import WktVersion
print(crs.to_wkt(WktVersion.WKT1_GDAL, pretty=True))

from pprint import pprint
pprint(crs.to_cf())

# Extracting attributes from CRS
crs = CRS("urn:ogc:def:crs,crs:EPSG::2393,crs:EPSG::5717")
print(crs)

print(crs.sub_crs_list)

cop = crs.sub_crs_list[0].coordinate_operation
print(cop.to_wkt(pretty=True))

print(cop.method_code)
# '9807'
print(cop.method_name)
# 'Transverse Mercator'
print(cop.params)


# Find UTM CRS by Latitude and Longitude
from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info

utm_crs_list = query_utm_crs_info(
    datum_name="WGS 84",
    area_of_interest=AreaOfInterest(
        west_lon_degree=-93.581543,
        south_lat_degree=42.032974,
        east_lon_degree=-93.581543,
        north_lat_degree=42.032974,
    ),
)
utm_crs = CRS.from_epsg(utm_crs_list[0].code)


# Transformations from CRS to CRS
from pyproj import CRS

crs_4326 = CRS.from_epsg(4326)
print(crs_4326)

crs_26917 = CRS.from_epsg(26917)
print(crs_26917)


# Create Transformer to convert from CRS to CRS
from pyproj import Transformer

transformer = Transformer.from_crs(crs_4326, crs_26917)
transformer = Transformer.from_crs(4326, 26917)
transformer = Transformer.from_crs("EPSG:4326", "EPSG:26917")

print(transformer.transform(50, -80))


from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:4326", "EPSG:26917", always_xy=True)
transformer.transform(-80, 50)

# Converting between geographic and projection coordinates within one datum
from pyproj import CRS

crs = CRS.from_epsg(3857)
print(crs)
print(crs.geodetic_crs)


# Create Transformer to convert from geodetic CRS to CRS
proj = Transformer.from_crs(crs.geodetic_crs, crs)

print(proj)
print(proj.transform(12, 15))


# 4D Transformations with Time
transformer = Transformer.from_crs(7789, 8401)

transformer.transform(xx=3496737.2679, yy=743254.4507, zz=5264462.9620, tt=2019.0)


# Geodesic calculations

# Creating Geod class
from pyproj import CRS, Geod

geod_clrk = Geod(ellps='clrk66')
geod_wgs84 = CRS("epsg:4326").get_geod()
