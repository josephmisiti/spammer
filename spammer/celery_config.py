import djcelery
from datetime import timedelta
from celery.schedules import crontab
djcelery.setup_loader()

CELERY_ROUTES = {
    "email_queue": {
        "queue": "email_queue",
        "binding_key": "email_queue"
    },
}

CELERY_QUEUES = {
    "email_queue": {
        "exchange": "email_queue",
        "exchange_type": "direct",
        "binding_key": "email_queue",
    },
}

CELERY_DEFAULT_QUEUE = "email_queue"
BROKER_BACKEND = "redis"
BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_REDIS_HOST = "127.0.0.1"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

##########
# RESULTS
##########
CELERY_RESULT_BACKEND = 'redis://localhost:6379/7'
CELERY_TASK_RESULT_EXPIRES =  60*60*24 

CELERY_IMPORTS = (
	"apps.collector.tasks",
)

CELERYD_CONCURRENCY         = 1
#CELERY_IGNORE_RESULT        = True
CELERY_ACKS_LATE            = True # Retry if task fails
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_TASK_TIME_LIMIT     = 60 * 15 # in seconds, so 15 minutes
CELERY_DISABLE_RATE_LIMITS  = True
CELERY_SEND_TASK_ERROR_EMAILS = True


# CELERYBEAT_SCHEDULE = {
#     'refresh_google_alerts': {
#         'task':     'refresh_google_alerts',
#         "schedule"    : timedelta(seconds=60*60*24),
#         'options'    : {'queue': 'beat_tasks' },
#     },
# }