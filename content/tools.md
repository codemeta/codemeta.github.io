---
title: Tools
layout: sidenav
---

This page lists some existing tools to help with CodeMeta files. They range from scripts to services, and can help you create, convert, validate, and visualize CodeMeta data.

The list is not exhaustive. You are invited to submit new tools, or update the listings for existing tools! This can be done in [this website's repository](https://github.com/codemeta/codemeta.github.io?tab=contributing-ov-file#updating-the-tools-page)

## Choosing Tools

These tools do not need anything except your browser. They provide a helpful form for you to fill out, and allow you to see and refine the output, while ensuring it is valid.

The [CodeMeta Generator](/create) is the reference generator implementation, and is best used for simple projects.

### Use Existing Data

The tools in the table of [Converters](#converters) can migrate data to and from various other formats. If you already have the necessary information in a `citation.cff`, a package manifest, or even your Git repository's API, you can easily adapt it to CodeMeta.

### A Tool for Your Stack

Our [table of libraries](#libraries) table lists tools packaged for specitic languages or environments, while [Generation Utilities](#generation-utilities) can be integrated into many pipelines.

### Keep in Sync

If you need to automate your metadata publishing, you can also find [Publishing Pipelines](#publishing-pipelines). These can work with your existing deployment or CI/CD workflows, and can help you keep your metadata in sync across multiple locations.

## Tools for Supported Versions

The tables in this section contain tools for supported versions of CodeMeta.

Note: Tools marked with a warning symbol ( ⚠️ ) are not known to support the *latest version* of CodeMeta.
{.tip}

These tools are categorised according to the context they can be used. In many cases a tool belongs to multiple categories and will be listed multiple times on this page.

{{% tools %}}


## Tools for Unsupported Versions

These tools have not been verified to work on supported versions of CodeMeta. They may not work as expected, if at all.

While out of date, these tools may provide a good starting point for a new tool, instead of starting from scratch.


{{% unsupported-tools %}}


Pending:

- DataCite
- Figshare
- JOSS
- Zenodo
