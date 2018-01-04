
def median(a):
	n = len(a)
	print(a)
	if n%2 == 0:
		mid = n//2
		print(mid)
		return (a[mid] + a[mid-1])/2
	return a[n//2]

def median_of_merged_arrays(a,b):
	n = len(a)
	if n == 1:
		return (a[0]+b[0])/2
	if n == 2:
		second = max(a[0],b[0])
		third = min(a[1],b[1])
		return (second+third)/2
	m1 = median(a)
	m2 = median(b)
	if m1 == m2:
		return m1
	if m1 < m2:
		if n%2 == 0:
			mid = (n//2)-1
			return median_of_merged_arrays(a[mid+1:],b[:mid+1])
		else:
			mid = n//2
			return median_of_merged_arrays(a[mid:],b[:mid+1])
	else:
		if n%2 == 0:
			mid = (n//2)-1
			return median_of_merged_arrays(a[:mid+1],b[mid+1:])
		else:
			mid = n//2
			return median_of_merged_arrays(a[:mid+1],b[mid:])

def median_of_two_sorted_arrays_test():
	ar1 = [1, 2, 3, 6, 8]
	ar2 = [4, 6, 8, 10, 12]
	print(median_of_merged_arrays(ar1,ar2))
	return

def median_of_merged_arrays_unequal_size(a,b):
	n1 = len(a)
	n2 = len(b)

	if n1 == 1:
		if n2 == 1:
			return (a[0] + b[0])/2
		if n2%2 == 0:
			mid = n//2
			if a[0] < b[mid-1]:
				return b[mid-1]
			if b[mid-1] < a[0] and a[0] < b[mid]:
				return a[0]
			if b[mid] < a[0]
				return b[mid]
		if n%2 == 1:
			mid = n2//2
			if a[0] < b[mid]:
				if a[0] < b[mid-1]:
					return (b[mid-1] + b[mid])/2
				else:
					return (a[0] + b[mid])/2
			if a[0] == b[mid]:
				return b[mid]
			if b[mid] < a[0]:
				if b[mid+1] < a[0]:
					return (b[mid]+b[mid+1])/2
				return (b[mid]+a[0])/2

	m1 = median(a)
	m2 = median(b)
	if m1 == m2:
		return m1
	if m1 < m2:
		return median_of_merged_arrays(a[(n//2)+1:],b[:n//2])
	return median_of_merged_arrays(a[:n//2],b[(n//2)+1:])
if __name__ == '__main__':
	median_of_two_sorted_arrays_test()
