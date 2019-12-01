from django import forms

class SortForm(forms.Form):
    CHOICES = (('BubbleSort', 'Bubble sort'), ('InsertionSort', 'Insertion sort'),('MergeSort', 'Merge sort'),('QuickSort', 'Quick sort'),('RadixSort', 'Radix sort'),('SelectionSort', 'Selection sort'),)
    file = forms.FileField()
    selection = forms.ChoiceField(choices=CHOICES)