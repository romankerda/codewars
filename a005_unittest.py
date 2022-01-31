import unittest
import a005_single_digit as a

class TestSingleDigit(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(a.single_digit(15), 4, "Should be 4")
        self.assertEqual(a.single_digit(157), 5, "Should be 5")
    def test_single_digit_2(self):
        self.assertEqual(a.single_digit(15), 4, "Should be 4")
        self.assertEqual(a.single_digit(157), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()