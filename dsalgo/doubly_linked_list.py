class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
    
class DoublyList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head

    def add_node(self, val):
        current = self.head
        while current.next != None:
            current = current.next
        n_node = Node(val)
        current.next = n_node
        n_node.prev = current
        self.tail = n_node

    def del_node(self, val):
        if self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head.next
            while current.value != val:
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

    def show(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next


lista = DoublyList(10)
lista.add_node(20)
lista.add_node(30)
lista.add_node(40)
lista.show()
