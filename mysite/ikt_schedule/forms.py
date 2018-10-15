from django import forms

from .models import Class

class PostForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ('title', 'text',)