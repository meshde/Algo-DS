class bin_tree_node(object):
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        if self is None and other is None:
            return True

        if self is None or other is None:
            return False

        if isinstance(other, int):
            return self.get_value() == other

        return (self.value == other.value
                and self.get_left_child() == other.get_left_child()
                and self.get_right_child() == other.get_right_child()
               )

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self,node):
        self.left = node
        return

    def set_right_child(self,node):
        self.right = node
        return

    def has_left_child(self):
        return not (self.get_left_child() == None)

    def has_right_child(self):
        return not (self.get_right_child() == None)

    def is_leaf(self):
        return (not (self.has_right_child() or self.has_left_child()))

    def count_nodes(self):
        left_count = 0
        right_count = 0
        if self.has_left_child():
            left_count = self.get_left_child().count_nodes()
        if self.has_right_child():
            right_count = self.get_right_child().count_nodes()
        return 1 + left_count + right_count

    def count_non_leaf(self):
        if self.is_leaf():
            return 0
        left_count = 0
        right_count = 0
        if self.has_left_child():
            left_count = self.get_left_child().count_non_leaf()
        if self.has_right_child():
            right_count = self.get_right_child().count_non_leaf()
        return 1 + left_count + right_count

    def inorder_print(self):
        if self.has_left_child():
            self.get_left_child().inorder_print()
        print(self.get_value())
        if self.has_right_child():
            self.get_right_child().inorder_print()
        return

    def preorder_print(self):
        print(self.get_value())
        if self.has_left_child():
            self.get_left_child().preorder_print()
        if self.has_right_child():
            self.get_right_child().preorder_print()
        return

    def postorder_print(self):
        if self.has_left_child():
            self.get_left_child().postorder_print()
        if self.has_right_child():
            self.get_right_child().postorder_print()
        print(self.get_value())
        return

    def get_path(self,value,path):
        if self.get_value() == value:
            path.append(self.get_value())
            return True
        if self.has_left_child() and self.get_left_child().get_path(value,path):
            path.insert(0,self.get_value())
            return True
        if self.has_right_child() and self.get_right_child().get_path(value,path):
            path.insert(0,self.get_value())
            return True
        return False

    def get_path_from_root(self,value):
        path = []
        if self.get_path(value,path):
            return path
        return None

    """ For theoretical information about LCA, please refer the lowest_common_ancestor.py file. """
    def get_lowest_common_ancestor(self,x,y,method='path'):
        if method == 'path':
            return self.get_lowest_common_ancestor_with_path(x,y)
        if method == 'recursion':
            return self.get_lowest_common_ancestor_with_recursion(x,y).get_value()
        print("method not recognised!")
        return None

    """ In the following method, LCA is found by listing out the paths from root to both the nodes, and then comapring the paths and outputting the last common value as LCA. """
    def get_lowest_common_ancestor_with_path(self,x,y):
        path_x = self.get_path_from_root(x)
        path_y = self.get_path_from_root(y)
        if path_x and path_y:
            mini = min(len(path_x),len(path_y))
            for i in range(mini):
                if path_x[i] != path_y[i]:
                    return path_x[i-1]
            return path_x[mini-1]
        return None

    """
    ----> In this method we use recusion to find the LCA of two nodes.
    ----> The method can be thought of as one that checks if either of the two nodes is present in the tree.
    ----> The method returns None if neither of the nodes is present.
    ----> If either node is the root itself, the root is returned as the LCA.
    ----> If not, the method is recursively called for the left and right sub-trees.
    ----> If both recursive calls return a node, this means that one of the two nodes was found in the left sub-tree and the other was found in the right sub-tree. In this case, the current node itself is returned as the LCA.
    ----> If only one call returns a node and the other returns None, then the node returned by the recursive call is the LCA.
    ----> If neither calls return a node, then LCA is does not exist in the tree and None is returned.
    """
    def get_lowest_common_ancestor_with_recursion(self,x,y):
        if x == self.get_value() or y == self.get_value():
            return self
        left = None
        right = None
        if self.has_left_child():
            left = self.get_left_child().get_lowest_common_ancestor_with_recursion(x,y)
        if self.has_right_child():
            right = self.get_right_child().get_lowest_common_ancestor_with_recursion(x,y)
        if left and right:
            return self
        if left or right:
            if left:
                return left
            return right
        return None
