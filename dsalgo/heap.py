class Heap:

    def __init__(self, type='min'):
        """
        Create a Heap object
        Args :
            type : type of Heap ('min' or 'max') default-'min'
        """
        self.size = None
        self.Heap = [0]
        self.type = type

    __all__ = ['parent', 'leftChild', 'rightChild', 'display',
               'isLeaf', 'root', 'insert', 'delete', 'to_list']

    def parent(self, pos):
        """
        returns parent element's position
        Args:
            pos : index of element
        Return :
            int : index of parent element
        """
        if((pos - 1) // 2) >= 0:

            return (pos - 1) // 2
        else:
            return 0

    def leftChild(self, pos):
        """
        returns parent element's position
        Args:
            pos : index of element
        return :
            int : index of its left child element
        """
        return (2 * pos) + 1

    def rightChild(self, pos):
        """
        returns parent element's position
        Args:
            pos(int) : index of element
        return :
            int : index of its right child element
        """
        return (2 * pos) + 2

    def display(self):
        """
        display heap elements
        """
        for i in range(0, ((self.size+1) // 2)):
            print("Parent : " + str(self.Heap[i]), end=" ")
            if self.size >= self.leftChild(i):
                print("Left Child : " + str(self.Heap[2 * i+1]), end=" ")
                if self.size >= self.rightChild(i):
                    print("Right Child : " + str(self.Heap[2 * i+2]))
        print()

    def isLeaf(self, pos):
        """
        checks the index is leaf or not
        Returns :
            boolean : True or False
        """
        if pos >= ((self.size+1)//2) and pos <= self.size:
            return True
        return False

    def root(self):
        """
        returns root element of the Heap
        """
        return self.Heap[0]

    def insert(self, item):
        """
        insert element in Heap
        Args :
            item : item to be inserted
        """
        if self.size is None:
            self.Heap[0] = item
            self.size = 0

        else:
            self.size += 1
            self.Heap.append(item)
            current = self.size

            if self.type == 'max':
                while (self.Heap[current] > self.Heap[self.parent(current)]):
                    self.swap(current, self.parent(current))
                    current = self.parent(current)
            elif self.type == 'min':
                while self.Heap[current] < self.Heap[self.parent(current)]:
                    self.swap(current, self.parent(current))
                    current = self.parent(current)
            else:
                print('Non Supported Type :'+type +
                      'is not supported. Type can be "min" or "max"')

    def swap(self, fpos, spos):
        """
        swap two element's position in Heap
        Args :
            fpos : first position
            spos : second position
        """
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    def delete(self, pos):
        """
        Delete an elemnet from Heap
        Args :
            pos : index of element to be deleted
        """
        self.Heap[pos] = self.Heap[self.size]
        self.Heap = self.Heap[:-1]
        self.size -= 1

        if self.type == 'max':
            if self.Heap[pos] > self.Heap[self.parent(pos)]:
                while(self.Heap[pos] > self.Heap[self.parent(pos)]):
                    self.swap(pos, self.parent(pos))
                    pos = self.parent(pos)
            while(self.rightChild(pos) <= self.size):
                if(self.Heap[pos] >= self.leftChild(pos) and
                        self.Heap[pos] >= self.rightChild(pos)):
                    return
                if(self.Heap[self.rightChild(pos)] <=
                        self.Heap[self.leftChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    pos = self.leftChild(pos)
                else:
                    self.swap(pos, self.rightChild(pos))
                    pos = self.rightChild(pos)

        elif self.type == 'min':
            if self.Heap[pos] < self.Heap[self.parent(pos)]:
                while(self.Heap[pos] < self.Heap[self.parent(pos)]):
                    self.swap(pos, self.parent(pos))
                    pos = self.parent(pos)
            while(self.rightChild(pos) <= self.size):
                if(self.Heap[pos] <= self.leftChild(pos) and self.Heap[pos] <=
                        self.rightChild(pos)):
                    return
                if(self.Heap[self.rightChild(pos)] >=
                        self.Heap[self.leftChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    pos = self.leftChild(pos)
                else:
                    self.swap(pos, self.rightChild(pos))
                    pos = self.rightChild(pos)

        else:
            print('Non Supported Type :'+type +
                  'is not supported. Type can be "min" or "max"')

    def to_list(self):
        """
        returns python list of Heap elements
        """
        return self.Heap
