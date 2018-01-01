""" The problem of tree enumeration is to give a count of the different possible binary trees having 'n' number of nodes """

"""
----> A given tree is composed of three parts: the root, the left sub-tree and the right sub-tree.
----> Given the number of total nodes, we can obtain different trees by dividing the n-1 nodes (the root being excluded), among the left and right sub-trees.
----> Suppose the left tree has 'x' number of nodes, then the right sub-tree will have 'n-x-1' number of nodes.
----> Now both left and right sub-trees can be arranged in many ways given their respective count of total nodes.
----> The idea for enumeration of all possible unlabelled trees is to consider all possible pair of counts for nodes in left and right subtrees and multiply the counts for a particular pair.
----> Finally results of all pairs are added.
"""
def unlabelled_enumeration(n):
	if n == 0 or n == 1:
		return 1
	ans = 0
	for i in range(n):
		ans += (unlabelled_enumeration(i)*unlabelled_enumeration(n-i-1))
	return ans

def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n*factorial(n-1)

""" Each enumerated unlabelled tree can be used to obtained n! different labelled trees """
def labelled_enumeration(n):
	return unlabelled_enumeration(n) * factorial(n)

def main():
	print(unlabelled_enumeration(3))
	print(labelled_enumeration(3))
	return

if __name__ == '__main__':
	main()

