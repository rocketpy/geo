# Astropy - package for Astronomy in Python and foster interoperability between Python astronomy packages.

# https://github.com/astropy/astropy
# http://astropy.org/
# https://pypi.org/project/astropy/
# https://docs.astropy.org/en/stable/


import astropy
from astropy import subpackage
from astropy.io import fits

hdulist = fits.open('data.fits')


from astropy import units as u
from astropy import coordinates as coord
coord.SkyCoord(ra=10.68458*u.deg, dec=41.26917*u.deg, frame='icrs')
