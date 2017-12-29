import sys
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TREE_PATH = os.path.join(os.path.join(ROOT,'BinTree'),'Python')
sys.path.append(TREE_PATH)

from bin_tree import bin_tree_node

def is_complete(node,i,total):
	if node == None:
		return True
	if i >= total:
		return False
	return ((is_complete(node.get_left_child(),(2*i)+1,total)) and (is_complete(node.get_right_child(),(2*i)+2,total)))

def is_heap(node):
	left = True
	right = True
	if node.has_left_child():
		if node.get_value() >= node.get_left_child().get_value():
			left = is_heap(node.get_left_child())
		else:
			return False
	if node.has_right_child():
		if node.get_value() >= node.get_right_child().get_value():
			right = is_heap(node.get_right_child())
		else:
			return False
	return (left and right)

def is_heap_wrapper(node):
	total = node.count_nodes()
	return (is_complete(node,0,total) and is_heap(node))

def main():
	root = bin_tree_node(10)
	root.set_left_child(bin_tree_node(9))
	root.set_right_child(bin_tree_node(8))
	root.get_left_child().set_left_child(bin_tree_node(7))
	root.get_left_child().set_right_child(bin_tree_node(6))
	root.get_right_child().set_left_child(bin_tree_node(5))
	root.get_right_child().set_right_child(bin_tree_node(4))
	root.get_left_child().get_left_child().set_left_child(bin_tree_node(3))
	root.get_left_child().get_left_child().set_right_child(bin_tree_node(2))
	root.get_left_child().get_right_child().set_left_child(bin_tree_node(1))

	print(is_heap_wrapper(root))
	return

if __name__ == '__main__':
	main()