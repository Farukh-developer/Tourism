from django.contrib import admin
from .models import Service, Tour
# Register your models here.
admin.site.register([Tour, Service])