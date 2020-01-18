from algoViewer.sort.sort_class import SortClass
from .constant import BUBBLE_SORT_C, BUBBLE_SORT_JAVA, BUBBLE_SORT_PYTHON

class BubbleSort(SortClass):
    def __init__(self):
        super().__init__()

    def set_array(self, argv):
        self.input = argv

    def create_algo(self):
        sort_steps = []
        n = len(self.input)
        # Traverse through all self.inputay elements
        for i in range(n):
            swapped = False
            # Last i elements are already
            #  in place
            for j in range(0, n-i-1):
                # traverse the self.inputay from 0 to
                # n-i-1. Swap if the element
                # found is greater than the
                # next element
                if self.input[j] > self.input[j+1] :
                    pair = [j, j+1]
                    sort_steps.append(pair)
                    self.input[j], self.input[j+1] = self.input[j+1], self.input[j]
                    swapped = True
            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break
        return sort_steps

    def switcher_algo_language(self):
        for key, _ in self.algo_language.items():
            if "C" == key:
                self.algo_language["C"] = BUBBLE_SORT_C
                continue
            if "Java" == key:
                self.algo_language["Java"] = BUBBLE_SORT_JAVA
                continue
            if "Python" == key:
                self.algo_language["Python"] = BUBBLE_SORT_PYTHON
                continue

    def show_sort_arr(self):
	    print(self.input)
