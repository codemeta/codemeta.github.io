---
title: "The Codemeta JSON-LD Representation"
---

## The JSON-LD Context File

CodeMeta properties can be serialized in JSON-LD by referencing the context file: `"@context": "https://doi.org/10.5063/SCHEMA/CODEMETA-1.0"`.
CodeMeta properties are built on and extend software properties from <https://schema.org>.  A list of all properties provided by the current CodeMeta `context` file can be found on the [terms](/terms) page.

Aside from the use of `@context`, codemeta JSON-LD looks like any other json metadata record, and can be easily written by hand.  Here's an example which provides some metadata for the [codemetar](https://github.com/codemeta/codemetar) R package.  Note that additional metadata may be added as indicated in [terms](/terms).

```{json}
{
  "@context": "https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld",
  "@type": "SoftwareSourceCode",
  "identifier": "codemetar",
  "title": "Generate CodeMeta Metadata for R Packages",
  "description": "Codemeta defines a 'JSON-LD' format for describing software metadata.\n    This package provides utilities to generate, parse, and modify codemeta.jsonld\n    files automatically for R packages.",
  "name": "codemetar",
  "codeRepository": "https://github.com/codemeta/codemetar",
  "issueTracker": "https://github.com/codemeta/codemetar/issues",
  "licenseId": "MIT + file LICENSE",
  "version": "0.1.0",
  "programmingLanguage": {
    "@type": "ComputerLanguage",
    "name": "R",
    "version": "3.4.0",
    "url": "https://r-project.org"
  },
  "runtimePlatform": "R version 3.4.0 (2017-04-21)",
  "author": [
    {
      "@type": "Person",
      "givenName": "Carl",
      "familyName": "Boettiger",
      "email": "cboettig@gmail.com",
      "@id": "http://orcid.org/0000-0002-1642-628X"
    }
  ],
  "copyrightHolder": "http://orcid.org/0000-0002-1642-628X"
  "depends": [
    {
      "@type": "SoftwareApplication",
      "name": "jsonlite",
      "version": "1.3",
      "provider": {
        "@id": "https://cran.r-project.org",
        "@type": "Organization",
        "name": "Central R Archive Network (CRAN)",
        "url": "https://cran.r-project.org"
      }
    }
  ],
  "contIntegration": "https://travis-ci.org/codemeta/codemetar",
  "developmentStatus": "Project Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public"
}
```
