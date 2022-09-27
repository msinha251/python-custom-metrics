# python-custom-metrics
This repo contains code sample for tracing custom metrics for prometheus using prometheus-client and python flask app that exposed custom defined metrics on metrics endpoint. For quick local setup docker-compose is available.

Docker-compose contains:
* prometheus
* grafana
* python-app
* grafana-dashboard

Commands:<br>
### build python app<br>
`docker-compose build python-app`<br>

### run all containers<br>
`docker-compose up`<br>

### stop containers
`docker-compose down`<br>

### running containers<br>
`docker-compose ps` 