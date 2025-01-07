from django import forms
from .models import Comment

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_body'}),
        }
