from .api import Todo, TodoList, initdb
from .api import getversion, getversion_sleep, getversion_sleeps
from ..extension import api

# 一个resource匹配多个route
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(initdb, '/initdb')

api.add_resource(getversion, '/')
api.add_resource(getversion_sleep, '/sleep')
api.add_resource(getversion_sleeps, '/sleep/<int:sleep_seconds>')
