""" Given two arrays, check if the second array is a sub-array of the first one. """

"""
----> This problem can be solved by creating a hashmap/dictionary for all elements of the first array with the value as their count of occurence.
----> Then we traverse through the second array, for each element checking if it exists in the hashmap/dictionary.
----> If it does, we then check if the corresponding value is greater than 0. If it does, we decrement the value. Else, we return False (This condition accounts for the situation when a certain element occurs more times in the second array than in the first).
----> If it doesn't, we return False.
----> To check if an element exists in the hashmap/dict, we could traverse through all keys till we find the element, but this increases the complexity of the solution.
----> Instead we use try...except/try...catch constructs to effectively handle the cases when the element does not exist in the map/dict.
"""

def check(arr1,arr2):
	d = dict()
	for x in arr1:
		try:
			d[x] += 1
		except:
			d[x] = 1
	for y in arr2:
		try:
			if d[y] == 0:
				return False
			d[y] -= 1
		except:
			return False
	return True

def main():
	arr1 = [11, 1, 13, 21, 3, 7]
	arr2 = [11, 3, 7, 1, 3]
	print(check(arr1,arr2))

if __name__ == '__main__':
	main()