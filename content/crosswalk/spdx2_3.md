---
title: "Crosswalk for SPDX 2.3 SBOM"
image: "/img/spdx.png"
date: "2024-01-15"
---

The [Software Package Data Exchange® (SPDX®)](https://spdx.dev/) specification defines a standard data format for communicating the component and metadata information associated with software packages, widely known as "software bill of materials" or "SBOM". An SPDX document can be associated with a set of software packages, files or snippets.

SPDX 2.3 supports multiple serialization formats and often uses the following file extensions:

| Serialization format | File extension(s)              |
|----------------------|--------------------------------|
| tag:value            | `*.spdx`                       |
| JSON                 | `*.spdx.json`                  |
| RDF (RDF/XML)        | `*.spdx.rdf`, `*.spdx.rdf.xml` |
| XLS spreadsheet      | `*.spdx.xls`, `*.spdx.xlsx`    |
| XML                  | `*.spdx.xml`                   |
| YAML 1.2             | `*.spdx.yaml`, `*.spdx.yml`    |

The crosswalk for the SPDX 2.3 SBOM is as follows:

{{< crosswalk name="SPDX 2.3" >}}
