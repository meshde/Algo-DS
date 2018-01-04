""" Given a SORTED array of size 'n' and a number 'x', find the position of x in the array. If not found, return -1. """

"""
----> We use the standard Binary Search algorithm, which searches for an input in a sorted array in O(logn).
----> This algorithm uses the Divide and Conquer paradigm.
----> We basically check the middle element of the array:
----> i) If the middle element is equal to the required number, the element has been found and we return the middle index.
----> ii) If the middle element is less than the x, we know for sure that x is not present in the left half of the array (as the array is sorted). Hence we recursively check only for the right half.
----> iii) Similarly if the middle element is greater than x, we check recusrively for the left half of the array.
"""

def binary_search(x,arr,l=0,r=None):
	if r == None:
		r = len(arr)-1
	mid = (l+r)//2
	if l > r:
		return -1
	if l == r:
		if arr[mid] == x:
			return mid
		else:
			return -1	
	if arr[mid] == x:
		return mid
	if arr[mid] < x:
		return binary_search(x,arr,mid+1,r)
	if arr[mid] > x:
		return binary_search(x,arr,l,mid-1)

def main():
	arr = [2,3,4,5,6,9,10,78]
	print(binary_search(1,arr))
	print(binary_search(10,arr))
	print(binary_search(7,arr))
	return

if __name__ == '__main__':
	main()
