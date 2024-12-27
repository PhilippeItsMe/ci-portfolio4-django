from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pet_Businesses (models.Model):
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_mobile = models.CharField(max_length=13)
    contact_email = models.EmailField()
    firm = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=8)
    npa = models.CharField(max_length=13)
    locality = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    #logo
    #primary_image
    #secondary_images
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta :
        unique_together = ('firm', 'contact_first_name','contact_last_name')