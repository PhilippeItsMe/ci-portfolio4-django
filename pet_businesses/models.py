from django.db import models


class Pet_Businesse (models.Model):
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_mobile = models.CharField(max_length=16)
    contact_email = models.EmailField()
    firm = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=8)
    npa = models.CharField(max_length=13)
    locality = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firm}"


class Service_Type (models.Model):
    pet_business = models.ForeignKey(
        Pet_Businesse, 
        on_delete=models.SET_NULL,  
        related_name="business_service_types",
        null=True
    )
    service_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_type} ({self.pet_business})"


class Pet_Type (models.Model):
    pet_business = models.ForeignKey(
        Pet_Businesse, 
        on_delete=models.SET_NULL,  
        related_name="business_pet_types",
        null=True
    )
    pet_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet_type} ({self.pet_business})"


class Pet_Type (models.Model):
     pet_business = models.ForeignKey(
         Pet_Businesse,  
         on_delete=models.SET_NULL,  
         related_name="business_pet_types",
         null=True)
     pet_type = models.CharField(max_length=150)
     date_created = models.DateTimeField(auto_now_add=True)
     last_modified = models.DateTimeField(auto_now=True)

     def __str__(self):
        return f"{self.pet_type} ({self.pet_business})"
