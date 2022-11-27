# ipyleaflet - Interactive maps in the Jupyter notebook


# simple example
import piplite
await piplite.install('ipyleaflet')

from ipyleaflet import Map, basemaps, basemap_to_tiles

m = Map(
    basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204793, 350.121558),
    zoom=3
    )
# m

