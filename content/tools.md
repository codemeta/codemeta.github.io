---
markup: mmark
---

### Tools

This page lists some existing tools to help with CodeMeta files

#### File Generation

 Some of the early tools still need a little updating to use the latest version of the codemeta context.

{.table .table-striped}

tool | language | codemeta version | maintainer | notes
-----|----------|------------------|------------|--------------
[CodeMeta file generator](https://gist.github.com/arfon/478b2ed49e11f984d6fb) | Ruby | 0.1.0 | [arfon](http://github.com/arfon) | (no support for current schema)
[Bolognese](https://github.com/datacite/bolognese) | Ruby | 1.0.0 | [mfenner](https://github.com/mfenner) | primarily a tool for conversion between formats provided by DataCite, including codemeta and schema.org
[codemetar](https://ropensci.github.io/codemetar) | R | 2.0.0 | [cboettig](https://github.com/cboettig) | Generate codemeta for R packages; + generic codemeta manipulation
[codemetapy](https://github.com/proycon/codemetapy) | Python | 2.0.0 | [proycon](https://github.com/proycon) | Generate codemeta for Python packages
[tributors](https://con.github.io/tributors/) | Python | 2.0.0 | [vsoch](https://github.com/vsoch) | Generate codemeta contributors section from GitHub API and Orcid API
[cff-converter](https://github.com/citation-file-format/cff-converter-python) | Python | 2.0.0 | [jspaaks](https://github.com/jspaaksh) | Convert `CITATION.cff` files to codemeta
[CodeMeta generator](https://codemeta.github.io/codemeta-generator/) | Javascript | 2.0.0 | [ProgVal](https://github.com/ProgVal) | Online form to create or complete a codemeta file



#### Integrations


Integrations indicate existing platforms & services which understand CodeMeta descriptions. These do not provide a user-facing software tool for generating codemeta.json, but can ingest
existing codemeta.json files automatically.

{.table .table-striped}

Name | Description |  Authors | Language | Codemeta Version
-----|-------------|----------|----------|--------------------
[Fidgit](https://github.com/arfon/fidgit): | An ungodly union of GitHub and Figshare | Arfon Smith, Kaitlin Thaney, Mark Hahnel | Ruby | 0.1.0
[Software Heritage](https://docs.softwareheritage.org/devel/swh-indexer/metadata-workflow.html#adding-support-for-additional-ecosystem-specific-metadata)|The metadata indexers | SWH team | Python | 2.0


Pending:


- JOSS
- Zenodo
- DataCite
- Figshare 


