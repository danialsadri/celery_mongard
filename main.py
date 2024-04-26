from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

app = Celery(main='main', broker='amqp://guest:guest@localhost:5672/', backend='rpc://')
logger = get_task_logger(__name__)

app.conf.update(
    task_time_limit=60,
    task_soft_time_limit=30,
    worker_concurrency=4,
    worker_prefetch_multiplier=1,
    task_ignore_result=True,
    task_always_eager=False,
    task_acks_late=False,
)


@app.task(name='main.add')
def add(x, y):
    sleep(5)
    return x + y


@app.task(name='main.add_bind', bind=True)
def add_bind(self, x, y):
    print(self.request)
    return x + y


@app.task(name='main.division_bind', bind=True, default_retry_delay=60 * 30)
def division_bind(self, x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logger.info('sorry...')
        self.retry(countdown=10, max_retries=2)
