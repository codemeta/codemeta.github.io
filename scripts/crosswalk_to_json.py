"""Transforms a CSV into JSON processable by Hugo

For example, this turns this:

.. code-block: csv

    titleA,titleB,titleC
    row1A,row1B,row1C
    row2A,row2B,row2C

into:

.. code-block: json

    [
        {
            "titleA": "row1A",
            "titleB": "row1B",
            "titleC": "row1C"
        },
        {
            "titleA": "row2A",
            "titleB": "row2B",
            "titleC": "row2C"
        }
    ]
"""

import csv
import json
import pathlib

DIR = pathlib.Path(__file__).parent.parent
CSV_PATH = DIR / "data/crosswalk.csv"
JSON_PATH = DIR / "data/crosswalk.json"

# header = ["titleA", "titleB", "titleC"]
# rows = [["row1A", "row1B", "row1C"], ["row2A", "row2B", "row2C"]]
(header, *rows) = list(csv.reader(CSV_PATH.open()))

json_items = []

for row in rows:
    json_items.append(dict(zip(header, row)))

JSON_PATH.write_text(json.dumps(json_items, indent="  "))
