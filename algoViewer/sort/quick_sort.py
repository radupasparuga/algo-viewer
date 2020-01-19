from algoViewer.sort.sort_class import SortClass
from .constant import QUICK_SORT_C, QUICK_SORT_JAVA, QUICK_SORT_PYTHON

class QuickSort(SortClass):
	def __init__(self):
		super().__init__()

	def set_array(self, argv):
			self.input = argv
    
	def partition(self, low, high): 
		i = ( low-1 )         # index of smaller element 
		pivot = self.input[high]     # pivot 
	
		for j in range(low , high): 
	
			# If current element is smaller than the pivot 
			if   self.input[j] < pivot: 
			
				# increment index of smaller element 
				i = i+1 
				self.input[i], self.input[j] = self.input[j], self.input[i] 
	
		self.input[i+1], self.input[high] = self.input[high], self.input[i+1] 
		return ( i+1 ) 

	def quick_sort(self, low, high):
		if low < high: 
			# pi is partitioning index, arr[p] is now 
			# at right place 
			pi = self.partition(low, high) 
			# Separately sort elements before 
			# partition and after partition 
			self.quick_sort(low, pi-1) 
			self.quick_sort(pi+1, high) 
		
	def create_algo(self): 
		n = len(self.input)
		self.quick_sort(0, n-1)
	
	def switcher_algo_language(self):
		for key, _ in self.switcher_algo_language.items():
			if "C" == key:
				self.algo_language["C"] = QUICK_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = QUICK_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_laungauge["Python"] = QUICK_SORT_PYTHON
				continue
			
	def show_sort_arr(self):
		print(self.input)
