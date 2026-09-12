---
title: CodeMeta Developer Guide
layout: sidenav
---

This guide is intended for software developers who require detailed information
about the CodeMeta project's usage of JavaScript Object Notation for Linked Data
([JSON-LD](http://json-ld.org/)) for defining a methodology for creating
software package descriptions. The information below, and the [Tools page] may
be helpful for developers that are designing software to generate or read
CodeMeta JSON software descriptions.

Users that only require instructions for manually creating CodeMeta software
descriptions may prefer the [User Guide](/user-guide/).

## CodeMeta Overview

The CodeMeta project strives to promote the citation and reuse of software
authored for scientific research. It does this by developing a mechanism to
assist the transfer of software and software metadata between the entities
that author, archive, index and distribute and use the software. The project's
intention was not to create a new metadata standard or schema, but instead to
define a crosswalk between existing software metadata schemas, and to provide a
uniform method to package and transfer this metadata between entities.

A complete description of the CodeMeta project can be found in the
[CodeMeta paper](https://github.com/codemeta/codemeta-paper).

CodeMeta's mechanism to package and transfer software descriptions uses
[JSON-LD](http://json-ld.org/).

[JSON-LD is a W3C standard](https://www.w3.org/TR/json-ld/) that enables JSON
based documents to be universally understandable and processable by adhering to
principles outlined for [linked data](https://en.wikipedia.org/wiki/Linked_data):

- Use URIs to name (identify) resources so that they can be located and
retrieved.
- Provide useful information about what a name identifies when it's looked up,
using open standards.
- Refer to other things using their HTTP URI-based names when publishing them
on the Web.

The JSON-LD [Best Practices guide](http://json-ld.org/spec/latest/json-ld-api-best-practices/)
describes linked data as:

> Linked Data is a way to create a network of standards-based machine interpretable data
> across different documents and Web sites. It allows an application to start at one piece of Linked
> Data, and follow embedded links to other pieces of Linked Data that are hosted on different
> sites across the Web.

## CodeMeta Metadata Usage

JSON-LD uses a *context file* to associate JSON names with IRIs
(Internationalized Resource Identifier). The JSON names then serve as
abbreviated, local names for the IRIs that are universally unique
identifiers for concepts from widely used schemas such as
[schema.org](http://schema.org).

The context file
[*codemeta.jsonld*](https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld)
contains the complete set of JSON properties adopted by the CodeMeta project.

A CodeMeta software description, or *CodeMeta document*, uses the JSON names
contained in the context file. The JSON names are more compact and easier to
process than IRIs. The CodeMeta document can be used to transfer metadata
between software authors, repositories, and others, for the purposes of
archiving, sharing, indexing, citing and discovering software.

Because the CodeMeta document refers to the context file, the mapping between
the local JSON names and the IRIs is always known, thereby giving the local
names universal context.

Any one CodeMeta document can have many applications. Consider the following
story:

1. The author of a research software package generates a CodeMeta document when
the software package is published to a repository.
1. The CodeMeta document is able to assist with repository ingest processing.
1. The CodeMeta document remains available in the repository, providing
additional metadata which may not have been used by that ingest process.
1. The software package may then be downloaded from the repository.
1. The included CodeMeta document is used in additional transactions involving
the software package, after it has been downloaded from the origin repository.

The **producer** of a CodeMeta document, i.e. the creators of the software,
must use the JSON names from the CodeMeta context file. The consumer of the
CodeMeta Document can use these same JSON names from the CodeMeta document for
any necessary processing tasks.

As an alternative to using the producer supplied JSON names, the **consumer**
can use the [JSON-LD API](https://www.w3.org/TR/json-ld-api/) to translate the
JSON names to their own local JSON names that may be in use by their local
processing scripts. This is done by first using the JSON-LD *expand* function
that replaces each JSON name in the CodeMeta Document with it's corresponding
IRI from the CodeMeta context file. For example, the producer's CodeMeta
Document may contain the following line:

```json
      "codeRepository": "https://github.com/DataONEorg/rdataone"
```

Using the JSON-LD API *expand* function, this is converted to:

```json
     "http://schema.org/codeRepository": "https://github.com/DataONEorg/rdataone"
```

Next, the consumer can use their own context file that maps from each IRI to
their own local JSON names. For example, the consumer may have a context that
maps the local JSON name 'repository' (as in `package.json` documents used by
NPM, see [/crosswalk/node/]) to "http://schema.org/codeRepository", so using
the JSON API *compact* function would result in a new CodeMeta Document with
the entry:

```json
     "repository": "https://github.com/DataONEorg/rdataone"
```

When the CodeMeta Document has been compacted, it can then be used by the
consumer for any necessary processing, using the local JSON names.

Note that this expansion and compaction process assumes that both the producer
and consumer JSON-LD context files share overlapping sets of IRIs.
{.tip}

## Crosswalk Tables

The Crosswalk tables are reference tables that provides mappings from one
format to another. The formats do not require 1:1 mappings, meaning that
neither vocabulary needs to match every term of the other.

Some mappings may represent partial data matches. In some cases one side of the
map may be more specific than the other; "id" values are a good example of
this. For example, some vocabularies may require a specific type of id, such as
ORCID but the other vocabulary can accept any form of id. The
[diagram on the crosswalk page](/crosswalk/) illustrates the variety of these
match relationships.

Crosswalks are one of the primary reasons and features of CodeMeta; the
intention for CodeMeta was not [to make a new](https://xkcd.com/927/)
vocabulary of its own, but instead to make conversion easy. As a result,
Crosswalks have been developed for CodeMeta and many other vocabularies. They
can be found in the [Crosswalk directory](/crosswalk#crosswalk-directory).

## Tools and Integrations

To facilitate automated ingest of research software into repositories such as
[figshare](https://figshare.com/), [Zenodo](https://zenodo.org/), the
[Knowledge Network for Biocomplexity](https://knb.ecoinformatics.org/), and
others, many of these repositories updated their submission processes to use
CodeMeta documents which provide the metadata necessary for the submission and
indexing of the software.

[Various tools](/tools/) have been created that assist in the generation of
CodeMeta documents, as well as migrations of data to and from the CodeMeta
format.

Many of these tools generate a CodeMeta document from existing available
information such as package manifests and code forge repository data. Some also
prompt the user for specific input to build a more complete CodeMeta document.

These contributions to the CodeMeta ecosystem exist because they were authored
for a purpose, such as to support a research project. They were shared with the
community so that they may assist others. This allows CodeMeta to be adopted
with greater ease, and assists with better pipelines for publishing software.

## Generating Citations from a CodeMeta Document

Enabling useful citations for reproducibility is one of the core purposes of
CodeMeta.

Citations for software packages are generated from CodeMeta documents by
converting the metadata into a modern [BibTeX format](https://www.bibtex.org/)
using [BibLaTeX format](https://www.biblatex.org/) and the
[BibLaTeX-software](https://www.ctan.org/pkg/biblatex-software) module that
enriches and expands the `@software` entry type.

If your citation data is not currently in a codemeta document, it can be
converted by using [a Crosswalk](/crosswalk#crosswalk-directory) for reference
or with the help of various [tools](/tools#converters).

### Citations for Stable Versions

These citations use the BibLaTeX-software `@softwareversion` entry type. They
are useful for citing a software version by a stable published release number.

Citations generated against stable published releases may be of limited use if
the software used in research is following an actively changing branch. See
the next section if this description resembles your situation.

Conversion from CodeMeta into a BibLaTeX-flavored BibTeX citation follows the
[BibTeX (@softwareversion) Crosswalk](/crosswalk/bibtex-softwareversion). This
mapping is only for the `@softwareversion` entry type.

The BibTeX generation can be done manually, or with a [tool](/tools/) such as
[Bolognese](https://github.com/datacite/bolognese).

The following in CodeMeta:

```json
{
    ...
    "name": "example-app",
    "softwareVersion": "1.2.3",
    ...
}
```

Would be represented in BibLaTeX as:

```bib
@softwareversion{example-app,
    ...
    version = "1.2.3"
    ...
}
```

### Citations for Active Development

Hashes should not be stored in CodeMeta, as this creates a race condition.
{.warning}

BibTeX citations may also be generated from CodeMeta documents and enhanced
with an identifier such as a commit hash or a long-term stable identifier for
better accuracy.

These citations also use extended entry types. Along with `@softwareversion`
the `@codefragment` entry type can be used. SWHIDs can also reference a file,
or code selection.

The following BibTeX citation:

```bib
@softwareversion{swh-dir-833177a,
    author = "Boettiger, Carl and Jones, Matthew B.",
    license = "Apache-2.0",
    abstract = "CodeMeta is a concept vocabulary that can be used to standardize the exchange of software metadata across repositories and organizations.",
    date = "2017-06-05",
    year = "2017",
    month = jun,
    file = "https://github.com/codemeta/codemeta/archive/2.0.zip",
    repository = "https://github.com/codemeta/codemeta",
    title = "CodeMeta: Minimal metadata schemas for science software and code, in JSON-LD",
    version = "2.0",
    swhid = "swh:1:dir:833177a48dc997f12b1786080dc32f67b3d3e4e0;origin=https://github.com/codemeta/codemeta.git;visit=swh:1:snp:c3c7f3ac853a2c6f07e73803f81df359a4851dc8;anchor=swh:1:rev:bae605fef4331833d608780051503108f0bbd59b"
}
```

References an exact copy of CodeMeta that aligns with a specific commit hash.

In that example, the hash or long-term stable identifier used is a
[Software Hash Identifier (SWHID)](https://swhid.org) which points to
[an archived copy](https://archive.softwareheritage.org/browse/directory/833177a48dc997f12b1786080dc32f67b3d3e4e0/?origin_url=https://github.com/codemeta/codemeta.git&revision=bae605fef4331833d608780051503108f0bbd59b&snapshot=c3c7f3ac853a2c6f07e73803f81df359a4851dc8)
of the repository. The use of a SWHID allows for a precise point in CodeMeta's
history to be referenced even if the origin repository is lost. Future
researchers will be able to obtain the code at that precise point by looking up
the SWHID in that archive, or a mirrored copy of it.

### Why not Citation File Format (CFF)?

[CFF](https://citation-file-format.gihub.io) is also a good way to record
metadata for citations, in particular if human-readability is a priority.
CodeMeta is more intended for being indexed by machines. It may be worth using
both, based on your circumstances. Some people prefer to maintain one
document instead of multiple documents. Each schema has its own approach for
which data is recorded and how. Use the one that best fits your requirements
and preferences.

Because CodeMeta aims to be a translation layer between different formats, it
also supports certain other technical and administrative metadata that CFF does
not; such as `funding`. Refer to the [terms](/terms/) page to see what CodeMeta
supports. Some pipelines that process `codemeta.json` documents will defer to a
`CITATION.cff` where one is available, and use `codemeta.json` for metadata
that CFF does not support.

Neither format is a committment. A `CITATION.cff` can be derived from a
`codemeta.json`, and a `codemeta.json` can be populated from a `CITATION.cff`.
There are various [tools](/tools/) available to help with this.

## Extending the CodeMeta Context

CodeMeta explicitly defines the terms it uses from <https://schema.org>, rather
than merely extending <https://schema.org> with a few additional terms. To use
additional terms from <https://schema.org> not listed on the [terms page](/terms/)
(or terms from any other context), you must extend your context appropriately.
For instance, to combine CodeMeta (v3.1) with all terms available in schema.org,
you would do:

```json
"@context": ["https://w3id.org/codemeta/3.1", "http://schema.org/"]
```

Note that the default context should be listed last.
{.tip}

## JSON-LD Relationship to RDF

The intent of JSON-LD is to provide a mechanism to represent linked data using
standard JSON syntax, yet JSON-LD was developed as a W3C Standard by the RDF
Working Group. Even though JSON-LD can be effectively used without converting
a JSON-LD document to RDF, it is useful to consider the relationship of JSON-LD
to RDF in order to fully understanding JSON-LD.

For example, in the CodeMeta document, the JSON-LD `@id` keyword is used to
associate an IRI with a JSON object. When the JSON-LD CodeMeta document is
serialized to RDF, this becomes the graph node identifier, or the subject of
the resulting RDF triple. If an `@id` is not specified for a JSON object, then
a blank node identifier is assigned to the resulting graph node for the output
RDF graph.

The JSON object `role`:

```json
    "programmingLanguage":[
      "Python",
      "C++",
    ...
      ]
```

is serialized to RDF as:

```turtle
_:b1 <https://codemeta.github.io/terms/programmingLanguage> "Python" .
_:b1 <https://codemeta.github.io/terms/programmingLanguage> "C++" .
```

When the JSON-LD `@type` keyword is applied to a simple JSON type, the
serialized RDF will have that type appended to the object, for example, the
following entry:

```json
"dateCreated":"2016-05-27"
```

is serialized to the following RDF ([N-Triples format](https://www.w3.org/TR/n-triples/)):

```turtle
_:b0 <http://schema.org/dateCreated> "2016-05-27"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
```

In this case, the `@type` was specified in the context file.

When the JSON-LD `@type` is applied to a JSON object, the type information is
serialized to RDF with an RDF type statement, for example, this JSON object:

```json
"author":[
  {
     "@id":"http://orcid.org/0000-0002-3957-2474",
     "@type":"Person",
    ...

  }
]
```

is serialized to RDF as:

```turtle
<http://orcid.org/0000-0002-3957-2474> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .

```

This example shows the `@type` keyword being used.
