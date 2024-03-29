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


import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)

# uncomment if including figures:
# import matplotlib.pyplot as plt
# from astropy.visualization import astropy_mpl_style
# plt.style.use(astropy_mpl_style)


# Constants

from astropy.constants import G

print(G)
"""
Name   = Gravitational constant
Value  = 6.6743e-11
Uncertainty  = 1.5e-15
Unit  = m3 / (kg s2)
Reference = CODATA 2018
"""
# or
from astropy import constants as const

print(const.G)
# Name   = Gravitational constant
