from django.contrib import admin
from .models import PetBusinesse, ServiceType, PetType, Comment, Like
from django_summernote.admin import SummernoteModelAdmin


@admin.register(PetBusinesse)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('firm', 'locality','approved', 'date_created')
    search_fields = ['firm', 'locality']
    prepopulated_fields = {'slug': ('firm',)}
    summernote_fields = ('description',)

@admin.register(ServiceType)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('service_type', 'date_created')
   
@admin.register(PetType)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_type','date_created')

@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_businesse', 'author', 'approved','date_created') 

@admin.register(Like)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('pet_businesse', 'author') 
    