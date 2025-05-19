{{- define "weather-app.name" -}}
weather-app
{{- end -}}

{{- define "weather-app.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}