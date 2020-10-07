class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack_using_linked_list:
	"""Implementation of Stack using Linked List"""

	def __init__(self):
		self.head = None
		self.num_elements = 0


	def push(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node

		self.num_elements += 1


	def pop(self):
		if self.is_empty():
			return

		value = self.head.value
		self.head = self.head.next
		self.num_elements -= 1
		return value


	def size(self):
		return self.num_elements


	def is_empty(self):
		return self.num_elements == 0


	def reverse_stack(self):
		stack = self
		holder_stack = Stack_using_linked_list()
		while not stack.is_empty():
			popped_element = stack.pop()
			holder_stack.push(popped_element)
		_reverse_stack_recursion(stack, holder_stack)
		
	def __repr__(self):
		current_node = self.head
		arr = []
		while current_node is not None:
			arr.append(current_node.value)
			current_node = current_node.next
		return "Stack({})".format(arr[::-1])


class Stack_using_array:
	"""Implementation of Stack using Array / List"""
	def __init__(self, initial_size = 10):
		self.arr = [0 for _ in range(initial_size)]
		self.next_index = 0
		self.num_elements = 0


	def push(self, data):
		if self.next_index == len(self.arr):
			print("Out of space! Increasing array capacity ...")
			self._handle_stack_capacity_full()

		self.arr[self.next_index] = data
		self.next_index += 1
		self.num_elements += 1


	def pop(self):
		if self.is_empty():
			self.next_index = 0
			return None
		self.next_index -= 1
		self.num_elements -= 1
		return self.arr[self.next_index]


	def size(self):
		return self.num_elements


	def is_empty(self):
		return self.num_elements == 0


	def _handle_stack_capacity_full(self):
		old_arr = self.arr

		self.arr = [0 for _ in range( 2* len(old_arr))]
		for index, element in enumerate(old_arr):
			self.arr[index] = element


	def reverse_stack(self):
		stack = self
		holder_stack = Stack_using_array()
		while not stack.is_empty():
			popped_element = stack.pop()
			holder_stack.push(popped_element)
		_reverse_stack_recursion(stack, holder_stack)
		
		
	def __repr__(self):
		arr = []
		for i in range(self.num_elements):
			arr.append(self.arr[i])
		return "Stack({})".format(arr)


def _reverse_stack_recursion(stack, holder_stack):
		if holder_stack.is_empty():
			return
		popped_element = holder_stack.pop()
		_reverse_stack_recursion(stack, holder_stack)
		stack.push(popped_element)