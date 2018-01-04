""" Given an integer 'x' and a SORTED array of size 'n', find if x occurs more than n/2 times in the array. """

"""
----> We use a modified Binary Search approach to find the index of the first occurence of x in the sorted array.
----> We then check if the value stored at the index n/2 positions away from the index found in the above step is equal to x or not. If it is, then x is a majority element, else it is not.
----> Binary Search is modified by adding a check to see if the left neighbour is equal to x, when x is found.
----> If not, the first occurence is found. Else, we recursively check on the left half of the array.
"""

def majority_element(x,arr,l=0,r=None):
	if r == None:
		r = len(arr)-1
	mid = (l+r)//2
	if arr[mid] < x:
		return majority_element(x,arr,mid+1,r)
	if arr[mid] > x:
		return majority_element(x,arr,l,mid-1)
	if arr[mid] == x:
		if arr[mid-1] == x:
			return majority_element(x,arr,l,mid-1)
		if arr[mid + (len(arr)//2)] == x:
			return True
		else:
			return False

def main():
	arr = [1, 2, 3, 4, 4, 4, 4]
	x = 4
	print(majority_element(x,arr))

if __name__ == '__main__':
	main()



"""
SIMILAR PROBLEMS

Problem: Count Occurences of x in given SORTED array.
Solution:
----> Use the above modification to find the index of the first occurence of x in the array.
----> Use a similar modification to find the index of the last occurence.
----> The difference between the two indices is the count of x in the array.

Problem: Given an array of 1s and 0s which has all 1s first followed by all 0s. Find the number of 0s.
Solution:
----> Find the index of the first occurence of 0 using the above modification.
----> The index of the last occurence is n-1.
----> The difference between the two indices is the rewuired count.

Problem: 
"""