---
title: User Guide
layout: sidenav
---

## What are CodeMeta files?

CodeMeta files, also called "CodeMeta instance files" are the `codemeta.json`
documents that are placed in the root of a software's code repository tree.
They define various aspects of the project in a JSON variant called JSON-LD,
which uses linking attributes to connect the data in this file with data from
other available sources.

## The CodeMeta Generator

The CodeMeta Generator is a tool for taking user input and either generating a
valid `codemeta.json` file, or testing an existing file to make sure that it
is valid.

### Generating a CodeMeta instance file

CodeMeta files can be generated using the
[CodeMeta Generator](https://codemeta.github.io/codemeta-generator/).
Instructions for [using the CodeMeta Generator](create) are available.

A _*beta*_ version of an automatic generator is also linked on that page.

### Testing a CodeMeta instance file

Your CodeMeta files can be validated using the
[codemeta-generator](https://codemeta.github.io/codemeta-generator/). Paste
the contents of a `codemeta.json` file into the bottom box, and click the
`Validate codemeta.json` button.

## Creating a CodeMeta instance file manually

A CodeMeta instance file describes the metadata associated with a software
object using JSON's linked data (JSON-LD) notation. A CodeMeta file can
contain any of the properties described on the [CodeMeta terms page](terms).

Any plaintext or code editor is sufficient for creating a CodeMeta instance
file. An editor that has syntax highlighting for `JSON` can assist by
making errors in the syntax stand out.

Most CodeMeta files are called `codemeta.json` by convention. While other
filenames are valid, they will be less recognisable and may be overlooked.
{.tip}

### Understanding JSON and JSON-LD

CodeMeta files contain JSON *key-value pairs*, sometimes referred to as
*name-value pairs* where the values can be *simple values*, *arrays*, or *JSON
objects*. Keys are also known as *properties* in linked data.

#### Simple Values

A simple value is a number, string, or one the literal values *false*, *null*
*true*. For example:

```json
"name" : "R Interface to the DataONE REST API"
```

Key-value pairs must be separated by a comma. There must be no comma at the
end before the closing brace (`}`).

#### Arrays

A JSON array is surrounded by parentheses; `[` and `]`. Arrays can contain
one or multiple values separated by commas:

```json
"keywords": [ "data sharing", "data repository", "DataONE" ]
```

Arrays should contain line breaks between values and indenting (spaces at the
start of a line). These make the data easier for humans to read. The above
example is equivalent to:

```json
"keywords": [
    "data sharing",
    "data repository",
    "DataONE"
]
```

Fields that accept a value of a given type will accept an array of values of
that type. For example, a software with two licenses could have this
attribute:

```json
"license": [
    "https://spdx.org/licenses/GPL-3.0-or-later",
    "https://spdx.org/licenses/BSD-3-Clause"
]
```

#### Objects

Some properties, such as `author`, can refer to other JSON objects. Objects
are surrounded by braces; `{` and `}`. These can contain other JSON values or
objects. For example:

```json
"author": {
    "@id": "http://orcid.org/0000-0003-0077-4738",
    "@type": "Person",
    "email": "slaughter@nceas.ucsb.edu",
    "givenName": "Peter",
    "familyName": "Slaughter"
}
```

#### Keywords

JSON-LD has the concept of Keywords, which are properties prefaced with a `@`.
Keywords give instructions to the processor instead of describing relations
between entities.

This includes:

* defining shorthands (`@context`, `@vocab`),
* changing value semantics (`@list` and `@set`, `@value`, `@language`, ...),
* intrinsically describing objects (`@id` and `@type`)

The JSON-LD `@type` keyword associates a JSON value or object with a well
known type. In the previous example, the statement `"@type":"Person"`
associates the `author` object with `http://schema.org/Person`. The
`@type` for any property which specifies a node (JSON object) should be
provided. The `Type` column of [the terms page](/terms/) indicates the
options appropriate for each term.

The `author` JSON object illustrates the use of the JSON-LD keyword `@id`,
which is used to associate an IRI with the JSON object. Any such node object
can be assigned an `@id`, and future uses of the `@id` property's *value* will
refer to this same object, (the person, Peter), elsewhere in the document. For
example, we can indicate the same individual is also the `maintainer` by
adding:

```json
"maintainer": "http://orcid.org/0000-0003-0077-4738"
```

This should be added at the top level of the document, indicating that this
individual is the `maintainer` of the software being described, like this:

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "author": {
        "@id": "http://orcid.org/0000-0003-0077-4738",
        "@type": "Person",
        "email": "slaughter@nceas.ucsb.edu",
        "givenName": "Peter",
        "familyName": "Slaughter"
    },
    "maintainer": "http://orcid.org/0000-0003-0077-4738"
}
```

JSON-LD operations can later *expand* this reference and *embed* the full
information at both locations.

This means the previous example is equivalent to:


```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "author": {
        "@id": "http://orcid.org/0000-0003-0077-4738",
        "@type": "Person",
        "email": "slaughter@nceas.ucsb.edu",
        "givenName": "Peter",
        "familyName": "Slaughter"
    },
    "maintainer": {
        "@id": "http://orcid.org/0000-0003-0077-4738",
        "@type": "Person",
        "email": "slaughter@nceas.ucsb.edu",
        "givenName": "Peter",
        "familyName": "Slaughter"
    }
}
```

#### Nesting objects

The following SoftwareSourceCode object is an example of a simple root
object:

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR"
}
```

A root object can refer to other objects. For example, it may recommend a
SoftwareApplication:

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "softwareSuggestions": {
        "@type": "SoftwareApplication",
        "name": "rmarkdown"
    }
}
```

Nesting can go many layers deep. In this example, to add attributes to this
application:

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "softwareSuggestions": {
        "@type": "SoftwareApplication",
        "name": "rmarkdown",
        "provider": {
            "@type": "Organization",
            "name": "Central R Archive Network (CRAN)",
            "url": "https://cran.r-project.org"
        }
    }
}
```

Indentation and matching braces are important. These reflect the hierarchy of
the document.

Each object begins with a `{` and ends with a matching `}`. Each object should
also have a depth of indentation (the spaces at the beginning of a line) that
reflects its place in the hierarchy.

This above example defines "Central R Archive Network (CRAN)" as the name of
the provider of "rmarkdown", which is a softwareSuggestions of CodemetaR.

Putting key-value or property-value pairs in a different place in the document
hierarchy can change the meaning of the document.

The code below has the `"url"` pair at a different hierarchy. The result is
that it no longer belongs with the `"provider"` information, and the meaning
of the document has changed. It is *_not_* equivalent to the code above.

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "softwareSuggestions": {
        "@type": "SoftwareApplication",
        "name": "rmarkdown",
        "provider": {
            "@type": "Organization",
            "name": "Central R Archive Network (CRAN)"
        },
        "url": "https://cran.r-project.org"
    }
}
```

The change in hierarchy means that `"https://cran.r-project.org"` is
represented as the `"url"` of `rmarkdown`, instead of being the url of
`Central R Archive Network (CRAN)`.

### Example of a CodeMeta file

The following is an example of a basic `codemeta.json` that can be put at the
root of a code repository:

```json
{
    "@context": "https://w3id.org/codemeta/3.1",
    "type": "SoftwareSourceCode",
    "applicationCategory": "Biology",
    "codeRepository": "https://github.com/gem-pasteur/macsyfinder",
    "description": "MacSyFinder is a program to model and detect macromolecular systems, genetic pathways… in prokaryotes protein datasets.",
    "downloadUrl": "https://pypi.org/project/MacSyFinder/",
    "license": "https://spdx.org/licenses/GPL-3.0+",
    "name": "macsyfinder",
    "version": "2.1.4",
    "continuousIntegration": "https://github.com/gem-pasteur/macsyfinder/actions",
    "developmentStatus": "active",
    "issueTracker": "https://github.com/gem-pasteur/macsyfinder/issues",
    "referencePublication": "https://doi.org/10.24072/pcjournal.250"
}
```

([Link to full example](https://github.com/gem-pasteur/macsyfinder/blob/master/codemeta.json)).

## The context

Every CodeMeta document must refer to the context file *codemeta.jsonld*, for
example via a URL. This indicates that all terms in the document should be
interpreted in the "context" of CodeMeta.

Most terms are chosen to match the equivalent terms in <http://schema.org>,
but CodeMeta provides a few additional terms not found in <http://schema.org>
which may be helpful for software projects.

CodeMeta also restricts the context to use only those <https://schema.org>
terms that are explicitly listed on the [terms](/terms/) page. Users wanting
to include additional terms may:

* Use the `schema:` prefix to define them as <http://schema.org> terms, (such
as `"schema:releaseNotes"` [in this example](https://github.com/SciCodes/somef-core/blob/f0481b6f28166e1c5a95919d2767f1aaa5b3fa87/codemeta.json#L85)), or
* Extend the context (see [the developer guide](/developer-guide/)).

The context file may be modified and updated in the future, if new JSON
properties are added or existing ones modified.

The CodeMeta GitHub repository defines tags to allow specific versions of a
file to be referenced, and assigns *digital object identifiers*, or DOIs, to
each release tag. Please use the
[appropriate release](https://github.com/codemeta/codemeta/releases) of the
CodeMeta schema in order to refer to the appropriate context file, e.g.

```json
"@context": "https://w3id.org/codemeta/3.1"
```

## Referencing CodeMeta

Release candidate versions may be referred to consistently using their
[git tag](https://github.com/codemeta/codemeta/tags) for the raw version, e.g.
<https://raw.githubusercontent.com/codemeta/codemeta/2.0-rc/codemeta.jsonld>.
*Please do not refer to the raw GitHub URL for the master branch*, as this is
/subject to change and will not guarantee a stable metadata file.

