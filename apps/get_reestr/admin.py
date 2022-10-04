from django.contrib import admin

from .models import PhoneList, ToList, Osp, CsvFile


admin.site.register(PhoneList)
admin.site.register(ToList)
admin.site.register(Osp)
admin.site.register(CsvFile)
