from algoViewer.sort.sort_class import SortClass
from .constant import SELECTION_SORT_C, SELECTION_SORT_JAVA, SELECTION_SORT_PYTHON

class SelectionSort(SortClass):
	def __init__(self):
		super().__init__()
	
	def set_array(self, argv):
			self.input = argv

	def create_algo(self):
		# Traverse through all array elements 
		for i in range(len(self.input)): 
			
			# Find the minimum element in remaining  
			# unsorted array 
			min_idx = i 
			for j in range(i+1, len(self.input)): 
				if self.input[min_idx] > self.input[j]: 
					min_idx = j 
					
			# Swap the found minimum element with  
			# the first element         
			self.input[i], self.input[min_idx] = self.input[min_idx], self.input[i] 

	def switcher_algo_language(self):
		for key, _ in self.algo_language.items():
			if "C" == key:
				self.algo_language["C"] = SELECTION_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = SELECTION_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_language["Python"] = SELECTION_SORT_PYTHON
				continue

	def show_sort_arr(self):
	    print(self.input)	
