from heap import MinHeap
from heap import MaxHeap

def k_smallest(arr,k):
	h = MinHeap()
	for item in arr:
		h.insert(item)
	for i in range(k):
		smallest = h.extract()
		print(smallest)
	return

def k_largest(arr,k):
	h = MaxHeap()
	for item in arr:
		h.insert(item)
	for i in range(k):
		largest = h.extract()
		print(largest)
	return

def main():
	arr = [1, 23, 12, 9, 30, 2, 50]
	k = 3
	k_largest(arr,k)
	return

if __name__ == '__main__':
	main()
