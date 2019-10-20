from sort_class import SortClass

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

        print(self.input)

    def switcher_algo_language(self):
        for key, _ in self.algo_language.items():
            if "C" == key:
                self.algo_language["C"] = """
// Optimized implementation of Bubble sort
#include <stdio.h>

void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

// An optimized version of Bubble Sort
void bubbleSort(int arr[], int n)
{
int i, j;
bool swapped;
for (i = 0; i < n-1; i++)
{
	swapped = false;
	for (j = 0; j < n-i-1; j++)
	{
		if (arr[j] > arr[j+1])
		{
		swap(&arr[j], &arr[j+1]);
		swapped = true;
		}
	}

	// IF no two elements were swapped by inner loop, then break
	if (swapped == false)
		break;
}
}

/* Function to print an array */
void printArray(int arr[], int size)
{
	int i;
	for (i=0; i < size; i++)
		printf("%d ", arr[i]);
	printf("n");
}

// Driver program to test above functions
int main()
{
	int arr[] = {64, 34, 25, 12, 22, 11, 90};
	int n = sizeof(arr)/sizeof(arr[0]);
	bubbleSort(arr, n);
	printf("Sorted array: \n");
	printArray(arr, n);
	return 0;
}
"""
                continue
            if "Java" == key:
                self.algo_language["Java"] = """
// Optimized java implementation
// of Bubble sort
import java.io.*;

class GFG
{
	// An optimized version of Bubble Sort
	static void bubbleSort(int arr[], int n)
	{
		int i, j, temp;
		boolean swapped;
		for (i = 0; i < n - 1; i++)
		{
			swapped = false;
			for (j = 0; j < n - i - 1; j++)
			{
				if (arr[j] > arr[j + 1])
				{
					// swap arr[j] and arr[j+1]
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
					swapped = true;
				}
			}

			// IF no two elements were
			// swapped by inner loop, then break
			if (swapped == false)
				break;
		}
	}

	// Function to print an array
	static void printArray(int arr[], int size)
	{
		int i;
		for (i = 0; i < size; i++)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver program
	public static void main(String args[])
	{
		int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
		int n = arr.length;
		bubbleSort(arr, n);
		System.out.println("Sorted array: ");
		printArray(arr, n);
	}
}


// This code is contributed
// by Nikita Tiwari.
"""
                continue
            if "Python" == key:
                self.algo_language["Python"] = """
# Python3 Optimized implementation
# of Bubble sort

# An optimized version of Bubble Sort
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already
		# in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to
			# n-i-1. Swap if the element
			# found is greater than the
			# next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		# IF no two elements were swapped
		# by inner loop, then break
		if swapped == False:
			break

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array :")
for i in range(len(arr)):
	print ("%d" %arr[i],end=" ")

# This code is contributed by Shreyanshi Arun
"""
                continue
        for k in self.algo_language.items():
            print(k)

x = BubbleSort(4, 6, 1, 3, 8)
x.create_algo()
x.switcher_algo_language()
