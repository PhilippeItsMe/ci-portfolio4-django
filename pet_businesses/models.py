from django.db import models


#----------- Pet Businesses Model -----------#

class Service_Type (models.Model):
    service_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["service_type"]

    def __str__(self):
        return f"{self.service_type}"


class Pet_Type (models.Model):
    pet_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["pet_type"]

    def __str__(self):
        return f"{self.pet_type}"


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
    business_pet_type = models.ManyToManyField(
        Pet_Type, 
        related_name="business_pet_types"
    )
    business_service_type = models.ManyToManyField(
        Service_Type, 
        related_name="business_service_types"
    )
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Generate slug from the firm if not set
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.firm)
        super(Pet_Businesse, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-last_modified"]

    def __str__(self):
        return f"{self.firm}"
