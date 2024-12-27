from django.contrib import admin
from .models import Pet_Businesse, Service_Type, Pet_Type


# Register your models here.
admin.site.register(Pet_Businesse)
admin.site.register(Service_Type)
admin.site.register(Pet_Type)