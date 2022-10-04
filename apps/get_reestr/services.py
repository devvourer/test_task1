from django.conf import settings
from django.utils import timezone

from .models import CsvFile, PhoneList, Osp, ToList

import requests
import csv


class Service:
    base_url = 'https://opendata.fssp.gov.ru'
    phone_list = '/7709576929-phonelist'
    osp = '/7709576929-osp'
    tolist = '/7709576929-tolist/'

    @staticmethod
    def get_content(response: requests.Response) -> str:
        """ Метод возвращает отформатированные данные в виде текста"""
        content = str(response.content.decode('utf-8'))[2: -1]
        return content.replace('\\t', ',').replace('\\n', '\n')

    @staticmethod
    def write_from_phone_list_csv(file: CsvFile) -> None:
        """ Запись данных PhoneList в бд с файла csv """
        with open(file.file.path) as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count:
                    _, created = PhoneList.objects.get_or_create(
                        region=row[0],
                        agency_name=row[2],
                        name=row[3],
                        number_type=row[4],
                        number=row[5],
                    )

                count += 1

    @staticmethod
    def write_from_osp_list_csv(file: CsvFile) -> None:
        """ Запись данных Osp в бд с файла csv """

        with open(file.file.path) as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count:
                    _, created = Osp.objects.get_or_create(
                        region=row[0],
                        code_territorial_agency=row[1],
                        name_territorial_agency=row[2],
                        postal_address=row[3],
                        chiefs_full_name=row[4],
                        telephone_number=row[5],
                        fax=row[6],
                        phone_help_service=row[7],
                        phone_help_service2=row[8],
                        working_hours=row[9],
                        territory_of_service=row[10],
                    )
                count += 1

    @staticmethod
    def write_from_tolist_csv(file: CsvFile) -> None:
        """ Запись данных ToList в бд с файла csv """
        with open(file.file.path) as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count:
                    _, created = ToList.objects.get_or_create(
                        name_territorial_agency=row[0],
                        abbreviated_name_territorial_agency=row[1],
                        full_name=row[2],
                        post=row[3],
                        description=row[4],
                        postal_address=row[5],
                        working_hours=row[6],
                        oktmo=row[7],
                        okato=row[8],
                        okpo=row[9],
                        ogrn=row[10],
                        tin=row[11],
                        faq_number=row[12],
                        tel_number_others=row[13],
                        fax=row[14],
                        url=row[15],
                        email=row[16],
                    )
                count += 1

    def get_phone_list_csv(self, date: str) -> None:
        """ Метод стягивает файл phone_list с сайта и записывает в бд"""
        date = date.replace('-', '')
        url = f'{self.base_url}{self.phone_list}/data-{date}-structure-20150209.csv'

        response = requests.get(url)
        content = self.get_content(response)
        date = timezone.now().strftime('%y-%m-%d')

        file_path = str(settings.BASE_DIR) + f'/reestrs/phone_list_{date}.csv'
        with open(file_path, 'w+') as file:
            file.write(content)

            obj, created = CsvFile.objects.get_or_create(name=CsvFile.FileNameChoices.PHONE_LIST)
            obj.file = file_path
            obj.save()

            self.write_from_phone_list_csv(obj)

    def get_osp_list_csv(self, date: str) -> None:
        """ Метод стягивает файл osp с сайта и записывает в бд"""

        date = date.replace('-', '')
        url = f'{self.base_url}{self.osp}/data-{date}-structure-20160226.csv'
        response = requests.get(url)
        content = self.get_content(response)
        date = timezone.now().strftime('%y-%m-%d')

        file_path = str(settings.BASE_DIR) + f'/reestrs/osp_{date}.csv'
        with open(file_path, 'w+') as file:

            file.write(content)
            obj, created = CsvFile.objects.get_or_create(name=CsvFile.FileNameChoices.OSP)
            obj.file = file_path
            obj.save()

            self.write_from_osp_list_csv(obj)

    def get_tolist_csv(self, date: str) -> None:
        """ Метод стягивает файл tolist с сайта и записывает в бд"""

        date = date.replace('-', '')
        url = f'{self.base_url}{self.tolist}/data-{date}-structure-20160729.csv'
        response = requests.get(url)
        content = self.get_content(response)
        date = timezone.now().strftime('%y-%m-%d')

        file_path = str(settings.BASE_DIR) + f'/reestrs/tolist_{date}.csv'
        with open(file_path, 'w+') as file:

            file.write(content)

            obj, created = CsvFile.objects.get_or_create(name=CsvFile.FileNameChoices.TO_LIST)
            obj.file = file_path
            obj.save()

            self.write_from_tolist_csv(obj)

