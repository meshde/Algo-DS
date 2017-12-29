from abc import ABC
from abc import abstractmethod
from math import inf

class Heap(ABC):
	def __init__(self):
		super().__init__()
		self.heap = []
	
	def get_length(self):
		return len(self.heap)
	
	@abstractmethod
	def compare(self,A,B):
		pass

	def need_to_swap_parent(self,child):
		return not self.compare(Heap.get_parent(child),child)

	def isleaf(self,i):
		 return ((2*i)+1 >= self.get_length())

	def get_correct_child(self,parent):
		left = Heap.get_left_child(parent)
		try:
			right = Heap.get_right_child(parent)
			if self.compare(left,right):
				return left
			return right
		except:
			return left

	def swap(self,i,j):
		self.heap[j] = self.heap[j] ^ self.heap[i]
		self.heap[i] = self.heap[j] ^ self.heap[i]
		self.heap[j] = self.heap[j] ^ self.heap[i]
		return

	def heapify_up(self,i):
		if i != 0:
			if self.need_to_swap_parent(i):
				"""Swap Parent and Child"""
				self.swap(i,Heap.get_parent(i))
				"""Recursively call in the new position"""
				self.heapify_up(Heap.get_parent(i))
		return
	
	@staticmethod
	def get_left_child(i):
		return (2*i)+1
	
	@staticmethod
	def get_right_child(i):
		return (2*i)+2

	@staticmethod
	def get_parent(i):
		return i//2

	def heapify_down(self,i):
		if not self.isleaf(i):
			"""Get the child to compare the ith element with"""
			child = self.get_correct_child(i)

			if self.need_to_swap_parent(child):
				self.swap(child,i)
				self.heapify_down(child)
		return
	
	def insert(self,val):
		self.heap.append(val)
		self.heapify_up(self.get_length()-1)
		return

	def get(self):
		return self.heap[0]

	def extract(self):
		ans = self.get()
		self.heap[0] = self.heap[self.get_length()-1]
		self.heap.pop(self.get_length()-1)
		self.heapify_down(0)
		return ans


class MaxHeap(Heap):
	def __init__(self):
		super().__init__()

	def compare(self,A,B):
		return (self.heap[A]>self.heap[B])

class MinHeap(Heap):
	def __init__(self):
		super().__init__()

	def compare(self,A,B):
		return (self.heap[A]<self.heap[B])
