from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command
logger = get_task_logger(__name__)

@shared_task
def get_currencies_task():
    from .script import fuel_in_database, currencies_in_database
    result = currencies_in_database()

    return f"finished task with result: {result}"

@shared_task
def get_gold_task():
    from .script import gold_in_database
    result = gold_in_database() 

    return f"finished task with result: {result}"


@shared_task
def get_fuel_task():
    from .script import fuel_in_database
    result = fuel_in_database()
    return f"finished task with result: {result}"

@shared_task
def get_foreign_currency_task():
    from .script import foreign_currency_in_database
    result = foreign_currency_in_database()
    return f"finished task with result: {result}"






