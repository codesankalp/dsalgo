import unittest
from dsalgo.string_algo import Strings

class TestEncodeDecode(unittest.TestCase):

    def setUp(self):
        self.st = Strings()

    def test_encode(self):
        self.assertEqual("3:Are3:you5:there", self.st.encode("Are you there"))
    
    def test_decode(self):
        self.assertEqual(['Are', 'you', 'there'],
                         self.st.decode("3:Are3:you5:there"))

    def test_longest_palindrome(self):
        self.assertAlmostEqual(
            "asdadsa", self.st.longest_palindrome("dasdasdasdasdasdadsa"))

    def test_repeat_substring(self):
        self.assertEqual(True, self.st.repeat_substring("abab"))

    def test_roman(self):
        self.assertAlmostEqual(9, self.st.roman_to_int("IX"))

if __name__ == "__main__":
    unittest.main()
