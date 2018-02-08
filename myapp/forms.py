from django import forms
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class InputForm(forms.Form):
    data_input_field = forms.CharField(max_length=1, validators=[alphanumeric])
