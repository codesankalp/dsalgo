import unittest
from dsalgo.search import Search
import random


class Test_seacrch(unittest.TestCase):
    def setUp(self):
        self.test_array = [i for i in range(random.randint(0, 100))]
        self.to_search = random.choice(self.test_array)
        self.search = Search(self.test_array, self.to_search)

    def test_linear_search(self):
        self.answer = self.test_array.index(self.to_search)
        self.assertEqual(self.answer, self.search.linear_search())

    def test_binary_search(self):
        self.answer = sorted(self.test_array).index(self.to_search)
        self.assertEqual(self.answer, self.search.binary_search())

    def test_jump_search(self):
        self.answer = sorted(self.test_array).index(self.to_search)
        self.assertEqual(self.answer, self.search.jump_search())

    def test_interpolation_search(self):
        self.answer = sorted(self.test_array).index(self.to_search)
        self.assertEqual(self.answer, self.search.interpolation_search())

    def test_fibonacci_search(self):
        self.answer = sorted(self.test_array).index(self.to_search)
        self.assertEqual(self.answer, self.search.fibonacci_search())

    def test_exponential_search(self):
        self.answer = sorted(self.test_array).index(self.to_search)
        self.assertEqual(self.answer, self.search.exponential_search())
    
    def test_recursive_search(self):
        self.answer = self.test_array.index(self.to_search)
        self.assertEqual(self.answer, self.search.recursive_search())
