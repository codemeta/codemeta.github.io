---
title: "The Codemeta JSON-LD Representation"
---


CodeMeta uses JSON-LD to represent and translate between software metadata formats.  JSON-LD lead developer Manu Sporny explains how JSON-LD works in this short clip:


{{< youtube Tm3fD89dqRE >}}



## The JSON-LD Context File

The current codemeta context file can be used from <https://w3id.org/codemeta/3.0> -- note that browsers will redirect using _content negotiation_ to a HTML page, while JSON-LD processors will get the JSON-LD context.

### Released versions

* <https://w3id.org/codemeta/3.0>
* <https://doi.org/10.5063/schema/codemeta-2.0>
* <https://doi.org/10.5063/schema/codemeta-1.0>

### CodeMeta terms

CodeMeta properties are built on and extend software properties from <https://schema.org>.  A list of all properties provided by the current CodeMeta `context` file can be found on the [terms](/terms) page. Here's an example [codemeta.json file](https://github.com/codemeta/codemetar/blob/master/codemeta.json) for the `codemetar` R package.  

## Compaction & expansion examples: 

