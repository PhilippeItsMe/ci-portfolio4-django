from django.contrib import admin
from .models import Pet_Businesse, Service_Type, Pet_Type, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pet_Businesse)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('firm', 'locality','approved', 'date_created')
    search_fields = ['firm', 'locality']
    prepopulated_fields = {'slug': ('firm',)}
    summernote_fields = ('description',)

@admin.register(Service_Type)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('service_type', 'date_created')
   
@admin.register(Pet_Type)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_type','date_created')

@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_businesse', 'author', 'approved','date_created') 

# Register your models here.
# admin.site.register(Service_Type)
# admin.site.register(Pet_Type)