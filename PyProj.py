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


# Geodesic line length
from pyproj import Geod

lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
        -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]

lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
        88, 59, 25, -4, -14, -33, -46, -61]

geod = Geod(ellps="WGS84")
total_length = geod.line_length(lons, lats)
print(f"{total_length:.3f}")


# Calculate the geodesic length of a shapely geometry
from pyproj import Geod
from shapely.geometry import Point, LineString

line_string = LineString([Point(1, 2), Point(3, 4)]))
geod = Geod(ellps="WGS84")
total_length = geod.geometry_length(line_string)
print(f"{total_length:.3f}")


# Geodesic area
from pyproj import Geod

geod = Geod('+a=6378137 +f=0.0033528106647475126')
lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
        -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]

lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
        88, 59, 25, -4, -14, -33, -46, -61]

poly_area, poly_perimeter = geod.polygon_area_perimeter(lons, lats)
print(f"{poly_area:.3f} {poly_perimeter:.3f}")


# Calculate the geodesic area and perimeter of a shapely polygon
from pyproj import Geod
from shapely.geometry import LineString, Point, Polygon

geod = Geod('+a=6378137 +f=0.0033528106647475126')

poly_area, poly_perimeter = geod.geometry_area_perimeter(
        Polygon(
            LineString([Point(1, 1), Point(1, 10), Point(10, 10), Point(10, 1)]),
            holes=[LineString([Point(1, 2), Point(3, 4), Point(5, 2)])],
        )
    )

print(f"{poly_area:.3f} {poly_perimeter:.3f}")


# Advanced Examples

# Optimize Transformations
import numpy as np
from pyproj import Transformer, transform

transformer = Transformer.from_crs(2263, 4326)
x_coords = np.random.randint(80000, 120000)
y_coords = np.random.randint(200000, 250000)

transform(2263, 4326, x_coords, y_coords)
transformer.transform(x_coords, y_coords)


# Transformation Group

from pyproj.transformer import TransformerGroup

trans_group = TransformerGroup("epsg:4326","epsg:2964")
print(trans_group)

trans_group.transformers[0].transform(66, -153)
(149661.2825058747, 5849322.174897663)

trans_group.transformers[1].transform(66, -153)
(149672.928811047, 5849311.372139239)

trans_group.transformers[2].transform(66, -153)


from pyproj.transformer import TransformerGroup

tg = TransformerGroup("epsg:4326", "+proj=aea +lat_0=50 +lon_0=-154 +lat_1=55 +lat_2=65 +x_0=0 +y_0=0 +datum=NAD27 +no_defs +type=crs +units=m", 
                      always_xy=True)
# tg.transformers[0].description
# tg.unavailable_operations[0].name
# tg.unavailable_operations[0].grids[0].url


# Area of Interest
from pyproj.transformer import Transformer, AreaOfInterest

transformer = Transformer.from_crs("epsg:4326", "epsg:2694")
print(transformer)

transformer = Transformer.from_crs(
    "epsg:4326",
    "epsg:2694",
    area_of_interest=AreaOfInterest(-136.46, 49.0, -60.72, 83.17),
)

# Promote CRS to 3D
from pyproj import CRS, Transformer

transformer = Transformer.from_crs("EPSG:4326", "EPSG:2056", always_xy=True)
transformer.transform(8.37909, 47.01987, 1000)

transformer_3d = Transformer.from_crs(
    CRS("EPSG:4326").to_3d(),
    CRS("EPSG:2056").to_3d(),
    always_xy=True,
...)

print(transformer_3d.transform(8.37909, 47.01987, 1000))


# Projected CRS Bounds
from pyproj import CRS, Transformer

crs = CRS("EPSG:3857")
transformer = Transformer.from_crs(crs.geodetic_crs, crs, always_xy=True)
transformer.transform_bounds(*crs.area_of_use.bounds)


# Multithreading
import concurrent.futures

from pyproj import Transformer


def transform_point(point):
    transformer = Transformer.from_crs(4326, 3857)
    return transformer.transform(point, point * 2)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for result in executor.map(transform_point, range(5)):
        print(result)


# Optimizing Single-Threaded Applications
import pyproj

codes = pyproj.get_codes("EPSG", pyproj.enums.PJType.PROJECTED_CRS, False)
crs_list = [pyproj.CRS.from_epsg(code) for code in codes]


# Caching pyproj objects
# Transformer

from functools import lru_cache
from pyproj import Transformer

TransformerFromCRS = lru_cache(Transformer.from_crs)

# Transformer.from_crs(2263, 4326)  # no cache
# TransformerFromCRS(2263, 4326)

from timeit import timeit

timeit(
    "CachedTransformer(2263, 4326)",
    setup=(
        "from pyproj import Transformer; "
        "from functools import lru_cache; "
        "CachedTransformer = lru_cache(Transformer.from_crs)"
    ),
    number=1000000,
)

timeit(
    "Transformer.from_crs(2263, 4326)",
    setup=("from pyproj import Transformer"),
    number=100,
)

# CRS Example
from functools import lru_cache
from pyproj import CRS

CachedCRS = lru_cache(CRS)

crs = CRS(4326)  # no cache
crs = CachedCRS(4326)  # cache

from timeit import timeit

timeit(
    "CachedCRS(4326)",
    setup=(
        "from pyproj import CRS; "
        "from functools import lru_cache; "
        "CachedCRS = lru_cache(CRS)"
    ),
    number=1000000,
)

timeit(
    "CRS(4326)",
    setup=("from pyproj import CRS"),
    number=1000,
)


# Debugging Internal PROJ
import logging

console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s:%(message)s")
console_handler.setFormatter(formatter)
logger = logging.getLogger("pyproj")
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


# Activate default logging config:
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
