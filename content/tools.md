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
[codemetar](https://codemeta.github.io/codemetar) | R | 2.0.0 | [cboettig](https://github.com/cboettig) | Generate codemeta for R packages; + generic codemeta manipulation



#### Integrations


Integrations indicate existing platforms & services which understand CodeMeta descriptions. These do not provide a user-facing software tool for generating codemeta.json, but can ingest
existing codemeta.json files automatically.

{.table .table-striped}

Name | Description |  Authors | Language | Codemeta Version
-----|-------------|----------|----------|--------------------
[Fidget](https://github.com/arfon/fidgit): | An ungodly union of GitHub and Figshare | Arfon Smith, Kaitlin Thaney, Mark Hahnel | Ruby | 0.1.0


Pending:


- JOSS
- Zenodo
- DataCite
- Figshare 


