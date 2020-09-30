from collections import deque

class Queue():
    def __init__(self, max_size = 10):
        self._queue = deque(maxlen=max_size)
    
    def enqueue(self, item):
        self._queue.append(item)
    
    def dequeue(self):
        return self._queue.pop()

    def display(self):
        print("QUEUE: --> ")
        for element in self._queue:
            print(element,end=" ")

def main():
    queue = Queue()
    queue.enqueue('Dog')
    queue.enqueue('Cat')
    queue.enqueue('Horse')
    queue.enqueue('Fox')
    queue.display()
    print("\n Popped element = ", queue.dequeue())
    queue.display()
if __name__ == '__main__':
    main()