from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
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
