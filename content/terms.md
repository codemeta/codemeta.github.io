---
title: Codemeta Terms

---


## Terms from Schema.org

Recognized properties for CodeMeta `Code` includes the following terms from <https://schema.org>:

{{% schematable  "https://raw.githubusercontent.com/codemeta/codemeta/master/data/schematerms.csv" %}}


These terms are all recognized properties of <https://schema.org/SoftwareSourceCode> or <https://schema.org/SoftwareApplication> Types. Note that while most properties take basic data types as values (`Text`, `URL`), several take other node types, such as `Person` or `Organization`.  Recommended fields for these node types in CodeMeta documents are given below.

## Codemeta terms

The CodeMeta project also introduces the following additional properties, which lack clear equivalents in <https://schema.org> but can play an important role in software metadata records covered by the CodeMeta crosswalk.


{{% schematable  "https://raw.githubusercontent.com/codemeta/codemeta/master/data/codemetaterms.csv" %}}


## Additional node types

### Person or Organization

{{% schematable  "https://raw.githubusercontent.com/codemeta/codemeta/master/data/person.csv" %}}



Please suggest additional terms or adjustments to this representation in the [codmeta issues](https://github.com/codemeta/codemeta/issues)