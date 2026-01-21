  <h2 class="ms-3">CodeMeta News</h2>
  <ul id="newslist" class="list-group list-unstyled">

{{ $items := slice }}

{{ range $feed := .Site.Data.feeds }}
{{ $item := index $feed.channel "item" }}
{{ $items = $items | append $item }}
{{ end }}

{{ $combi := slice }}

{{- range $items -}}
{{ $t := time.AsTime .pubDate }}
{{ $m := dict "link" .link "title" .title "pubDate" $t "description" .description }}
{{ $combi = $combi | append $m }}
{{- end -}}

{{ $combi := sort $combi ".pubDate" "desc" }}

{{ range $combi }}
  <li class="ps-2 pb-2">
    <h3><a class="list-group-item newslink p-2" href="{{ .link }}">{{ .title }}</a></h3>
    <small class="ps-2 text-secondary-emphasis">{{ .pubDate | time.Format "Jan 02, 2006 3:04 PM MST"  }}</small>
    <div class="ps-2 pt-2">{{ .description }}</div>
  </li>
{{ end }}
  </ul>
<script src="../js/news.js"></script>
<script>
let urls = {{ .Site.Params.feeds | jsonify | safeJS }}
refreshNewslist(urls);
</script>
