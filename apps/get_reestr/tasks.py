from celery.schedules import crontab

from core.celery import app

from .models import CsvFile
from .services import Service
from .utils import get_date_from_html


@app.task()
def check_phone_list_reestr():
    url = 'https://opendata.fssp.gov.ru/7709576929-phonelist'

    date = get_date_from_html(url)

    service = Service()

    try:
        csv_file = CsvFile.objects.get(name=CsvFile.FileNameChoices.PHONE_LIST)

        if date.date() > csv_file.updated:
            service.get_phone_list_csv(date)

    except CsvFile.DoesNotExist:
        service.get_phone_list_csv(date)


@app.task()
def check_osp_list_reestr():
    url = 'https://opendata.fssp.gov.ru/7709576929-osp'

    date = get_date_from_html(url)

    service = Service()

    try:
        csv_file = CsvFile.objects.get(name=CsvFile.FileNameChoices.PHONE_LIST)

        if date.date() > csv_file.updated:
            service.get_osp_list_csv(date)

    except CsvFile.DoesNotExist:
        service.get_osp_list_csv(date)


@app.task()
def check_tolist_reestr():
    url = 'https://opendata.fssp.gov.ru/7709576929-tolist/'

    date = get_date_from_html(url)

    service = Service()

    try:
        csv_file = CsvFile.objects.get(name=CsvFile.FileNameChoices.PHONE_LIST)

        if date.date() > csv_file.updated:
            service.get_tolist_csv(date)

    except CsvFile.DoesNotExist:
        service.get_tolist_csv(date)


app.conf.beat_schedule = {
    'check_phone_list_reestr': {
        'task': 'check_phone_list_reestr',
        'schedule': crontab(minute=0, hour=12)
    },
    'check_osp_list_reestr': {
            'task': 'check_osp_list_reestr',
            'schedule': crontab(minute=0, hour=13)
        },
    'check_tolist_reestr': {
            'task': 'check_tolist_reestr',
            'schedule': crontab(minute=0, hour=14)
        },
}

