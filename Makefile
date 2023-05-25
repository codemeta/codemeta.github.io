all: data/crosswalk.json

# Download the latest crosswalk
data/crosswalk.csv:
	wget https://github.com/codemeta/codemeta/raw/master/crosswalk.csv -O data/crosswalk.csv

# Convert crosswalk.csv to crosswalk.json so Hugo can parse it
data/crosswalk.json: data/crosswalk.csv
	python3 scripts/crosswalk_to_json.py
