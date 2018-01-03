""" 
NOTES: 
----> The bits are counted from LSB to MSB and counting starts from 0.
----> A bit is set if it is 1 and unset if it is 0.

"""


""" Returns mask with ith bit equal to the ith bit of num """
def get_ith_bit_mask(num,i):
	temp_mask = (1 << i)
	return (num & temp_mask)


""" Returns the ith bit of num """
def get_ith_bit(num,i):
	mask = get_ith_bit_mask(num,i)
	if mask == 0:
		return 0
	return 1


""" Sets the ith bit of num """
def set_ith_bit(num,i):
	mask = (1 << i)
	num |= mask
	return num


""" Unsets the rightmost set bit.
----> Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set bit(including the righmost set bit).
----> So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the righmost set bit. 
"""
def clear_lowest_set_bit(num):
	return (num & (num-1))


""" Counts the number of set bits in the binary representation of the number 
----> The idea is to one-by-one unset the rightmost set bit.
----> The number of bits that were unset is counted.
----> This count represents the total number of set bits in the original number as all set bits were one-by-one unset from right to left. 
"""
def count_set_bits(num):
	ans = 0
	while(num):
		num = clear_lowest_set_bit(num)
		ans += 1
	return ans


""" Checks if the given number is a power of 2 """
def is_power_of_2(num,method='clear'):
	if method = 'count':
		return is_power_of_2_count(num)
	if method == 'clear':
		return is_power_of_2_clear(num)
	print("Method not recognised!!")
	return

""" Checks if the given number is a power of 2 by checking if the exactly one bit is set or not. """
def is_power_of_2_count(num):
	count = count_set_bits(num)
	return (count == 1)

""" Checks if the given number is a power of 2 by clearing the rightmost set bit and checking if the result is 0 or not. """
def is_power_of_2_clear(num):
	num = clear_lowest_set_bit(num)
	return (num == 0)
