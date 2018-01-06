""" Given a an array and an input number 'x', check if there exists a pair in the array that sums upto x. """

"""
----> The solution is to use a hahsmap/dictionary with key as each element of the array and the value as 1.
----> Traverse through the array and for each element 'a', check if 'x-a' exists in the map/dict as a key.
----> If it does, return True.
----> Else, add 'a' as a key in the map/dict with value as 1 (or any random number/object).
----> We use try...catch/try...except constructs to check if a key exists in the map/dict, rather than having to search through the entire map/dict. 
"""

def check(arr,x):
	d = dict()

	for a in arr:
		try:
			d[x-a]
			return True
		except:
			d[a] = 1
	return False

def main():
	arr = [1, 4, 45, 6, 10, 8]
	x = 6
	print(check(arr,x))
	return

if __name__ == '__main__':
	main()



"""
SIMILAR PROBLEMS

Problem: Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.
Solution: This can be solved by slightly modifying the above code.
"""