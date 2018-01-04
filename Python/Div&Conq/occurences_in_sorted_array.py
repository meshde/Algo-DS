""" Given a SORTED array of 'n' elements and a number 'x', we have to count the occurences of 'x' in the array in O(logn) time. """

"""
----> There are two approaches to this problem.
----> Method 1 (Naive): Using Linear Search we can simply iterate through the array and count the occurences of x in O(n) time.
----> Method 2 (Divide & Conquer): Whenever we have a sorted array and have to solve the given problem in O(logn), consider using the Divide & Conquer paradigm.
----> i) Check the middle element of the given array.
----> ii) If the element is less than x, then we can guarantee that x does not occur in the elements on the left of the middle element (since the array is sorted).
----> iii) Hence, we should only check for the occurences of x on the right half of the array.
----> iv) Similarly, if the middle element is greater than x, we should only check the left half of the array.
----> v) Finally, if the middle element is equal to x, we check both left and right halves further, sum their returned results and add 1 to it (1 was added as the element x was found in the middle as well).
----> vi) This approach works better than the Linear search because, as seen in points (ii) and (iv), half of the array is easily discarded at certain points during the search.
"""

def count(x,arr,l=0,r=None):
	if r == None:
		r = len(arr)-1
	# print("L:",l,"R:",r)
	if l > r:
		return 0
	mid = (l+r)//2
	if l == r:
		if arr[mid] == x:
			# print("Found at",mid)
			return 1
		return 0 
	if arr[mid] == x:
		# print("Found at",mid)
		return 1 + count(x,arr,l,mid-1) + count(x,arr,mid+1,r)
	if arr[mid] < x:
		return count(x,arr,mid+1,r)
	if arr[mid] > x:
		return count(x,arr,l,mid-1)

def main():
	arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
	x = 2
	# arr = [1,2]
	# x = 1
	print(count(x,arr))
	return

if __name__ == '__main__':
	main()
