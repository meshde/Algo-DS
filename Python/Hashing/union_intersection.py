""" Given two arrays, we have to find the union and the intersection of the two arrays. """

"""
----> We use hashmap/dictionary to solve the problem.
----> We insert each element in the first array as a key in the map/dict with it's count of occurence as the corresponding value.
----> We then traverse through the second array and check is it exists in the map/dict as key.
----> If it does, decrement the corresponding value.
----> For union operation, first all the elements of the first array are added to the result array. Then, the second array is traversed. If the element is not found as key in the map/dict or it is found but the value is 0, we add the element in the result array.
----> For intersection operation, when traversing through the second array, if the element is found in the map/dict and if the value is not 0, it is added to the result array.
"""

def union(arr1,arr2):
	d = dict()
	ans = []
	
	for x in arr1:
		try:
			d[x] += 1
		except:
			d[x] = 1
		ans.append(x)
	
	for x in arr2:
		try:
			if d[x] > 0:
				d[x] -= 1
			else:
				ans.append(x)
		except:
			ans.append(x)
	
	return ans

def intersection(arr1,arr2):
	d = dict()
	ans = []

	for x in arr1:
		try:
			d[x] += 1
		except:
			d[x] = 1

	for x in arr2:
		try:
			if d[x] > 0:
				d[x] -= 1
				ans.append(x)
		except:
			pass

	return ans

def main():
	arr1 = [10, 15, 4, 20]
	arr2 = [8, 4, 2, 10]
	print(union(arr1,arr2))
	print(intersection(arr1,arr2))
	return

if __name__ == '__main__':
	main()

