from django import forms
from .models import Comment
from django.contrib.auth.models import User, Group


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

class CustomSignupForm(forms.Form):
    group_choices = [
        ('Pet Owners', 'Pet Owners'),
        ('Business Owners', 'Business Owners'),
    ]
    group = forms.ChoiceField(choices=group_choices, label="Sign Up as")

    def save(self, request):
        from allauth.account.forms import CustomSignupForm
        user = CustomSignupForm().save(request)
        group_name = self.cleaned_data['group']
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        return user
    