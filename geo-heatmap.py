#  geo-heatmap - Generate an interactive geo-heatmap from your Google location data.

# PYPI: https://pypi.org/project/geo-heatmap/
# Github: https://github.com/jamesjarvis/geo-heatmap

# pip install geo-heatmap

"""
# Get Your Location Data

Here you can find out how to download your Google data: https://support.google.com/accounts/answer/3024190?hl=en
Here you can download all of the data that Google has stored on you: https://takeout.google.com/

To use this script, you only need to select and download your "Location History", which Google will provide to you as a JSON file by default. KML is also an output option and is accepted for this program.

# Install the script
In a command prompt or Terminal window, navigate to the directory containing the location data files. Then, type the following, and press enter:

pip install geo-heatmap
# Run the Script
In the same command prompt or Terminal window, type the following, and press enter:

geo-heatmap <file> [<file> ...]
Replace the string <file> from above with the path to any of the following files:

The Location History.json JSON file from Google Takeout
The Location History.kml KML file from Google Takeout
The takeout-*.zip raw download from Google Takeout that contains either of the above files
Examples:
Single file:

geo-heatmap C:\Users\Testuser\Desktop\locations.json
geo-heatmap "C:\Users\Testuser\Desktop\Location History.json"
geo-heatmap locations.json
Multiple files:

geo-heatmap locations.json locations.kml takeout.zip
Using the stream option (for users with Memory Errors):

geo-heatmap -s locations.json
Set a date range:

geo-heatmap --min-date 2017-01-02 --max-date 2018-12-30 locations.json
Usage:
usage: geo-heatmap [-h] [-o] [--min-date YYYY-MM-DD]
                      [--max-date YYYY-MM-DD] [-s] [--map MAP]
                      file [file ...]

positional arguments:
  file                  Any of the following files:
                        1. Your location history JSON file from Google Takeout
                        2. Your location history KML file from Google Takeout
                        3. The takeout-*.zip raw download from Google Takeout
                        that contains either of the above files

optional arguments:
  -h, --help            show this help message and exit
  -o , --output         Path of heatmap HTML output file.
  --min-date YYYY-MM-DD
                        The earliest date from which you want to see data in the heatmap.
  --max-date YYYY-MM-DD
                        The latest date from which you want to see data in the heatmap.
  -s, --stream          Option to iteratively load data.
  --map MAP, -m MAP     The name of the map tiles you want to use.
                        (e.g. 'OpenStreetMap', 'StamenTerrain', 'StamenToner', 'StamenWatercolor')

"""
