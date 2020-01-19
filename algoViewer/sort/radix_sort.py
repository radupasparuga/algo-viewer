from algoViewer.sort.sort_class import SortClass
from .constant import RADIX_SORT_C, RADIX_SORT_JAVA, RADIX_SORT_PYTHON

class RadixSort(SortClass):
	def __init__(self):
		super().__init__()

	def set_array(self, argv):
			self.input = argv

	def counting_sort(self, exp1):
		n = len(self.input) 
		# The output array elements that will have sorted arr 
		output = [0] * (n) 
		# initialize count array as 0 
		count = [0] * (10) 
		# Store count of occurrences in count[] 
		for i in range(0, n): 
			index = (self.input[i]//exp1) 
			count[(index)%10] += 1
	
		# Change count[i] so that count[i] now contains actual 
		#  position of this digit in output array 
		for i in range(1,10): 
			count[i] += count[i-1] 
	
		# Build the output array 
		i = n-1
		while i>=0: 
			index = (self.input[i]//exp1) 
			output[count[(index)%10] - 1] = self.input[i] 
			count[(index)%10] -= 1
			i -= 1
	
		# Copying the output array to arr[], 
		# so that arr now contains sorted numbers 
		i = 0
		for i in range(0,len(self.input)): 
			self.input[i] = output[i] 
	
	def create_algo(self):
		sort_steps = []
		# Find the maximum number to know number of digits 
		max1 = max(self.input) 
	
		# Do counting sort for every digit. Note that instead 
		# of passing digit number, exp is passed. exp is 10^i 
		# where i is current digit number 
		exp = 1
		while max1/exp > 0: 
			self.counting_sort(exp) 
			exp *= 10

	def show_sort_arr(self):
		print(self.input)
