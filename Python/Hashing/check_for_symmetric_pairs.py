""" Given an array of pairs, find all symmetric pairs in it.
Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d. """

"""
----> We can use a hashmap/dictionary to solve this problem.
----> For each pair in the array, we insert the first element as key with the second element as the value.
----> At the same time we also check if the second element exists as a key in the map/dict.
----> If it does, check if the value is equal to the first element.
----> If it is, print it.
"""

def check(arr):
	d = dict()

	for a in arr:
		d[a[0]] = a[1]
		try:
			if d[a[1]] == a[0]:
				print(a)
		except:
			pass
	return

def main():
	arr = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
	check(arr)
	return

if __name__ == '__main__':
	main()