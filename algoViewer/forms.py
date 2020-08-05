from django import forms

class SortForm(forms.Form):
    CHOICES = (('BubbleSort', 'Bubble sort'), ('InsertionSort', 'Insertion sort'),('SelectionSort', 'Selection sort'),)
    file = forms.FileField()
    selection = forms.ChoiceField(choices=CHOICES)