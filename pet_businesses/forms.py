from django import forms
from .models import PetBusiness, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


# Pet business form

class PetBusinessForm(forms.ModelForm):
    """
    Form for creating and updating PetBusiness instances.
    """
    class Meta:
        model = PetBusiness
        fields = [
            'firm',
            'slug',
            'street',
            'number',
            'npa',
            'locality',
            'phone',
            'email',
            'website',
            'linkedin',
            'facebook',
            'instagram',
            'tiktok',
            'business_pet_type',
            'business_service_type',
            'description',
        ]
        widgets = {
            'firm': forms.TextInput(attrs={'class': 'form-control', 'id': 'firm-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'id': 'slug-input'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'npa': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'tiktok': forms.URLInput(attrs={'class': 'form-control'}),
            'business_pet_type': forms.CheckboxSelectMultiple(),
            'business_service_type': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'firm': 'Business Name',
            'slug': 'Page url',
            'street': 'Street Address',
            'number': 'Street Number',
            'npa': 'Postal Code',
            'locality': 'City',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'website': 'Website',
            'linkedin': 'LinkedIn Profile',
            'facebook': 'Facebook Page',
            'instagram': 'Instagram Profile',
            'tiktok': 'TikTok Profile',
            'business_pet_type': 'Pet Types Supported',
            'business_service_type': 'Services Offered',
            'description': 'Business Description',
        }


# Comments form

class CommentForm(forms.ModelForm):
    """
    Form to enter comments.
    """
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_body'}),
        }


# Registration form

class UserRegistrationForm(UserCreationForm):
    """
    User registration form extending Django's built-in UserCreationForm.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomSignupForm(forms.Form):
    """
    Custom signup form to register users by group.
    """
    group_choices = [
        ('Pet Owners', 'Pet Owners'),
        ('Business Owners', 'Business Owners'),
    ]
    group = forms.ChoiceField(choices=group_choices, label="Sign Up as")

    def signup(self, request, user):
        group_name = self.cleaned_data['group']
        try:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
        except Group.DoesNotExist:
            raise ValueError(f"The group '{group_name}' does not exist.")
        user.save()
        return user
