from bin_tree import bin_tree_node

def get_tree():
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

	return root

def traversal_test():
	root = get_tree()
	print("-----Inorder-----")
	root.inorder_print()
	print("-----Preorder-----")
	root.preorder_print()
	print("-----Postorder-----")
	root.postorder_print()
	return

def count_non_leaf_test():
	root = get_tree()
	print(root.count_non_leaf())
	return

def main():
	count_non_leaf_test()
	return

if __name__ == '__main__':
	main()


