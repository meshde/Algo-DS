class bin_tree_node(object):
	def __init__(self,val):
		self.value = val
		self.left = None
		self.right = None

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

	def count_nodes(self):
		left_count = 0
		right_count = 0
		if self.has_left_child():
			left_count = self.get_left_child().count_nodes()
		if self.has_right_child():
			right_count = self.get_right_child().count_nodes() 
		return 1 + left_count + right_count