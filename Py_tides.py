# Pytides - Pytides is small Python package for the analysis and prediction of tides.

# https://github.com/sam-cox/pytides/

# Installation
"""
easy_install pytides
or
pip install pytides
should do the trick.
Mainly for my own reference (sanity), to get pytides and its dependencies all working in a Debian (mint) virtualenv:

sudo apt-get install liblapack-dev libatlas-base-dev gfortran
export LAPACK=/usr/lib/liblapack.so
export ATLAS=/usr/lib/libatlas.so
export BLAS=/usr/lib/libblas.so
pip install numpy
pip install scipy
pip install pytides
"""

# Example Pytides Usage
from datetime import datetime
from pytides.tide import Tide
import numpy as np
import matplotlib.pyplot as plt


##Prepare our tide data
station_id = '8516945'

heights = []
t = []

f = open('data/'+station_id, 'r')
for i, line in enumerate(f):
    t.append(datetime.strptime(" ".join(line.split()[:2]), "%Y-%m-%d %H:%M"))
    heights.append(float(line.split()[2]))
f.close()
