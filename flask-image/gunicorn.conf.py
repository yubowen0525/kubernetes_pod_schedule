from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
import gevent.monkey
gevent.monkey.patch_all()
keepalive = 1
workers = 4  # 工作进程数
worker_class = 'gunicorn.workers.ggevent.GeventWorker'  # 异步方式
x_forwarded_for_header = 'X-FORWARDED-FOR'
bind = "0.0.0.0:8080"  # 监听端口号
worker_connections = 8048
graceful_timeout = 10
limit_request_line = 8048
backlog = 8048
pidfile = 'debug.log'
chire='./'
daemon = True
debug = False
accesslog = "./gunicorn-logs"



def when_ready(server):
    GunicornPrometheusMetrics.start_http_server_when_ready(8090)


def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
