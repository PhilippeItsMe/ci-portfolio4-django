from django.db import models
from django.contrib.auth.models import User


# Pet Businesses Model

class ServiceType (models.Model):
    """
    Model for types of pet services.
    """
    service_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["service_type"]
        verbose_name = "Service Type"
        verbose_name_plural = "Service Types"

    def __str__(self):
        return f"{self.service_type}"


class PetType (models.Model):
    """
    Model for types of pets.
    """
    pet_type = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["pet_type"]
        verbose_name = "Pet Type"
        verbose_name_plural = "Pet Types"

    def __str__(self):
        return f"{self.pet_type}"


class PetBusiness (models.Model):
    """
    Model representing a pet business with details such as address,
    contact information, and services offered.
    """
    firm = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="pet_business_user", default=1)
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
        PetType,
        related_name="business_pet_types"
    )
    business_service_type = models.ManyToManyField(
        ServiceType,
        related_name="business_service_types"
    )
    description = models.TextField()
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-last_modified"]
        verbose_name = "Pet Business"
        verbose_name_plural = "Pet Businesses"

    def __str__(self):
        return f"{self.firm}"


# Comment Model

class Comment(models.Model):
    """
    Model for comments on pet businesses.
    """
    pet_businesse = models.ForeignKey(PetBusiness,
                                      on_delete=models.CASCADE,
                                      related_name="comments")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="commenter")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["date_created"]

    def __str__(self):
        return f"Comment {self.content} by {self.author}"


# Like Model

class Like(models.Model):
    """
    Model for likes on pet businesses.
    """
    pet_businesse = models.ForeignKey(PetBusiness,
                                      on_delete=models.CASCADE,
                                      related_name="likes")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="liker")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        constraints = [
            models.UniqueConstraint(fields=['pet_businesse', 'author'],
                                    name='unique_like')
        ]

    def __str__(self):
        return f'{self. author} {self.pet_businesse}'
