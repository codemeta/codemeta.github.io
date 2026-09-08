{{ $crosswalkName := .Params.name }}

<table class="table table-striped">
<thead>
<tr>
<th style="text-align:left;">
Property
</th>
<th style="text-align:left;">
{{ $crosswalkName }}
</th>
</tr>
</thead>
<tbody>
{{- range $property := .Site.Data.crosswalk }}
{{- if index $property $crosswalkName }}
<tr>
<td style="text-align:left;">
{{ $property.Property }}
</td>
<td style="text-align:left;">
{{ index $property $crosswalkName }}
</td>
</tr>
{{- end -}}
{{ end }}
</tbody>
</table>

New to CodeMeta? The [User Guide](/user-guide) describes how these terms are used in a
`codemeta.json` file. There are also [various tools](/tools) such as
[the generator](/create) that can help!
{.tip}
