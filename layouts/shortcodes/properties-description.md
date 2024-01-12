{{ $matchParentType := .Params.matchParentType }}

<table class="table table-striped">
<thead>
<tr>
<th>
Property
</th>
<th>
Type
</th>
<th title="What Codemeta versions support this property">
Versions
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
{{ range $property := .Site.Data.properties_description }}
{{ $parentType := index $property "Parent Type" }}
{{ if findRE $matchParentType $parentType }}
<tr>
<td>
{{ index $property "Property" }}
</td>
<td>
{{ index $property "Type" }}
</td>
<td>
{{ replaceRE "(\\.0)*" "" (delimit (sort (index $property "versions")) ", ") }}
</td>
<td>
{{ index $property "Description" }}
</td>
</tr>
{{ end }}
{{ end }}
</tbody>
</table>
