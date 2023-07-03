# A Python library that allows to extract data from sentinel satellites, exploiting multi-threading and relying on Google Earth Engine APIs.

# https://github.com/Amatofrancesco99/master-thesis/tree/main/Notebooks
# https://pypi.org/project/sentinel-satellites/

# pip install sentinel-satellites


# First you have to initialize and authorize the Google Earth Engine APIs.
import ee, sentinel_satellites


ee.Authenticate()
ee.Initialize()

# Then, supposing that you have already loaded the fields_df pandas DataFrame,
# you have just to run the following code.
df = sentinel_satellites.get_features(fields_df, "2022-01-01", "2022-12-31", sentinel=2, filters_params=['40'], fields_threads=3)

# Choose the file (it must be a JSON file)
file_chooser = ipyfilechooser.FileChooser(
    path='../../Datasets/main/', filename='main-fields.json',
    select_default=True, use_dir_icons=True, filter_pattern='*.json'
)
display(file_chooser)

# Load JSON data from file
with open(file_chooser.selected) as f:
    data = json.load(f)

# Create DataFrame with properties excluding 'manure_dates' column
fields_df = pd.DataFrame([{k:v for k,v in f['properties'].items() if k!='manure_dates'} for f in data['features']])

