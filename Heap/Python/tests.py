from heap import MaxHeap
from heap import MinHeap

def max_heap_test():
	h = MaxHeap()
	heap_test(h)
	return
	# Output:
	# 332
	# 65
	# 49
	# 45
	# 22
	# 19
	# 4
	# 1

def min_heap_test():
	h = MinHeap()
	heap_test(h)
	return
	# Output:
	# 1
	# 4
	# 19
	# 22
	# 45
	# 49
	# 65
	# 332

def heap_test(h):
	for i in [19,4,45,65,22,1,332,49]:
		h.insert(i)
	while h.get_length() > 0:
		i = h.extract()
		print(i)
	return

if __name__ == '__main__':
	max_heap_test()
	min_heap_test()