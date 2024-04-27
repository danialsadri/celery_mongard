from kombu import Queue, Exchange

default_exchange = Exchange(name='default', type='direct')
media_exchange = Exchange(name='media', type='direct')

task_queues = (
    Queue(name='default', exchange=default_exchange, routing_key='default'),
    Queue(name='image', exchange=media_exchange, routing_key='image'),
    Queue(name='video', exchange=media_exchange, routing_key='video'),
)

task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'

task_routes = {
    'main.add': {'queue': 'default'},
    'main.add_bind': {'queue': 'image'},
    'main.division_bind': {'queue': 'video'},
}
