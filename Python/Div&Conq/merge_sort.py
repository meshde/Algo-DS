def get_mid(l,r):
	return (l+r)//2

def merge_sort(arr,l=0,r=None):
	if r == None:
		r = len(arr)-1
	if l < r:
		mid = get_mid(l,r)
		merge_sort(arr,l,mid)
		merge_sort(arr,mid+1,r)
		merge(arr,l,r)
	return

def merge(arr,l,r):
	mid = get_mid(l,r)
	left = arr[l:mid+1]
	right = arr[mid+1:r+1]
	i = 0
	j = 0
	k = l
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
	return

def main():
	arr = [12, 11, 13, 5, 6, 7]
	merge_sort(arr)
	print(arr)
	return

if __name__ == '__main__':
	main()
