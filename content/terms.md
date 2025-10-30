---
title: CodeMeta Terms
---

## Terms from Schema.org

### Schema.org Software terms

Recognized properties for CodeMeta `SoftwareSourceCode` and `SoftwareApplication` includes the following terms from <https://schema.org>.  These terms are part of the CodeMeta specification and can be used without any prefix.

{{% properties-description matchParentType="schema:(SoftwareSourceCode|SoftwareApplication|CreativeWork|Thing)"%}}

These terms are all recognized properties of <https://schema.org/SoftwareSourceCode> or <https://schema.org/SoftwareApplication> Types.

Note that while most properties take basic data types as values (`Text`, `URL`), several take other node types, such as `Person`, `Organization`, `Review`, or `Role`.
Recommended fields for these node types in CodeMeta documents are given below.

### Schema.org Thing terms

{{% properties-description matchParentType="schema:(Thing)"%}}

### Schema.org Person terms

{{% properties-description matchParentType="schema:(Person)"%}}

### Schema.org Review terms

{{% properties-description matchParentType="schema:(Review)"%}}

### Schema.org Role terms

{{% properties-description matchParentType="schema:(Role)"%}}

## CodeMeta terms

The CodeMeta project also introduces the following additional properties, which lack clear equivalents in <https://schema.org> but can play an important role in software metadata records covered by the CodeMeta crosswalk.

{{% properties-description matchParentType="codemeta:"%}}

Please suggest additional terms or adjustments to this representation in the [CodeMeta issues](https://github.com/codemeta/codemeta/issues).
