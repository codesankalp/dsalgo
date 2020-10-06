class Node(object):
    # Doubly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doubly_linked_list(object):
    # Use items = doubly_linked_list()
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        # items.append_item() append elements any number of times
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def prepend(self, data):
        # Insert a node in the beginning
        new_item = Node(data, None, None)
        new_item.next = self.head
        self.head = new_item
        if self.tail is None:
            self.tail = self.head
        self.count += 1

    def print_foward(self):
        #  to print the output use items.print_foward()
        for node in self.__iter():
            print(node)

    def size(self):
        return self.count

    def __iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def to_list(self):
        current_node = self.head
        arr = []
        while current_node is not None:
            arr.append(current_node.data)
            current_node = current_node.next
        return arr
