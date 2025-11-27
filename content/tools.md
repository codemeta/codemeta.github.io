---
title: Tools
layout: sidenav
---

This page lists some existing tools to help with CodeMeta files.

## File Generation

Some of the early tools still need a little updating to use the latest version of the CodeMeta context.

Name | Language | CodeMeta versions | Maintainers | Description
-----|----------|-------------------|-------------|------------
[AutoCodemeta Generator](https://w3id.org/autocodemeta) | JavaScript | 3.0.0 | [dgarijo](http://github.com/dgarijo) | Optimized version of CodeMeta Generator that automatically creates a CodeMeta file from a given repository
[Bolognese](https://github.com/datacite/bolognese) | Ruby | 1.0.0 | [mfenner](https://github.com/mfenner) | Primarily a tool for conversion between formats provided by DataCite, including CodeMeta and schema.org
[cff-converter](https://github.com/citation-file-format/cff-converter-python) | Python | 2.0.0 | [jspaaks](https://github.com/jspaaksh) | Convert `CITATION.cff` files to codemeta
[CodeMeta file generator](https://gist.github.com/arfon/478b2ed49e11f984d6fb) | Ruby | 0.1.0 | [arfon](http://github.com/arfon) | (no support for current schema)
[CodeMeta generator](https://codemeta.github.io/codemeta-generator/) | JavaScript | 2.0.0, 3.0.0 | [ProgVal](https://github.com/ProgVal) | Online form to create or complete a CodeMeta file
[codemeta-harvester](https://github.com/proycon/codemeta-harvester) | POSIX Shell | 2.0.0, 3.0.0 | [proycon](https://github.com/proycon) | Automatic software metadata conversion pipeline that uses codemetapy and other tools
[codemeta-server](https://github.com/proycon/codemeta-server) | Python | 2.0.0, 3.0.0 | [proycon](https://github.com/proycon) | Webservice offering an API (including SPARQL) and simple human web-interface so search and browse software metadata
[codemetapy](https://github.com/proycon/codemetapy) | Python | 2.0.0, 3.0.0 | [proycon](https://github.com/proycon) | Generate CodeMeta for Python, NodeJS, Java packages and others; + generic CodeMeta manipulation
[codemetar](https://ropensci.github.io/codemetar) | R | 2.0.0 | [cboettig](https://github.com/cboettig) | Generate CodeMeta for R packages; + generic CodeMeta manipulation
[FACILE-RS](https://git.opencarp.org/openCARP/FACILE-RS) | Python | 2.0.0 | [MarieHouillon](https://github.com/MarieHouillon) | Metadata conversion (to Citation File Format (CFF), DataCite, BagIt and BagPack) and software publication pipelines based on CodeMeta. Previously known as openCARP-CI.
[Somef](https://github.com/KnowledgeCaptureAndDiscovery/somef) | Python | OEG developers | [dgarijo](http://github.com/dgarijo) | Tool that automatically extracts software metadata from repositories and scientific publications
[tributors](https://con.github.io/tributors/) | Python | 2.0.0 | [vsoch](https://github.com/vsoch) | Generate CodeMeta contributors section from GitHub API and ORCID API
{.table .table-striped}

## Integrations

Integrations indicate existing platforms & services which understand CodeMeta descriptions.
These do not provide a user-facing software tool for generating codemeta.json, but can ingest
existing codemeta.json files automatically.

Name | Language | CodeMeta versions | Maintainers | Description
-----|----------|-------------------|-------------|------------
[Fidgit](https://github.com/arfon/fidgit) | Ruby | 0.1.0 | Arfon Smith, Kaitlin Thaney, Mark Hahnel | An ungodly union of GitHub and Figshare
[Software Heritage](https://docs.softwareheritage.org/devel/swh-indexer/metadata-workflow.html#adding-support-for-additional-ecosystem-specific-metadata) | Python | 2.0 | SWH team | The metadata indexers
{.table .table-striped}

Pending:

- DataCite
- Figshare
- JOSS
- Zenodo
