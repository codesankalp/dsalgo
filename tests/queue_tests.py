import unittest
from dsalgo.pyqueue import (
    Queue_from_linked_list as qfll,
    Queue_from_array as qfa)
import random


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.test_array = \
            [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
        self.ll_queue = qfll()
        self.arr_queue = qfa()

    def test_enqueue(self):
        for i in self.test_array:
            self.ll_queue.enqueue(i)
            self.arr_queue.enqueue(i)
        self.assertEqual(self.ll_queue.to_list(), self.test_array)
        self.assertEqual(self.arr_queue.to_list(), self.test_array)

    def test_dequeue(self):
        length = random.randint(0, len(self.test_array))
        self.test_enqueue()
        for _ in range(length):
            self.ll_queue.dequeue()
            self.arr_queue.dequeue()
        self.assertEqual(self.ll_queue.to_list(), self.test_array[length:])
        self.assertEqual(self.arr_queue.to_list(), self.test_array[length:])

    def test_size(self):
        self.test_enqueue()
        self.assertEqual(self.ll_queue.size(), len(self.test_array))
        self.assertEqual(self.arr_queue.size(), len(self.test_array))

    def test_empty(self):
        self.test_enqueue()
        self.assertEqual(self.ll_queue.is_empty(), self.test_array == [])
        self.assertEqual(self.arr_queue.is_empty(), self.test_array == [])


if __name__ == '__main__':
    unittest.main()
