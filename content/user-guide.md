---
title: user guide

---

## Generating a CodeMeta file

You can use the [codemeta-generator](https://codemeta.github.io/codemeta-generator/) directly at <https://codemeta.github.io/codemeta-generator/>

## Creating A CodeMeta Instance File Manually

A CodeMeta instance file describes the metadata associated with a software object using JSON's linked data (JSON-LD) notation.  A codemeta file can contain any of the properties described on the [CodeMeta terms page](/terms/). Most codemeta files are called `codemeta.json` by convention.

Here is an example of a basic `codemeta.json` that you can put at the root of a Github repo ([link to full example](https://github.com/ropensci/codemetar/blob/master/codemeta.json)):
```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",
    "description": "Codemeta defines a 'JSON-LD' format for describing software metadata. This package provides utilities to generate, parse, and modify codemeta.jsonld files automatically for R packages.",
    "license": "https://spdx.org/licenses/GPL-3.0",
    "identifier": "http://dx.doi.org/10.5281/zenodo.XXXX"
}
```

### Basics

When creating a CodeMeta document, note that they contain JSON name ("property" in linked-data), value pairs where the values can be simple values, arrays or JSON objects. A simple value is a number, string, or one the literal values *false*, *null* *true*, for example:

```
"name" : "R Interface to the DataONE REST API"
```

There must be a comma between of these key-value pairs, and no comma at the end before the closing bracket (`}`).

### Arrays

A JSON array is surrounded by the characters `[` and `]`, and can contain multiple values separated by commas:

```
"keywords": [ "data sharing", "data repository", "DataONE" ]
```

As with any JSON documents, you can add line breaks between values for improved quality. For example, the former key-value pair is this is equivalent to:

```
"keywords": [
    "data sharing",
    "data repository",
    "DataONE"
]
```

All fields that accept a value of a given type accept an array of values of this type, and vice-versa. For example, a software with two licenses could have this attribute:

```
"license": [
    "https://spdx.org/licenses/GPL-3.0",
    "https://spdx.org/licenses/BSD-3-Clause"
]
```

### Objects

Some properties, such as `author`, can refer to other JSON objects surrounded by curly braces and can contain other JSON values or objects, for example:

```
"author": {
    "@id": "http://orcid.org/0000-0003-0077-4738",
    "@type": "Person",
    "email": "slaughter@nceas.ucsb.edu",
    "givenName": "Peter",
    "familyName": "Slaughter"
}
```

The JSON-LD "@type" keyword associates a JSON value or object with a well known type, for example, the
statement `"@type":"Person"` associates the `author` object with `http://schema.org/Person`.  
It is good practice to always provide the `@type` for any property which specifies a node (JSON object).
The [terms page](/terms/) indicates these node types.

The "author" JSON object illustrates the use of the JSON-LD keyword "@id", which is used to associate an IRI with the JSON object.  Any such node object can be assigned an `@id`, and we may use the `@id` to refer to this same object (the person, Peter), elsewhere in the document; e.g. we can indicate the same individual is also the `maintainer` by adding:

```
"maintainer": "http://orcid.org/0000-0003-0077-4738"
```

This should be added at the top level of the document, indicating that this individual is the `maintainer` of the software being described, like this:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
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

JSON-LD operations can later *expand* this reference and *embed* the full information at both locations. This means the example above is equivalent to:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
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


### Nesting objects

We saw before a simple (root) SoftwareSourceCode object:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR"
}
```

and this root object can refer to other objects, for example recommend a SoftwareApplication:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
    "@type": "SoftwareSourceCode",
    "name": "CodemetaR",

    "softwareSuggestions": {
        "@type": "SoftwareApplication",
        "name": "rmarkdown"
    }
}
```

And you may in turn want to add attributes to this application:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
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

It is important to mind the order of curly brackets (an object begins with a `{` and ends with a matching `}`) and indentation (spaces at the beginning of a line) to reflect the hierarchy: "Central R Archive Network (CRAN)" is the name of the provider of "rmarkdown", which is a softwareSuggestion of CodemetaR.

For example, the above code is not equivalent to:

```json
{
    "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
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

because in the latter, `"https://cran.r-project.org"` is the `"url"` of `rmarkdown`, instead of being the url of `Central R Archive Network (CRAN)`.

## The context

Every CodeMeta document must refer to the context file *codemeta.jsonld*, for example via a URL.  This indicates that all terms in the document should be interpreted in the "context" of CodeMeta.  Most terms are chosen to match the equivalent terms in <http://schema.org>, but CodeMeta provides a few additional terms not found in <http://schema.org> which may be helpful for software projects.  CodeMeta also restricts the context to use only those <https://schema.org> terms that are explicitly listed on ther [terms](/terms/) page.  Users wanting to include additional terms must extend the context (see [developer-guide](/developer-guide/)).  


The context file may be modified and updated in the future, if new JSON properties are added or existing ones modified.
The CodeMeta GitHub repository defines tags to allow specific versions of a file to be referenced, and assigns 
*digital object identifiers*, or DOIs, to each release tag. Please use the [appropriate release](https://github.com/codemeta/codemeta/releases) of the CodeMeta schema in order to refer to the
appropriate context file, e.g.


```
"@context": "https://doi.org/10.5063/schema/codemeta-2.0"
```

Release candidate versions may be referred to consistently using their git tag for the raw version, e.g. <https://raw.githubusercontent.com/codemeta/codemeta/2.0-rc/codemeta.jsonld>.  *Please do not refer to the raw GitHub URL for the master branch*, as this is subject to change and will not guarantee a stable metadata file.  



## Testing An Instance file

Our [codemeta-generator](https://codemeta.github.io/codemeta-generator/) can also check a codemeta.json file you wrote is valid. To do that, copy-paste your code in the bottom box, and click "Validate codemeta.json".
