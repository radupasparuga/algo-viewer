from algoViewer.sort.sort_class import SortClass
from .constant import MERGE_SORT_C, MERGE_SORT_JAVA, MERGE_SORT_PYTHON

class MergeSort(SortClass):
	def __init__(self):
		super().__init__()

	def set_array(self, argv):
		self.input = argv

	def create_algo(self):
		sort_steps = []
		self.merge_sort(self.input)	

	def merge_sort(self, arr):
		if len(arr) > 1:
			mid = len(arr)//2
			L = arr[:mid]
			R = arr[mid:]

			self.merge_sort(L)
			self.merge_sort(R)

			i = j = k = 0

			while i < len(L) and j < len(R):
				if L[i] < R[j]:
					arr[k] = L[i]
					i += 1
				else:
					arr[k] = R[j]
					j += 1
				k += 1
			
			while i < len(L):
				arr[k] = L[i]
				i += 1
				k += 1
			
			while j < len(R):
				arr[k] = R[j]
				j += 1
				k += 1

	def switcher_algo_language(self):
		for key, _ in self.algo_language.items():
			if "C" == key:
				self.algo_language["C"] = MERGE_SORT_C
				continue
			if "Java" == key:
				self.algo_language["Java"] = MERGE_SORT_JAVA
				continue
			if "Python" == key:
				self.algo_language["Python"] = MERGE_SORT_PYTHON
				continue

	def show_sort_arr(self):
		print(self.input)
