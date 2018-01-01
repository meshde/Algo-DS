"""
The LCA of nodes u and v in a tree is the ancestor of u and v that is located farthest from the root.

Applications:
----> The problem of computing lowest common ancestors of classes in an inheritance hierarchy arises in the implementation of object-oriented programming systems.
----> The LCA problem also finds applications in models of complex systems found in distributed computing.
----> In compilers, the LCA of two basic blocks is a place you can put a computation so it is available to both. This might be useful for eliminating common subexpressions.
----> Merge algorithms of version control systems.

Algorithms:
The various algorithms for finding the LCA have been implemented as part of the object method of bin_tree_node under bin_tree.py

"""

from tests import get_tree

def main():
	root = get_tree()
	x = 1
	y = 6
	print(root.get_lowest_common_ancestor(x,y,'path'))
	print(root.get_lowest_common_ancestor(x,y,'recursion'))
	return

if __name__ == '__main__':
	main()