from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from prometheus_flask_exporter import RESTfulPrometheusMetrics


db = SQLAlchemy()
api = Api(prefix='/api')
metrics = RESTfulPrometheusMetrics.for_app_factory()
