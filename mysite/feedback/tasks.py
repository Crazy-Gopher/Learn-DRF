from celery.decorators import task
from celery.utils.log import get_task_logger

from feedback.emails import send_feedback_email

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import datetime

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="test_celery_beat",
    ignore_result=True
)
def test_celery_beat():
    logger.info("Current Time: " + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))