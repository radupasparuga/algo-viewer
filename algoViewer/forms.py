from django import forms

class SortForm(forms.Form):
    file = forms.FileField()