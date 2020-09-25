import unittest
from dsalgo.Search import Search
array = [2, 4, 6, 8, 10, 1]

class TestSearch(unittest.TestCase):

    def test_linear(self):
        self.assertEqual(Search(array, 'linear', 10), 4)
        self.assertEqual(Search(array, 'linear', 12), -1)

    def test_binary(self):
        self.assertEqual(Search(array, 'binary', 10), 4)
        self.assertEqual(Search(array, 'binary', 12), -1)

  

if __name__ == '__main__':
    unittest.main()
