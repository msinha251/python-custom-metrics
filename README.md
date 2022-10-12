# ml-platform-app-metrics
This repo build docker image for `platform-app-metrics` which contains code sample for tracing custom metrics for prometheus using prometheus-client and python flask app that exposed custom defined metrics on metrics endpoint. For quick local setup docker-compose is available and for K8S, helm template is available.


<details>
<summary> docker-compose Commands </summary>
<hr>

Docker-compose contains:
* prometheus
* grafana
* python-app
* grafana-dashboard

## Commands:
#### build python app<br>
`docker-compose build python-app`<br>

#### run all containers<br>
`docker-compose up`<br>

#### stop containers
`docker-compose down`<br>

#### running containers<br>
`docker-compose ps` 

</hr>
</details>


<details>
<summary>Steps for prometheus service monitor</summary>
<hr>

 #### Step 1: Get the details (NAMESPACE, NAME) for existing running prometheus stack:
 `kubectl get prometheus -A`

 #### Step 2: Get the labels needed for ServiceMonitor:
 `kubectl get prometheus -n <NAMESPACE> <NAME> -o=jsonpath='{.spec.serviceMonitorSelector}'`

 Output:
 `{"matchLabels":{"release":"kube-prometheus-stack"}}`

 #### Step 3: Make sure the metrics endpoint service is running. 

 #### Step 4: Create service monitor:
  * Update the namespace under metadata from Step 1 output.
  * Add the prometheus labels from above command output (release:kube-prometheus-stack) under metadata > labels
  * Update endpoints path (if different than metrics)
  * Update the custom metrics service namespace under namespaceSelector.matchNames  

 Sample service monitor template:
```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    release: kube-prometheus-stack
  name: ml-platform-app
  namespace: monitoring
spec:
  endpoints:
  - path: /metrics
    port: metrics
    interval: 60s
  namespaceSelector:
    matchNames:
    - databricks-cd
  selector:
    matchLabels:
      run: ml-platform-app
 ```

</hr>
</details>