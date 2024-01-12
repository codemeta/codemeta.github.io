all: data/crosswalk.json data/properties_description.json

# Download the latest crosswalk
data/crosswalk.csv:
	wget https://github.com/codemeta/codemeta/raw/master/crosswalk.csv -O data/crosswalk.csv

# Convert crosswalk.csv to crosswalk.json so Hugo can parse it
data/crosswalk.json: scripts/crosswalk_to_json.py data/crosswalk.csv
	python3 scripts/crosswalk_to_json.py

# properties_description.csv file was only split off from crosswalks.csv starting with
# v2.1, so we can't download v2.0 itself. There were no major changes between the two,
# anyway.
data/properties_description/v2.0.csv:
	wget https://github.com/codemeta/codemeta/raw/2.1/properties_description.csv -O $@

# Download properties descriptions for other versions
data/properties_description/v%.csv:
	wget https://github.com/codemeta/codemeta/raw/$*/properties_description.csv -O $@

data/properties_description.json: scripts/properties_to_json.py data/properties_description/v2.0.csv data/properties_description/v3.0.csv
	python3 scripts/properties_to_json.py
