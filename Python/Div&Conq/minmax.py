""" Given an array, find the minimum and the maximum element with the least number of comparisons. """

"""
----> This problem can be solved in O(n) using the Divide & Conquer paradigm.
----> In this approach, the array is divided into two halves and the min and max of the two halves is found recursively.
----> Then the min and max of the two halves is compared to return the min and max of the array as a whole.
"""

def minmax(arr):
	n = len(arr)
	if n == 1:
		return {'min':arr[0],'max':arr[0]}
	if n == 2:
		return {'min':min(arr[0],arr[1]),'max':max(arr[0],arr[1])}
	
	mid = n//2
	
	left = minmax(arr[:mid])
	right = minmax(arr[mid:])
	
	ans = dict()
	ans['min'] = min(left['min'],right['min'])
	ans['max'] = max(left['max'],right['max'])

	return ans

def main():
	arr = [1000, 11, 445, 1, 330, 3000]
	print(minmax(arr))
	return

if __name__ == '__main__':
	main()
