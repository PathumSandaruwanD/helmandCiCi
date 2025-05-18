srilanka-weather-app/
└── helm/
    └── weather-app/              <-- 🧠 This is the Helm chart (can be renamed)
        ├── Chart.yaml            <-- 🧾 Metadata about your chart (name, version, etc.)
        ├── values.yaml           <-- 🧰 Default values for your app (e.g., image, env)
        ├── templates/            <-- 📦 Kubernetes resource definitions (templated)
        │   ├── deployment.yaml   <-- 📄 Defines your app's Deployment
        │   ├── service.yaml      <-- 📄 Exposes your app via ClusterIP/NodePort/Ingress
        │   ├── _helpers.tpl      <-- ⚙️ Optional: functions/macros (used by templates)
        │   └── NOTES.txt         <-- 📋 Instructions shown after `helm install`
