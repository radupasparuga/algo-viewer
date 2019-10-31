from sort_class import SortClass
import constant

class SelectionSort(SortClass):
	def __init__(self, *argv):
		super().__init__(*argv)
		print(self.input)
	
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

	def show_sort_arr(self):
	    print(self.input)	

x = SelectionSort(4, 6, 1, 3, 8)
x.create_algo()
x.show_sort_arr()