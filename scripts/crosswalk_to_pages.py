"""Transforms crosswalk.csv field headers into md files.

This recreates the old existing files. Some were a little
bit special.

Everything special is stored in data/crosswalk_pages.json
"""

import re
import csv
import json
import pathlib

DIR = pathlib.Path(__file__).parent.parent
CW_CSV = DIR / "data/crosswalk.csv"
MD_DIR = DIR / "content/crosswalk"
ORIDES_PATH = DIR / "data/crosswalk_pages.json"

# Get our override values
try:
    with open(ORIDES_PATH, 'r', encoding='utf-8') as orides_f:
        orides = json.load(orides_f)
except FileNotFoundError:
    raise FileNotFoundError(f"The data overrides file '{ORIDES_PATH}' could not be opened.")

# Get crosswalk.csv header fieldnames
try:
    with open(CW_CSV, 'r') as f:
        csv_dict = csv.DictReader(f)
        cw_stems = csv_dict.fieldnames[4:]
except FileNotFoundError:
    raise FileNotFoundError(f"The CodeMeta properties file '{CW_CSV}' could not be opened.") 

# Do we have anything to parse? If not, raise an error about that
if len(cw_stems) > 0:
    for stem in cw_stems:
        stem_clean = real_stem = stem.strip()
        stem_slug = re.sub(r'[^a-zA-Z0-9]+', '-', stem_clean)

        # Find our stem in the overrides file
        match = next((item for item in orides if (item["stem"] == real_stem) or (item["short"] == real_stem) or (item["name"] == real_stem)), None)

        # If a name exists, use it or stick with the cleaned stem name
        try:
            vocab_name = match["name"]
        except (TypeError, KeyError):
            vocab_name = stem_clean
            pass

        # If a shortname exists, we want this for the .md filename
        try:
            stem_slug = match["short"]
        except (TypeError, KeyError):
            pass

        # If there's an image defined, use it, if not use the codemeta.png as placeholder
        try:
            vocab_img = match["img"]
        except (TypeError, KeyError):
            vocab_img = f"image: /img/codemeta.png"
            pass
        else:
            # of course check if it exists and if not use the same placeholder
            img_path = DIR / "static/img" / vocab_img
            img_path = pathlib.Path(img_path)
            if img_path.is_file():
                vocab_img = f"image: /img/{vocab_img}"
            else:
                vocab_img = f"image: /img/codemeta.png"

        # A few pages had text after the table to refer back to other versions of the schemas
        # this seems useful enough to preserve
        try:
            vocab_foot = match["foot"]
        except (TypeError, KeyError):
            vocab_foot = ""
            pass
        else:
            vocab_foot = f"{{{{% crosswalks_footnote name='{stem_clean}' %}}}}"

        # Only some have dates. TODO Can be patched in later
        try:
            vocab_date = match["date"]
        except (TypeError, KeyError):
            date_formatted = ""
            pass
        else:
            date_formatted = f"date: {vocab_date}"

        # A Software Ontology has no name. Keep it special for now.
        if vocab_name == "":
            title = f"title: \"Crosswalk\""
            vocab_name = stem_clean
        else:
            title = f"title: \"Crosswalk for {vocab_name}\""

        md_text = f"""---
{title}
vocab: "{vocab_name}"
slug: "{stem_slug}"
{vocab_img}
{date_formatted}
---

{{{{% crosswalks_desc name="{stem_clean}" %}}}}

{{{{% crosswalk name="{real_stem}" %}}}}

{vocab_foot}"""

        # preserve filename casing only for diff readability
        if len(stem_slug) > 1:
            stem_slug = stem_slug.lower()

        # Write our shiny markdown file for the crosswalk.
        cw_md = MD_DIR / f"{stem_slug}.md"
        cw_md.write_text(md_text)
else:
    # Oops?
    raise ValueError("The crosswalk.csv file had zero entries, is it empty?!");
