
from django import forms
from .models import TestModel

class SingleUploadModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'