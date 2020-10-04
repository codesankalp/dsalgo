import unittest

from dsalgo.dmath import dmath


class TestDmath(unittest.TestCase):
    def setUp(self):
        self.dm = dmath()

    def test_gcd(self):
        # case 1 a=0 b=0
        self.assertEqual(self.dm.gcd(0, 0), 0)
        # case 1 a=0 b=9
        self.assertEqual(self.dm.gcd(0, 9), 9)
        # case 1 a=2 b=0
        self.assertEqual(self.dm.gcd(2, 0), 2)
        # case 1 a=270 b=192
        self.assertEqual(self.dm.gcd(270, 192), 6)
        # case 1 a=192 b=270
        self.assertEqual(self.dm.gcd(192, 270), 6)

    def test_list_gcd(self):
        self.assertEqual(self.dm.list_gcd([2, 4, 6, 8]), 2)

    def test_lcm(self):
        self.assertEqual(self.dm.lcm(18, 9), 18)

    def test_list_lcm(self):
        self.assertEqual(self.dm.list_lcm([9, 18, 34, 16, 17]), 2448)

    def test_is_prime(self):
        self.assertEqual(self.dm.is_prime(17), True)
        self.assertEqual(self.dm.is_prime(38), False)

    def test_next_prime(self):
        self.assertEqual(self.dm.next_prime(18), 19)
        self.assertEqual(self.dm.next_prime(20), 23)

    def prev_prime(self):
        self.assertEqual(self.dm.prev_prime(18), 17)
        self.assertEqual(self.dm.prev_prime(20), 19)

    def test_list_prime(self):
        self.assertEqual(self.dm.list_prime([3, 7, 9, 12, 14]),
                         [3, 7])

    def test_series_prime(self):
        # case 1 start == 2 end == none reverse == false count == default
        self.assertEqual(self.dm.series_prime(),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

        # case 2 start == 2 end == 30 reverse == false count = 5
        self.assertEqual(self.dm.series_prime(start=2, end=30, count=5),
                         [2, 3, 5, 7, 11])

        # case 3 start == 31 end == none reverse == true count == default
        self.assertEqual(self.dm.series_prime(start=31, reverse=True),
                         [31, 29, 23, 19, 17, 13, 11, 7, 5, 3])

        # case 4 start == 31 end == 2 reverse == true count = 5
        self.assertEqual(self.dm.series_prime(start=31, reverse=True, count=5),
                         [31, 29, 23, 19, 17])
