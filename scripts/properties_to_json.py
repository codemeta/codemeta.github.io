"""Transforms a set of ``properties_Description.csv`` files from the main Codemeta repo
into JSON processable by Hugo.

For example, this turns this :file:`v3.0.csv`:

.. code-block: csv

    Parent Type,Property,Type,Description
    schema:CreativeWork,author,Organization or Person,The author of this content
    codemeta:SoftwareSourceCode,readme,URL,link to software Readme file
    codemeta:SoftwareSourceCode,embargoEndDate,Date,"Software may be embargoed from public access until a specified date

and this :file:`v2.0.csv`:

.. code-block: csv

    Parent Type,Property,Type,Description
    schema:CreativeWork,author,Organization or Person,The author of this content
    codemeta:SoftwareSourceCode,readme,URL,link to software Readme file
    codemeta:SoftwareSourceCode,embargoDate,Date,"Software may be embargoed from public access until a specified date

into:

.. code-block: json

    [
        {
            "versions": ["v3.0", "v2.0"],
            "Parent Type": "schema:CreativeWork",
            "Property": "author",
            "Type": "Organization or Person",
            "Description": "The author of this content"
        },
        {
            "versions": ["v3.0", "v2.0"],
            "Parent Type": "schema:SoftwareSourceCode",
            "Property": "readme",
            "Type": "URL",
            "Description": "The author of this content"
        },
        {
            "versions": ["v3.0"],
            "Parent Type": "schema:SoftwareSourceCode",
            "Property": "embargoEndDate",
            "Type": "Date",
            "Description": "Software may be embargoed from public access until a specified date"
        },
        {
            "versions": ["v2.0"],
            "Parent Type": "schema:SoftwareSourceCode",
            "Property": "embargoDate",
            "Type": "Date",
            "Description": "Software may be embargoed from public access until a specified date"
        }
    ]
"""

import csv
import json
import pathlib

DIR = pathlib.Path(__file__).parent.parent
CSV_PATH = DIR / "data/properties_description/"
JSON_PATH = DIR / "data/properties_description.json"

json_items = []

# List .csv files in reverse version order, so Description from the latest version
# takes precedence.
paths = sorted(
    CSV_PATH.glob("*.csv"), key=lambda p: float(p.stem.lstrip("v")), reverse=True
)

for csv_path in paths:
    version = csv_path.stem
    # header = ["Parent Type", "Property", "Type", "Description"]
    (header, *rows) = list(csv.reader(csv_path.open()))

    for row in rows:
        item = dict(zip(header, row))

        if item["Property"] == "":
            continue  # skip empty rows

        # Look for a similar existing item from a newer Codemeta version
        for existing_item in json_items:
            if existing_item.items() >= item.items():
                # We found an existing item, add this version to its list
                assert (
                    version not in existing_item["versions"]
                ), f"Codemeta {version} has duplicated property {item}"
                existing_item["versions"].append(version)
                break
        else:
            # No similar item, create a new one
            item["versions"] = [version]
            json_items.append(item)

# Sort properties by their name
json_items.sort(key=lambda item: item["Property"])

JSON_PATH.write_text(json.dumps(json_items, indent="  "))
