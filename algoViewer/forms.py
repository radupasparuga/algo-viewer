from django import forms

class SortForm(forms.Form):
    CHOICES = (('bubble_sort', 'Bubble sort'), ('insertion_sort', 'Insertion sort'),('merge_sort', 'Merge sort'),('quick_sort', 'Quick sort'),('radix_sort', 'Radix sort'),('selection_sort', 'Selection sort'),)
    file = forms.FileField()
    selection = forms.ChoiceField(choices=CHOICES)