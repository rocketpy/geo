#  any location on earth without an API-Key  !!!

#  https://pypi.org/project/geovision/

#  pip install geovision

"""
Dependencies :
  Python 3.7+
  Selenium
  Beautiful Soup
  Chrome Driver
"""

#  some examples (taked from https://pypi.org/project/geovision/)

from geovision import geocode

geo = geocode('Signal Iduna Park')


geo.locality # = Dortmund, Germany
geo.country # = Germany
geo.area_code # = 9F39
geo.local_code # = FFV2+2P
geo.plus_code # = 9F39FFV2+2P
geo.address # = Strobelallee 50, 44139 Dortmund, Germany
geo.coordinates # = (51.492562, 7.451812)
geo.latitude # = 51.492562
geo.longitude # = 7.451812

#  objects
from geovision import Geocoder

geo = Geocoder()
geo.geocode('Signal Iduna Park')
geo.to_dict()
"""
{'Signal Iduna Park': {'locality': 'Dortmund, Germany', 'country': 'Germany', 'area_code': '9F39', 'local_code': 'FFV2+2P', 'plus_code': '9F39FFV2+2P', 'address': 'Strobelallee 50, 44139 Dortmund, Germany', 'coordinates': (51.492562, 7.451812), 'latitude': 51.492562, 'longitude': 7.451812}}
"""
