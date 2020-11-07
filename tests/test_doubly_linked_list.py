import unittest
from dsalgo.doubly_linked_list import (
    doubly_linked_list as dll)
import random


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.test_array = \
            [random.randint(-100, 100) for _ in range(random.randint(0, 100))]

    def test_append(self):
        self.dll = dll()
        for i in self.test_array:
            self.dll.append(i)
        self.assertEqual(self.dll.to_list(), self.test_array)

    def test_prepend(self):
        self.dll = dll()
        for i in self.test_array:
            self.dll.prepend(i)
        self.assertEqual(self.dll.to_list(), self.test_array[::-1])

    def test_size(self):
        self.test_append()
        self.assertEqual(self.dll.size(), len(self.test_array))
