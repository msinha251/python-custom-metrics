import logging
from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge, Info
import time
import requests
import logging
import databricks_metrics

logger = logging.basicConfig(level=logging.INFO)

#TODO var's from config or env

app = Flask(__name__)

_INF = float("inf")

graphs = {}
# graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
# graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))
# graphs['i'] = Info('python_requests_type', 'Description of info')

graphs['cd_status'] = Gauge('cd_last_status_boolean', 'Gauge for the cd last status.')
graphs['ghe_status'] = Gauge('ghe_status_boolean', 'Gauge for ghe status.')
# graphs['i'] = Info('python_requests_type', 'Success (1) / Failed (0)')
graphs['c1'] = Counter('python_request_success_total', 'The total number of success requests')
graphs['c0'] = Counter('python_request_failed_total', 'The total number of failed requests')


@app.route("/<code>")
def prometheus_metrics(code):
    #ghe_status
    try:
        r = requests.get(ghe_url)
        if r.status_code == 200:
            logger.info("GHE is UP")
            graphs['ghe_status'].set(1)
        else:
            logger.info("GHE is DOWN")
            graphs['ghe_status'].set(0)
    except:
        graphs['ghe_status'].set(0)
        
    #cd_status
    if code == '200':
        graphs['c1'].inc()
        # graphs['i'].info({'success': '1'})
        graphs['cd_status'].set(1)
        return Response("Success", status=code, mimetype='text/plain')
    else:
        graphs['c0'].inc()
        # graphs['i'].info({'failed': '0'})
        graphs['cd_status'].set(0)
        return Response("Unknown Code", status=code , mimetype='text/plain')
    # start = time.time()


@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")
