"""
In this problem, we are given an array in which each element occurs n times, except for one. The objective is to find that one element.

----> The solution is to do bitwise modulo n addition of all the elements in the array.
----> In bitwise modulo n addition, the ith bit of the result is 0 if the ith bit is set n times or a multiple of n times in the operands.
----> n=2 is a special case in which, we can use XOR operation. (Technically, XOR is bitwise addition modulo 2)

"""
import random
import bit_magic

def repeating_twice(arr):
	xor = 0
	for x in arr:
		xor ^= x
	return xor

def repeating_twice_test():
	arr = [1,2,3,4,5,6,7,6,5,4,3,2,1]
	print(repeating_twice(arr))
	return

def repeating_n_times(arr,n):
	result = 0
	for i in range(32):
		total = 0
		for x in arr:
			total += bit_magic.get_ith_bit(x,i)
		if total%n != 0:
			result = bit_magic.set_ith_bit(result,i)
	return result

def repeating_n_times_test(n):
	arr = []
	k = random.randint(0,10)
	for i in range(1,k):
		for j in range(n):
			arr.append(i)
	arr.append(k)
	print(arr)
	print(repeating_n_times(arr,n))
	return

if __name__ == '__main__':
	repeating_n_times_test(3)