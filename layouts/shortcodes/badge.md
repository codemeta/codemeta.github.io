{{ $supported := .Site.Params.supported }}{{ $latest := $supported | sort | collections.Reverse }}{{ $latest := index $latest 0 }}
[![Permanent Identifier](https://img.shields.io/badge/perma--id-https%3A%2F%2Fw3id.org%2Fcodemeta%2F{{ substr $latest 0 3 }}-blue.svg)](https://w3id.org/codemeta/{{ substr $latest 0 3 }})
