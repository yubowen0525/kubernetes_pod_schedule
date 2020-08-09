from Project import creat_app
from Project.extension import db
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

app = creat_app('testing')
metrics = GunicornPrometheusMetrics(app)

if __name__ == '__main__':
    # start_http_server(8000)
    # app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    #     '/metrics': make_wsgi_app()
    # })
    app.run(host="0.0.0.0", port="8080")