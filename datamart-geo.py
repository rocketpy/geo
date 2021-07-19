#   datamart-geo - Geographical location data
#  This package contains geospatial data and associated facilities to resolve administrative areas.

# PyPi: https://pypi.org/project/datamart-geo/
# Home page : https://gitlab.com/ViDA-NYU/auctus/datamart-geo

# pip install datamart-geo

# To use the fuzzy-search capabilities (GeoData.resolve_name_fuzzy()), you will need to install datamart-geo[fuzzy].

# Example usage:
geo_data = datamart_geo.GeoData.download()  # Download data if needed
france = geo_data.resolve_name('France')
# france
# <datamart_geo.Area "Republic of France" (3017382) type=Type.ADMIN_0>
france.latitude, france.longitude
# (46.0, 2.0)
# france.bounds
# (-61.797841, 55.854503, -21.370782, 51.087541)
assert france.type == datamart_geo.Type.ADMIN_0
assert france.type == datamart_geo.Type.COUNTRY

cuers = geo_data.resolve_name('Cuers')
cuers
# <datamart_geo.Area "Cuers" (6451482) type=Type.ADMIN_4>
# cuers.latitude, cuers.longitude
# (43.2375, 6.07083)
# cuers.get_parent_area()
# <datamart_geo.Area "Arrondissement de Toulon" (2972326) type=Type.ADMIN_3>
