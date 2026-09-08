---
title: "The CodeMeta JSON-LD Representation"
layout: sidenav
---

CodeMeta uses JSON-LD to represent and translate between software metadata formats.
JSON-LD lead developer Manu Sporny explains how JSON-LD works in this short clip:

{{% youtube Tm3fD89dqRE %}}

## The JSON-LD Context File

{{% badge %}}

Context file of released versions:

- CodeMeta 4.0: <https://w3id.org/codemeta/4.0>
- CodeMeta 3.1: <https://w3id.org/codemeta/3.1>
- CodeMeta 3.0: <https://w3id.org/codemeta/3.0>
- CodeMeta 2.0: <https://doi.org/10.5063/schema/codemeta-2.0>
- CodeMeta 1.0: <https://doi.org/10.5063/schema/codemeta-1.0>

## CodeMeta terms

CodeMeta properties are built on and extend software properties from
<https://schema.org>.
A list of all properties provided by the current CodeMeta `context` file can be
found on the [terms](/terms) page. Here's an example
[codemeta.json file](https://github.com/gem-pasteur/macsyfinder/blob/master/codemeta.json)
for the `gem-pasteur/macsyfinder` project.
