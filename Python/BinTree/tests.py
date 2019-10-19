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

def add_node_to_bst(bst, val):
    if val < bst.get_value():
        if bst.has_left_child():
            add_node_to_bst(bst.get_left_child(), val)
        else:
            bst.set_left_child(bin_tree_node(val))
    else:
        if bst.has_right_child():
            add_node_to_bst(bst.get_right_child(), val)
        else:
            bst.set_right_child(bin_tree_node(val))

def get_bst(arr):
    root_val = arr[0]
    bst = bin_tree_node(root_val)

    for val in arr[1:]:
        add_node_to_bst(bst, val)

    return bst

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

def get_path_from_root_test(value = 1):
	root = get_tree()
	path = root.get_path_from_root(value)
	if path:
		print(path)
	else:
		print("Not Found!!!")
	return

def LCA_test():
	root = get_tree()
	print(root.get_lowest_common_ancestor(1,2,method='recursion'))
	return

def main():
	LCA_test()
	return

if __name__ == '__main__':
	main()


