{{ $supported := .Site.Params.supported }}

{{ $latest := $supported | sort | collections.Reverse }}
{{ $latest := index $latest 0 }}

{{ $tools := .Site.Data.tools }}
{{ range $cats := .Site.Data.tool_categories }}
{{ $cat := index $cats }}

### {{ $cat.name }}

{{ $cat.desc }}

<table class="table table-striped">
  <tr>
    <th>Tool name</th>
    <th>Language</th>
    <th>Maintainers</th>
    <th>Versions</th>
    <th>Description</th>
  </tr>
  {{ range $tools }}
    {{ if in $supported (index .versions 0 ) }}
      {{- if in .categories $cat.name }}
      
      
  <tr>
    <td><a href="{{ .url }}">{{ .name }}</a></td>
    <td>{{ .language }}</td>
    <td>{{ $icnt := sub (.maintainers | len) 1 }}{{- range $i, $mtnrs := .maintainers }}{{ $mtnr := index $mtnrs }}{{ if $mtnr.url }}<a href="{{ $mtnr.url }}">{{ $mtnr.name }}</a>{{ else }}{{ $mtnr.name }}{{ end }}{{ if lt $i $icnt }},{{end}}<br>{{ end -}}</td>
    <td>{{ if in .versions $latest | not }} ⚠️ {{ end }}
    {{ delimit .versions  ", " }}</td>
    <td>{{ .description }}</td>
  </tr>
    {{ end -}}
    {{ end }}
  {{ end }}
  </table>
{{ end }}

