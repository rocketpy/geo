# pysatNASA: pysat support for NASA Space Science instruments

# https://github.com/pysat/pysatNASA
# git clone https://github.com/pysat/pysatNASA.git

# Change directories into the repository folder and run the setup.py file.
# For a local install use the "--user" flag after "install".
# cd pysatNASA/
# python setup.py install


# Using with pysat
import pysat
from pysatNASA.instruments import icon_ivm

ivm = pysat.Instrument(inst_module=icon_ivm, inst_id='a')
