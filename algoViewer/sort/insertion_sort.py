from sort_class import SortClass
import constant

class InsertionSort(SortClass):
	def __init__(self, *argv):
		super().__init__(*argv)
		print(self.input)
	
	def set_array(self, *argv):
			self.input = list(argv)
    
	def create_algo(self):
		# Traverse through 1 to len(arr) 
		for i in range(1, len(self.input)): 
	
			key = self.input[i] 
	
			# Move elements of arr[0..i-1], that are 
			# greater than key, to one position ahead 
			# of their current position 
			j = i-1
			while j >= 0 and key < self.input[j] : 
					self.input[j + 1] = self.input[j] 
					j -= 1
			self.input[j + 1] = key 
	
	def switcher_algo_language(self):
		for key, _ in self.switcher_algo_language.items():
			if "C" == key:
				self.algo_language["C"] = constant.INSERTION_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = constant.INSERTION_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_language["Python"] = constant.INSERTION_SORT_PYTHON
				continue
	
	def show_sort_arr(self):
		print(self.input)

x = InsertionSort(4, 6, 1, 3, 8)
x.create_algo()
x.show_sort_arr()