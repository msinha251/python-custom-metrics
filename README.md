# python-custom-metrics
This repo contains code sample for tracing custom metrics for prometheus using prometheus-client and python flask app that exposed custom defined metrics on metrics endpoint. For quick local setup docker-compose is available.

Docker-compose contains:
* prometheus
* grafana
* python-app
* grafana-dashboard

Command:
###build python app
`docker-compose build python-app`

###runn all containers
`docker-compose up`

###stop containers
`docker-compose down`

###running containers
`docker-compose ps` 