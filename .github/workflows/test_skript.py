import unittest
from skript import scitani

class TestScitani(unittest.TestCase):
    def test_scitani(self):
        self.assertEqual(scitani(3, 4), 7)
        self.assertEqual(scitani(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
