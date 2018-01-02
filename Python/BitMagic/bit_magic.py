""" NOTE: The bits are counted from LSB to MSB and counting starts from 0 """


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