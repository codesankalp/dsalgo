class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue_from_linked_list():

	def __init__(self):
		self.head = None
		self.tail = None
		self.num_elements = 0

	def enqueue(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			self.tail.next = new_node
			self.tail = self.tail.next
		self.num_elements += 1

	def dequeue(self):
		if self.is_empty():
			return None
		value = self.head.value
		self.head = self.head.next
		self.num_elements -= 1
		return value

	def size(self):
		return self.num_elements

	def is_empty(self):
		return self.num_elements == 0
		
	def __repr__(self):
		current_node = self.head
		arr = []
		while current_node is not None:
			arr.append(current_node.value)
			current_node = current_node.next
		return "Queue({})".format(arr)


class Queue_from_array():

	def __init__(self, initial_size=10):
		self.arr = [0 for _ in range(initial_size)]
		self.next_index = 0
		self.front_index = -1
		self.queue_size = 0

	def enqueue(self, value):
		# if queue is already full --> increase capacity
		if self.queue_size == len(self.arr):
			self._handle_queue_capacity_full()

		# enqueue new element
		self.arr[self.next_index] = value
		self.queue_size += 1
		self.next_index = (self.next_index + 1) % len(self.arr)
		if self.front_index == -1:
			self.front_index = 0

	def dequeue(self):
		# check if queue is empty
		if self.is_empty():
			self.front_index = -1
			self.next_index = 0
			return None

		# dequeue front element
		value = self.arr[self.front_index]
		self.front_index = (self.front_index + 1) % len(self.arr)
		self.queue_size -= 1
		return value

	def size(self):
		return self.queue_size

	def is_empty(self):
		return self.size() == 0

	def front(self):
		# check if queue is empty
		if self.is_empty():
			return None
		return self.arr[self.front_index]

	def _handle_queue_capacity_full(self):
		old_arr = self.arr
		self.arr = [0 for _ in range(2 * len(old_arr))]

		index = 0

		for i in range(self.front_index, len(old_arr)):
			self.arr[index] = old_arr[i]
			index += 1

		for i in range(0, self.front_index):
			self.arr[index] = old_arr[i]
			index += 1

		self.front_index = 0
		self.next_index = index
		
	def __repr__(self):
		arr = []
		for i in range(self.queue_size):
			arr.append(self.arr[i])
		return "Queue({})".format(arr)
