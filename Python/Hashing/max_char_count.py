""" Given a string, find the character that occurs the maximum. """

"""
----> The solution is to use a hashmap/dictionary.
----> The keys in the map/dict are the 26 letters of the English alphabet, and the value is the count of that character. (Initially 0)
----> Find the key with the max value. This can be done in O(1), as the dict/map size is constant (26).
"""

def get_max_char(string):
	d = dict()
	for i in range(97,123):
		d[chr(i)] = 0
	for word in string.split():
		for c in word:
			d[c] += 1
	maxi = d['a']
	ans = 'a'
	for c in d:
		if d[c] > maxi:
			maxi = d[c]
			ans = c
	return ans

def main():
	string = "sample string"
	print(get_max_char(string))
	return

if __name__ == '__main__':
	main()
