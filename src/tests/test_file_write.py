import unittest
from src.Program import FileWrite;

class TestCreateArray(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, FileWrite, 10)
        self.assertRaises(TypeError, FileWrite, True)
        self.assertRaises(TypeError, FileWrite, [])

if __name__ == '__main__':
    unittest.main()
