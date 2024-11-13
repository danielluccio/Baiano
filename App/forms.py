from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['date', 'is_smok']
        widgets = {
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'is_smoke': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }