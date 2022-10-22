# fake-geo-images - Fake geospatial images for unit tests

# https://pypi.org/project/fake-geo-images/
# https://github.com/up42/fake-geo-images

# pip install fake-geo-images


import numpy as np
import rasterio as rio
from pathlib import Path
from my_image_processing import ndvi
from fake_geo_images.fakegeoimages import FakeGeoImage


def test_ndvi():
    """
    A unit test if an NDVI method works in general
    """
    # Create 4-band image simulating RGBN as needed for NDVI
    test_image, _ = FakeGeoImage(
            300, 150, 4, "uint16", out_dir=Path("/tmp"), crs=4326, nodata=0, nodata_fill=3, cog = False
        ).create(seed=42)

    ndvi_image = ndvi(test_image)

    with rio.open(str(ndvi_image)) as src:
        ndvi_array = src.read()
        # NDVI only has one band of same size as input bands
        assert ndvi_array.shape == (1, 300, 150)
        # NDVI has float values between -1 and 1
        assert ndvi_array.dtype == np.float
        assert ndvi_array.min >= -1
        assert ndvi_array.max <= 1

