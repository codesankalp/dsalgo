import unittest
from dsalgo.heap import Heap
import random


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.test_array = \
            [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
        self.minHeap = Heap()
        self.maxHeap = Heap('max')

    def test_root(self):
        for i in self.test_array:
            self.minHeap.insert(i)
            self.maxHeap.insert(i)
        self.assertEqual(self.minHeap.root(), min(self.minHeap.to_list()))
        self.assertEqual(self.maxHeap.root(), max(self.maxHeap.to_list()))


if __name__ == '__main__':
    unittest.main()
