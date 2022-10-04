from django.db import models


class PhoneList(models.Model):

    region = models.PositiveSmallIntegerField()
    agency_name = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    number_type = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Osp(models.Model):
    region = models.PositiveSmallIntegerField()
    code_territorial_agency = models.PositiveSmallIntegerField()
    name_territorial_agency = models.CharField(max_length=200, null=True)
    postal_address = models.CharField(max_length=200, null=True)
    chiefs_full_name = models.CharField(max_length=200, null=True)
    telephone_number = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=100, null=True)
    phone_help_service = models.CharField(max_length=100, null=True)
    phone_help_service2 = models.CharField(max_length=100, null=True)
    working_hours = models.CharField(max_length=500, null=True)
    territory_of_service = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ToList(models.Model):
    name_territorial_agency = models.CharField(max_length=200)
    abbreviated_name_territorial_agency = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    description = models.TextField()
    postal_address = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=500)
    oktmo = models.CharField(max_length=20, null=True)
    okato = models.CharField(max_length=20, null=True)
    okpo = models.CharField(max_length=20, null=True)
    ogrn = models.CharField(max_length=20, null=True)
    tin = models.CharField(max_length=20, null=True)
    faq_number = models.CharField(max_length=100, null=True)
    tel_number_others = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=100, null=True)
    url = models.URLField(null=True)
    email = models.EmailField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CsvFile(models.Model):

    class FileNameChoices(models.TextChoices):
        TO_LIST = 'tolist', 'Перечень территориальных органов '
        PHONE_LIST = 'phonelist', 'Телефонный справочник работников'
        OSP = 'osp', 'Перечень отделов судебных приставов'

    file = models.FileField()
    name = models.CharField(max_length=10, choices=FileNameChoices.choices)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
