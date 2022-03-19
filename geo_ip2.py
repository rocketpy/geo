# GeoIP2 API
# This package provides an API for the GeoIP2 and GeoLite2 web services and databases.

# https://pypi.org/project/geoip2/

# pip install geoip2


import geoip2.webservice

# This creates a Client object that can be reused across requests.
# Replace "42" with your account ID and "license_key" with your license
# key. Set the "host" keyword argument to "geolite.info" to use the
# GeoLite2 web service instead of GeoIP2 Precision.
with geoip2.webservice.Client(42, 'license_key') as client:
    # Replace "city" with the method corresponding to the web service
    # that you are using, i.e., "country", "city", or "insights". Please
    # note that Insights is not supported by the GeoLite2 web service.
    response = client.city('203.0.113.0')

# response.country.iso_code
# response.country.name
# response.country.names['zh-CN']

# response.subdivisions.most_specific.name
# response.subdivisions.most_specific.iso_code

# response.city.name
# response.postal.code
# response.location.latitude
# response.location.longitude
# response.traits.network

# IPv4Network('203.0.113.0/32')

