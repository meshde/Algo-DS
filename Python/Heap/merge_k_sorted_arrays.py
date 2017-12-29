from heap import MinHeap

class CustomHeap(MinHeap):
	def __init__(self):
		super().__init__()

	def swap(self,i,j):
		temp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = temp
		return

def get_next(arr,j):
	if j < len(arr):
		return arr[j]
	return None

def merge_k_sorted_arrays(arr):
	ans = []
	h = CustomHeap()
	for i in range(len(arr)):
		h.insert((arr[i][0],i,0))
	while not h.is_empty():
		smallest,i,j = h.extract()
		ans.append(smallest)
		j += 1
		value = get_next(arr[i],j)
		if value != None:
			h.insert((value,i,j))
	return ans

def main():
	arr = [[2, 6, 12, 34],[1, 9, 20, 1000],[23, 34, 90, 2000]]
	ans = merge_k_sorted_arrays(arr)
	print(ans)
	return

if __name__ == '__main__':
	main()