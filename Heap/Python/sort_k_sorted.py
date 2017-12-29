"""
A 'k-sorted' array is an array where each element is at most k distance away from its target position in the sorted array.

The solution is to use a min-heap of size k+1 as follows:
1. Insert first k+1 elements of k-sorted array in the heap. 
----> Now the root element of the heap will be the minimum element of the entire array as the first element can be atmost at the (k+1)th index.
2. One by one extract the value of the root of the heap and insert the next item from the k-sorted array into the heap.
3. The value extracted in the ith iteration represents the ith element in the final sorted array.
----> The min-heap in this solution can be thought of as a sliding window of size k+1, initially encompassing the first k+1 items of the k-sorted array, extracting the minimum element in the window and sliding the window to include the next element from the k-sorted array. This is then repeated.

----> Q)   Why heap of size k+1 and not N? ( where N is the total number of elements in the k-sorted array)
----> Ans) We could use heap of size and then one by one extract the minimum eleemnt from the heap or perform Heap Sort, but that would be comparatively inefficient (as size of heap would be larger). Our solution is more efficient as it considers the fact that the ith element can be atmost k indices away, hence it only makes sense to compare it with k items around it than with all elements in the array as would be done in a heap of size N.

----> Q)   Why size k+1 and not k?
----> Ans) An element can be at most k indices away, meaning an element supposed to be in the 1st index can be atmost in the (k+1)th index (these two indices are k distances apart).

"""

from heap import MinHeap

def sort_k_sorted(arr,k):
	ans = []
	h = MinHeap()
	for i in range(k+1):
		h.insert(arr[i])
	for i in range(k+1,len(arr)):
		smallest = h.extract()
		ans.append(smallest)
		h.insert(arr[i])
	while not h.is_empty():
		smallest = h.extract()
		ans.append(smallest)
	return ans

def main():
	arr =[2, 6, 3, 12, 56, 8]
	k = 3
	ans = sort_k_sorted(arr,k)
	print(ans)
	return

if __name__ == '__main__':
	main()