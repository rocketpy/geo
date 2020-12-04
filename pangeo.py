#  PANGEO - A community platform for Big Data geoscience

#  Official website: http://pangeo.io/
#  GitHub: https://github.com/pangeo-data

#  Pangeo Gallery: http://gallery.pangeo.io/
#  Pangeo Notebooks:  https://github.com/pangeo-data/pangeo-example-notebooks


#  Example, scikit-image-example.ipynb
from dask_gateway import Gateway

gateway = Gateway()
cluster = gateway.new_cluster()
cluster.scale(10)
# cluster


from dask.distributed import Client, progress

client = Client(cluster)


%matplotlib inline
from dask import delayed
import skimage.io
import matplotlib.pyplot as plt


# Read a single image from Google Cloud Storage
sample = skimage.io.imread('https://storage.googleapis.com/pangeo-data/FIB-25/iso.00000.png')

fig = plt.figure(figsize=(10, 10))
plt.imshow(sample, cmap='gray')


#  Construct a Lazy Dask Array from all of the images
from dask import delayed
import dask.array as da

# filenames = ['https://storage.googleapis.com/pangeo-data/FIB-25/iso.%05d.png' % i for i in range(0, 8090)]
filenames = ['https://storage.googleapis.com/pangeo-data/FIB-25/iso.%05d.png' % i for i in range(0, 1000)]
images = [delayed(skimage.io.imread)(fn) for fn in filenames]
arrays = [da.from_delayed(im, shape=sample.shape, dtype=sample.dtype) for im in images]
x = da.stack(arrays, axis=0)
# x
