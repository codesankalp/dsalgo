class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None


	def append(self, value):
		"""next node creation of linked list"""
		if self.head is None:
			self.head = Node(value)
			return

		# Move to the tail (the last node)
		node = self.head
		while node.next:
			node = node.next

		node.next = Node(value)
		return


	def print(self):
		"""print nodes of the linked list"""
		current_node = self.head
		
		while current_node is not None:
			print(current_node.value)
			current_node = current_node.next


	def to_list(self):
		"""Returns python list of Linked List"""
		out_list = []

		node = self.head
		while node:
			out_list.append(node.value)
			node = node.next

		return out_list

	def to_linked_list(self,array):
		"""
		appends array elements into linked list
		args: array(obj) -> python list
		return : None
		"""
		for i in array:
			self.append(i)

	def prepend(self, value):
		""" Prepend a node to the beginning of the list """

		if self.head is None:
			self.head = Node(value)
			return

		new_head = Node(value)
		new_head.next = self.head
		self.head = new_head


	def search(self, value):
		""" Search the linked list for a node with the requested value and return the node. """
		if self.head is None:
			return None

		node = self.head
		while node:
			if node.value == value:
				return node
			node = node.next

		raise ValueError("Value not found in the list.")


	def remove(self, value):
		""" Delete the first node with the desired data. """
		if self.head is None:
			return

		if self.head.value == value:
			self.head = self.head.next
			return

		node = self.head
		while node.next:
			if node.next.value == value:
				node.next = node.next.next
				return
			node = node.next

		raise ValueError("Value not found in the list.")


	def pop(self):
		""" Return the first node's value and remove it from the list. """
		if self.head is None:
			return None

		node = self.head
		self.head = self.head.next

		return node.value

	def insert(self, value, pos):
		""" Insert value at pos position in the list. If pos is larger than the
			length of the list, append to the end of the list. """
		# If the list is empty 
		if self.head is None:
			self.head = Node(value)
			return
			
		if pos == 0:
			self.prepend(value)
			return

		index = 0
		node = self.head
		while node.next and index <= pos:
			if (pos - 1) == index:
				new_node = Node(value)
				new_node.next = node.next
				node.next = new_node
				return

			index += 1
			node = node.next
		else:
			self.append(value)


	def size(self):
		""" Return the size or length of the linked list. """
		size = 0
		node = self.head
		while node:
			size += 1
			node = node.next

		return size


	def reverse(self):
		"""
		Reverse the inputted linked list

		Args:
		   linked_list(obj): Linked List to be reversed
		Returns:
		   obj: Reveresed Linked List
		"""
		new_list = LinkedList()
		
		prev_node = None

		current_node = self.head
		
		while current_node is not None:
			new_node = Node(current_node.value)
			new_node.next = prev_node 
			prev_node = new_node
			current_node = current_node.next

		new_list.head = prev_node
		
		return new_list


	def iscircular(self):
		"""
		Determine wether the Linked List is circular or not

		Args:
		   linked_list(obj): Linked List to be checked
		Returns:
		   bool: Return True if the linked list is circular, return False otherwise
		"""

		if self.head is None:
			return False
		
		slow = self.head
		fast = self.head
		
		while fast and fast.next:
			# slow pointer moves one node
			slow = slow.next
			# fast pointer moves two nodes
			fast = fast.next.next
			
			if slow == fast:
				return True
		
		# If we get to a node where fast doesn't have a next node or doesn't exist itself, 
		# the list has an end and isn't circular
		return False


	def swap_nodes(self, position_one, position_two):
		"""
		:param: head- head of input linked list
		:param: `position_one` - indicates position (index) ONE
		:param: `position_two` - indicates position (index) TWO
		return: head of updated linked list with nodes swapped
		"""

		# If both the indices are same
		if position_one == position_two:
			return head
		
		# Helper references
		one_previous = None
		one_current = None

		two_previous = None
		two_current = None

		current_index = 0
		current_node = self.head 
		new_head = None

		# LOOP - find out previous and current node at both the positions (indices)
		while current_node is not None:
			
			# Position_one cannot be equal to position_two, 
			# so either one of them might be equal to the current_index
			if current_index == position_one:
				one_current = current_node
			
			elif current_index == position_two:
				two_current = current_node
				break

			# If neither of the position_one or position_two are equal to the current_index
			if one_current is None:
				one_previous = current_node
			
			two_previous = current_node
			
			# increment both the current_index and current_node
			current_node = current_node.next         
			current_index += 1
			

		# Loop ends
		
		
		'''SWAPPING LOGIC'''
		# We have identified the two nodes: one_current & two_current to be swapped, 
		# Make use of a temporary reference to swap the references
		two_previous.next = one_current
		temp = one_current.next
		one_current.next = two_current.next
		two_current.next = temp
		
		# if the node at first index is head of the original linked list
		if one_previous is None:
			new_head = two_current
		else:
			one_previous.next = two_current
			new_head = self.head
		# Swapping logic ends
		
		return new_head

	def sort_append(self, value):
		"""
		Append a value to the Linked List in ascending sorted order

		Args:
		   value(int): Value to add to Linked List
		"""
		if self.head is None:
			self.head = Node(value)
			return
		
		if value < self.head.value:
			node = Node(value)
			node.next = self.head
			self.head = node
			return
		
		node = self.head
		while node.next is not None and value >= node.next.value:
			node = node.next
			
		new_node = Node(value)
		new_node.next = node.next
		node.next = new_node
		
		return None

	def sort(self):
		"""
		returns sorted linkedlist

		Args:
		   None
		Returns:
		   array: Return sorted Linkedlist
		"""

		sorted_array = []
		array = self.to_list()

		linked_list = LinkedList()
		for value in array:
			linked_list.sort_append(value)
		
		# Convert sorted linked list to a normal list/array
		node = linked_list.head
		while node:
			sorted_array.append(node.value)
			node = node.next
		
		return linked_list


	def skip_i_delete_j(self, i, j):
		"""
		:param: head - head of linked list
		:param: i - first `i` nodes that are to be skipped
		:param: j - next `j` nodes that are to be deleted
		return - return the updated head of the linked list
		"""
		'''
		The Idea: 
			Traverse the Linkedist. Make use of two references - `current` and `previous`.
			- Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
			- Delete next `j` nodes. Keep incrementing the `current`.
			- Connect the `previous.next` to the `current`
		'''
		# Edge case - Skip 0 nodes (means Delete all nodes)
		head = self.head
		if i == 0:
			return None
		
		# Edge case - Delete 0 nodes
		if j == 0:
			return head
		
		# Invalid input
		if head is None or j < 0 or i < 0:
			return head

		# Helper references
		current = head
		previous = None
		
		# Traverse - Loop untill there are Nodes available in the LinkedList
		while current:
			
			'''skip (i - 1) nodes'''
			for _ in range(i - 1):
				if current is None:
					return head
				current = current.next
			previous = current
			current = current.next
			
			'''delete next j nodes'''
			for _ in range(j):
				if current is None:
					break
				next_node = current.next
				current = next_node
			
			'''Connect the `previous.next` to the `current`''' 
			previous.next = current
		
		# Loop ends
		
		return head
def Circular(head):
         if head==None:
          return True
         
         # Next of head
         node = head.next
         i = 0
     
          # This loop would stop in both cases (1) If
          # Circular (2) Not circular
         while((node is not None) and (node is not head)):
           i = i + 1
           node = node.next
     
           return(node==head)
		 
def is_Palindrome(s):
 
    rev = ''.join(reversed(s))
 
    # Checking if both string are 
    # equal or not
    if (s == rev):
        return True
    return False


def kth_to_Last(head, k):

	n = 0
	curr = head

	while curr:
		curr = curr.next
		n = n + 1

	# if number of nodes is more than or equal to K
	if n >= k:
		# return (n-k+1)th node from the beginning
		curr = head
		for i in range(n - k):
			curr = curr.next

	return curr

def reverse(self, head): 
  
    if head is None or head.next is None: 
        return head 

    rest = self.reverse(head.next) 
  
    head.next.next = head 
    head.next = None
  
    return rest 


 
def rotate_list(self, k): 
        if k == 0:  
            return 
          
        current = self.head 
          
        
        count = 1 
        while(count <k and current is not None): 
            current = current.next
            count += 1
     
        if current is None: 
            return
  
        kthNode = current  
      
  
        while(current.next is not None): 
            current = current.next
  
        current.next = self.head 
          
       
        self.head = kthNode.next
  
        kthNode.next = None
		

def swap_in_pairs(self): 
        temp = self.head 
         
        if temp is None: 
            return 
          
       
        while(temp is not None and temp.next is not None): 
 
            if(temp.data == temp.next.data): 
     
                temp = temp.next.next
            else: 

                temp.data, temp.next.data = temp.next.data, temp.data 
   
                temp = temp.next.next
