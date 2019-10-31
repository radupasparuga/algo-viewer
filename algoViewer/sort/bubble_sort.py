from sort_class import SortClass
import constant

class BubbleSort(SortClass):
    def __init__(self, *argv):
        super().__init__(*argv)
        print(self.input)

    def create_algo(self):
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
                    self.input[j], self.input[j+1] = self.input[j+1], self.input[j]
                    swapped = True

            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break

    def switcher_algo_language(self):
        for key, _ in self.algo_language.items():
            if "C" == key:
                self.algo_language["C"] = constant.BUBBLE_SORT_C
                continue
            if "Java" == key:
                self.algo_language["Java"] = constant.BUBBLE_SORT_JAVA
                continue
            if "Python" == key:
                self.algo_language["Python"] = constant.BUBBLE_SORT_PYTHON
                continue
        for k in self.algo_language.items():
            print(k)

x = BubbleSort(4, 6, 1, 3, 8)
x.create_algo()
x.switcher_algo_language()
