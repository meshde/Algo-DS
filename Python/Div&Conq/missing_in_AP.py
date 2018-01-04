""" Given an array that represents elements of arithmetic progression in order. One element is missing in the progression, find the missing number. """

"""
----> We first calculate the difference of the AP (d).
----> This can be done by observing that if the element were not missing, the element at the ith index can be calculated as (a + (i * d)), where a is the first element of the array and the AP.
----> Hence, the last element can be calculated as (a + ((n-1) * d))), if there were no elements missing.
----> Since an element is missing, the last element is now (a + (n * d)). This is used to calculate d.
----> This problem can now be solved in O(logn) time using the Divide & Conquer paradigm.
----> We check if the middle element satisfies the second point.
----> If it does, this means that the missing element's position is not to the left of the middle element. Hence, we recursively check in the right half of the array.
----> If it doesn't, this means that the missing elements' position is to the left of the middle element. Hence, we recursively check in the left half.
----> For the base case, we check if the difference between the middle element and the element to it's direct left is equal to d. If not, we return the answer accordingly.
"""

def find_missing_util(arr):
	n = len(arr)
	d = (arr[n-1]-arr[0])//n
	return find_missing(arr,0,n-1,d)

def find_missing(arr,l,r,d):
	mid = (l+r)//2
	if l == r:
		return arr[l]+d
	if arr[mid] != arr[mid-1] + d:
		return arr[mid-1]+d
	if (arr[mid] == (arr[0] + (mid * d))):
		return find_missing(arr,mid+1,r,d)
	return find_missing(arr,l,mid-1)

def main():
	arr = [2, 4, 8, 10, 12, 14]
	print(find_missing_util(arr))

if __name__ == '__main__':
	main()