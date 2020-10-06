class Node(object):
    # Doubly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
	
class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def print_foward(self):
        for node in self.iter():
            print(node)

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
            
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val
 
    def append_item(self, data):
        # Append an item 
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1 #counting number of items


# Use items = doubly_linked_list()
# then items.append_item() append elements here any number of times
# and use print_forward() to print the output as below :
# items.print_foward() [#1]
# items.print_backward() [adding a new function #2]
# print("Number of items of the  Doubly linked list:",items.count)
