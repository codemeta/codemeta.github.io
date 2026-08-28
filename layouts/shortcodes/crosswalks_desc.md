{{ $crosswalkName := .Params.name }}
{{ $result := where .Site.Data.crosswalk_pages "stem" $crosswalkName }}
{{ if gt (len $result) 0 -}}
  {{ range $result }}
  {{ .desc }}
  {{ end }}
{{ else }}
Properties of the {{ $crosswalkName }} vocabulary.  
{{ end }}
