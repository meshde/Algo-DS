""" Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array in O(logn)"""

"""
----> This problem can be solved in O(n) using Linear Search
----> To solve in O(logn), we use the Divide and Conquer paradigm.
----> We compare the middle element of the array with it's left and right neighbours.
----> If the middle element is greater than the left neighbour but less than the right one, we can infer that this part of the array is still increasing and that the answer can not lie in the left half of the arary. Hence, we recursively check in the right half only.
----> Similarly, if the middle element is less than than the left neighbour bur greater than the right one, we recusrsively check in the left half only.
----> Finally, if the middle element is greater than both it's neighbours, then that element is the point where the array changes from increasing to decreasing, and hence is the max element.
"""

def max_element(arr,l=0,r=None):
	if r == None:
		r = len(arr)-1
	if l == r:
		return arr[l]
	if r == l+1:
		return max(arr[l],arr[r])
	mid = (l+r)//2
	if arr[mid-1] <= arr[mid] and arr[mid] > arr[mid+1]:
		return arr[mid]
	if arr[mid-1] <= arr[mid]:
		return max_element(arr,mid+1,r)
	return max_element(arr,l,mid-1)

def main():
	arr = [1, 3, 50, 10, 9, 7, 6]
	print(max_element(arr))
	return

if __name__ == '__main__':
	main()


"""
SIMILAR PROBLEMS

Problem: A sorted array is rotated at some unknown point, find the minimum element in it.
Solution:
----> Can be solved similar to the above problem with slight changes.
"""