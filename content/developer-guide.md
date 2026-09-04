---
title: CodeMeta Developer Guide
layout: sidenav
---

This guide is intended for software developers who require detailed information about the CodeMeta project's
usage of JavaScript Object Notation for Linked Data ([JSON-LD](http://json-ld.org/)) for defining a
methodology for creating software package descriptions. For example, this guide may be helpful for developers that are
designing software to generate or read CodeMeta JSON software descriptions.

Users that only require instructions for manually creating CodeMeta software descriptions may wish to
review the upcoming [User Guide](/user-guide/).

## CodeMeta Overview

The CodeMeta project strives to promote the citation and reuse of software authored for scientific research by developing a mechanism to assist the transfer of software and software metadata between the entities that author, archive, index and distribute and use the software. Our approach is not to create a new metadata standard or schema, but instead to define a crosswalk between existing software metadata schemas, and to provide a uniform method to package and transfer this metadata between entities.

(A complete description of the CodeMeta project can be found here [https://github.com/codemeta/codemeta-paper](https://github.com/codemeta/codemeta-paper).)

The mechanism to package and transfer software descriptions that the CodeMeta project has adopted uses [JSON-LD](http://json-ld.org/),
which is a W3C standard that enables JSON based documents to be universally understandable and processable
by adhering to principles outlined for [linked data](https://en.wikipedia.org/wiki/Linked_data):

- Use URIs to name (identify) resources so that they can be located and retrieved.
- Provide useful information about what a name identifies when it's looked up, using open standards.
- Refer to other things using their HTTP URI-based names when publishing them on the Web.

The JSON-LD [Best Practices guide](http://json-ld.org/spec/latest/json-ld-api-best-practices/) describes linked data as:

> Linked Data is a way to create a network of standards-based machine interpretable data
> across different documents and Web sites. It allows an application to start at one piece of Linked
> Data, and follow embedded links to other pieces of Linked Data that are hosted on different
> sites across the Web.

JSON-LD is a W3C standard, specified at https://www.w3.org/TR/json-ld/

## CodeMeta Metadata Usage

JSON-LD uses a *context file* to associate JSON names with IRIs (Internationalized Resource Identifier).  The JSON names then serve as abbreviated, local names for the IRIs that are universally unique identifiers for concepts from widely used schemas such as [schema.org](http://schema.org).

The context file [*codemeta.jsonld*](https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld) contains the complete set of JSON properties adopted by the CodeMeta project.

A CodeMeta software description, or *CodeMeta document*, uses the JSON names contained in the context file. The JSON names are more compact and easier to process than IRIs. The CodeMeta document can be used to transfer metadata between software authors, repositories, and others, for the purposes of archiving, sharing, indexing, citing and discovering software.

Because the CodeMeta document refers to the context file, the mapping between the local JSON names and the
IRIs is always known, thereby giving the local names universal context.

An example usage of the CodeMeta document is for the author of research software package to generate a CodeMeta Document when the software package is published to a repository. The CodeMeta Document can be used to aid in any repository ingest processing. The CodeMeta Document can be made available in the repository with the software package as it may contain additional metadata that was not used by the repository. In addition this file may be used in other transactions involving the software package after the package has been downloaded from the repository.

The producer of an CodeMeta Document, i.e. the creators of the software, must use the JSON names from the CodeMeta context file. The consumer of the CodeMeta Document can use these same JSON names from the CodeMeta Document for any necessary processing tasks.

As an alternative to using the producer supplied JSON names, the consumer can use the [JSON-LD API](https://www.w3.org/TR/json-ld-api/) to translate the JSON names to their own local JSON names that may be in use by their local processing scripts. This is done by first using the JSON-LD *expand* function that replaces each JSON name in the CodeMeta Document with it's corresponding IRI from the CodeMeta context file. For example, the producer's CodeMeta Document may contain the following line:

```json
      "codeRepository": "https://github.com/DataONEorg/rdataone"
```

Using the JSON-LD API *expand* function, this is converted to:

```json
     "http://schema.org/codeRepository": "https://github.com/DataONEorg/rdataone"
```

Next, the consumer can use their own context file that maps from each IRI to their own local JSON names. For example, the consumer may have a context that maps the local JSON name 'repository' (as in `package.json` documents used by NPM, see [/crosswalk/node/]) to "http://schema.org/codeRepository", so using the JSON API *compact* function would result in a new CodeMeta Document with the entry:

```json
     "repository": "https://github.com/DataONEorg/rdataone"
```

When the CodeMeta Document has been compacted, it can then be used by the consumer for any necessary processing, using the local JSON names.

Note that this expansion and compaction process assumes that both the producer and consumer JSON-LD context files share overlapping sets of IRIs.

## Crosswalk Table

## Tools and Integrations

To facilitate automated ingest of research software into repositories such as [figshare](https://figshare.com/), [Zenodo](https://zenodo.org/), the [Knowledge Network for Biocomplexity](https://knb.ecoinformatics.org/) and others, these repositories will update
their submission processes to use CodeMeta Document which will provide the metadata necessary for the submission and indexing of the software.  

Tools will be created that assist in the generation of CodeMeta documents. For example, a tool written in the R language would generate a CodeMeta document from an R package that was authored to support a research project, automatically collecting available metadata and possibly prompting the user for any additional required metadata. The CodeMeta document would then be used to assist in publishing the software to a repository. An example CodeMeta document is shown in Appendix C.

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

Citations may also be generated from CodeMeta documents and combined with an
identifier such as a commit hash or a long-term stable identifier like a
[Software Hash Identifier (SWHID)](https://swhid.org) for better accuracy.

These citations also use extended entry types. Along with `@softwareversion`
the `@codefragment` entry type can be used. SWHIDs can also reference a file,
or code selection,

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

References an exact version of CodeMeta stored in the
[Software Heritage Archive](https://archive.softwareheritage.org), along with
its origin and a snapshot reference. The use of a SWHID allows for a precise
point in CodeMeta's history to be referenced. Future researchers will be able
to obtain the code at that precise point by looking up the SWHID in the Archive
or a mirror.

## Extending the CodeMeta Context

CodeMeta explicitly defines the terms it uses from <http://schema.org>, rather than merely extending <http://schema.org> with a few additional terms.  To use additional terms from <http://schema.org> not listed on the [terms page](/terms/) (or terms from any other context), you must extend your context appropriately.  For instance, to combine CodeMeta (v3.1) with all terms available in schema.org, you would do:

```json
"@context": ["https://w3id.org/codemeta/3.1", "http://schema.org/"]
```

Note the default context should be listed last.  

## Appendix A JSON-LD Relationship to RDF

The intent of JSON-LD is to provide a mechanism to represent linked data using standard JSON syntax, yet JSON-LD was developed as a W3C Standard by the RDF Working Group. Even though JSON-LD can be effectively used without converting a JSON-LD document to RDF, it is useful to consider the relationship of JSON-LD to RDF in order to fully understanding JSON-LD.

For example, in the CodeMeta document, the JSON-LD "@id" keyword is used to associate an IRI with a JSON object. When the JSON-LD CodeMeta document is serialized to RDF, this becomes the graph node identifier, or the subject of the resulting RDF triple. If an @id is not specified for a JSON object, then a blank node identifier is assigned to the resulting graph node for the output RDF graph. The JSON object `role` from the example
CodeMeta document:

```json
      "roleCode":[
         "originator",
         ...
      ]
```

is serialized to RDF as:

```n3
_:b1 <https://codemeta.github.io/terms/roleCode> "originator" .
```

When the JSON-LD "@type" keyword is applied to a simple JSON type, the serialized RDF will have that type appended to the object, for example, the following entry from the example CodeMeta document:

```json
"dateCreated":"2016-05-27"
```

is serialized to the following RDF ([N-Triples format](https://www.w3.org/TR/n-triples/)):

```n3
_:b0 <http://schema.org/dateCreated> "2016-05-27"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
```

In this case, the "@type" was specified in the context file.

When the JSON-LD "@type" is applied to a JSON object, the type information is serialized to RDF with
an RDF type statement, for example, this JSON object from the sample CodeMeta document:

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

```n3
<http://orcid.org/0000-0002-3957-2474> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .

```

This example shows the "@type" keyword being used in the CodeMeta document.
