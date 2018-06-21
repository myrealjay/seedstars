from django import forms

class profileForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)