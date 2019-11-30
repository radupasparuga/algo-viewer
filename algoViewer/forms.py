from django import forms

class SortForm(forms.Form):
    file = forms.FileField()
    CHOICES = (('bubble_sort', 'Bubble sort'), ('insertion_sort', 'Insertion sort'),('merge_sort', 'Merge sort'),('quick_sort', 'Quick sort'),('radix_sort', 'Radix sort'),('selection_sort', 'Selection sort'),)
    field = forms.ChoiceField(choices=CHOICES)