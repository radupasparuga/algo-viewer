from algoViewer.sort.bubble_sort import BubbleSort
from algoViewer.sort.insertion_sort import InsertionSort
from algoViewer.sort.merge_sort import MergeSort
from algoViewer.sort.quick_sort import QuickSort
from algoViewer.sort.radix_sort import RadixSort
from algoViewer.sort.selection_sort import SelectionSort

bubble = BubbleSort()
insertion = InsertionSort()
merge = MergeSort()
quick = QuickSort()
radix = RadixSort()
selection = SelectionSort()

def create_algo_object(number_array):
  global bubble, insertion, merge, quick, radix, selection
  algo_switcher = {}
  algo_switcher[bubble.__class__.__name__] = bubble.set_array(number_array)
  algo_switcher[insertion.__class__.__name__] = insertion.set_array(number_array)
  algo_switcher[merge.__class__.__name__] = merge.set_array(number_array)
  algo_switcher[quick.__class__.__name__] = quick.set_array(number_array)
  algo_switcher[radix.__class__.__name__] = radix.set_array(number_array)
  algo_switcher[selection.__class__.__name__] = selection.set_array(number_array)

  return algo_switcher
