from django import forms
from .models import File

#normal form
# class FileForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     file=forms.FileField()

#model form
class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields='__all__'