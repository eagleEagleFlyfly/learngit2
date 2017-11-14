from celery.schedules import crontab
from celery import Celery
from datetime import timedelta

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='rpc://')

app.conf.update(
# 定时配置要放在这里，f**k...
    CELERYBEAT_SCHEDULE={
        'perminute': {
            'task': 'tasks.add',
            # 'schedule': crontab(minute='*/1'),
            'schedule': timedelta(seconds=5),
            'args': (1, 2)
        }
    }
)