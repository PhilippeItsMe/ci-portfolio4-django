from django import forms
from .models import Pet_Businesse

class Pet_Businesses_Form(forms.ModelForm):
    class Meta:
        model = Pet_Businesse
        fields = ('firm','street','number','npa','locality','phone','email',
                  'website','linkedin','facebook','instagram','tiktok',
                  'business_pet_type','business_service_type', 'description',)
        widgets = {
            'business_pet_type': forms.CheckboxSelectMultiple,
            'business_service_type': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 4}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://'}),
        }
        labels = {
            'firm': 'Business Name',
            'business_pet_type': 'Pet Types Served',
            'business_service_type': 'Services Offered',
        }
    
