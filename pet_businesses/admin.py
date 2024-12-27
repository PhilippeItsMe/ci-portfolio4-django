from django.contrib import admin
from .models import Pet_Businesse, Service_Type, Pet_Type
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pet_Businesse)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('firm', 'locality')
    search_fields = ['firm', 'locality']
    # list_filter = ('business_pet_type')
    prepopulated_fields = {'slug': ('firm',)}
    summernote_fields = ('description',)

@admin.register(Service_Type)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('service_type')
   
@admin.register(Pet_Type)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_type')

# Register your models here.
# admin.site.register(Service_Type)
# admin.site.register(Pet_Type)