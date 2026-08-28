{{ $supported := .Site.Params.supported }}

{{ $tools := .Site.Data.tools }}



<table class="table table-striped">
  <tr>
    <th>Tool name</th>
    <th>Language</th>
    <th>Category</th>
    <th>Maintainers</th>
    <th>Versions</th>
    <th>Description</th>
  </tr>
  {{ range sort $tools "name" "asc" }}
  {{ $latest := .versions | collections.Reverse }}
  {{ if in $supported (index $latest 0 ) | not }}
  <tr>
    <td><a href="{{ .url }}">{{ .name }}</a></td>
    <td>{{ .language }}</td>
    <td>{{ $icnt := sub (.categories | len) 1 }} {{ range $i, $cat := .categories }}<a href="#{{ $cat | urlize }}">{{ $cat }}</a>{{ if lt $i $icnt }},{{end}}<br>{{ end -}}</td>
    <td>{{ $icnt := sub (.maintainers | len) 1 }}{{- range $i, $mtnrs := .maintainers }}{{ $mtnr := index $mtnrs }}{{ if $mtnr.url }}<a href="{{ $mtnr.url }}">{{ $mtnr.name }}</a>{{ else }}{{ $mtnr.name }}{{ end }}{{ if lt $i $icnt }},{{end}}<br>{{ end -}}</td>
    <td>{{ delimit .versions ", " }}</td>
    <td>{{ .description }}</td>
  </tr>
    {{ end -}}
    {{ end }}
  </table>
