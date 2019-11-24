from sort_class import SortClass
import constant

class QuickSort(SortClass):
	def __init__(self, *argv):
		super().__init__(*argv)
		print(self.input)

	def set_array(self, *argv):
			self.input = list(argv)
    
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

	def create_algo(self, low, high):
		if low < high: 
			# pi is partitioning index, arr[p] is now 
			# at right place 
			pi = self.partition(low, high) 
			# Separately sort elements before 
			# partition and after partition 
			self.create_algo(low, pi-1) 
			self.create_algo(pi+1, high) 
	
	def switcher_algo_language(self):
		for key, _ in self.switcher_algo_language.items():
			if "C" == key:
				self.algo_language["C"] = constant.QUICK_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = constant.QUICK_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_laungauge["Python"] = constant.QUICK_SORT_PYTHON
				continue
			
	def show_sort_arr(self):
		print(self.input)

x = QuickSort(4, 6, 1, 3, 8)
x.create_algo(0, 4)
x.show_sort_arr()
