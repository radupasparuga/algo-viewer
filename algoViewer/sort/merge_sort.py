from sort_class import SortClass
import constant 

class MergeSort(SortClass):
	def __init__(self, *argv):
		super().__init__(*argv)
		print(self.input)

	def set_array(self, *argv):
			self.input = list(argv)

	def create_algo(self, arr):
		if len(arr) >1: 
			mid = len(arr)//2 #Finding the mid of the array 
			L = arr[:mid] # Dividing the array elements  
			R = arr[mid:] # into 2 halves 
	
			create_algo(L) # Sorting the first half 
			create_algo(R) # Sorting the second half 
	
			i = j = k = 0
			
			# Copy data to temp arrays L[] and R[] 
			while i < len(L) and j < len(R): 
				if L[i] < R[j]: 
					arr[k] = L[i] 
					i+=1
				else: 
					arr[k] = R[j] 
					j+=1
				k+=1
			
			# Checking if any element was left 
			while i < len(L): 
				arr[k] = L[i] 
				i+=1
				k+=1
			
			while j < len(R): 
				arr[k] = R[j] 
				j+=1
				k+=1

	def switcher_algo_language(self):
		for key, _ in self.algo_language.items():
			if "C" == key:
				self.algo_language["C"] = constant.MERGE_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = constant.MERGE_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_language["Python"] = constant.MERGE_SORT_PYTHON
				continue

	def show_sort_arr(self):
		print(self.input)

x = MergeSort(4, 6, 1, 3, 8)
x.create_algo([4, 6, 1, 3, 8])
x.show_sort_arr()
