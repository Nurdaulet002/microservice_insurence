from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Insurance, Insurer, Service, ICD

admin.site.register(Insurance)
admin.site.register(Insurer)
admin.site.register(Service)
admin.site.register(ICD)