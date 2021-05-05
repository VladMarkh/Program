import unittest
from src.Program import AnCipherArray;

class TestCipherArray(unittest.TestCase):
    def test_array(self):
        self.assertEqual(AnCipherArray([['ᒂ', '\xa0', '\xa0', '\xa0', '\xa0'], ['ᓰ', '\xa0', '\xa0', '\xa0', '\xa0'], ['ᓺ', '\xa0', '\xa0', '\xa0', '\xa0'], ['ᕏ', '\xa0', '\xa0', '\xa0', '\xa0'], ['ᔱ', '\xa0', '\xa0', '\xa0', '\xa0']],5),[['К', ' ', ' ', ' ', ' '], ['а', ' ', ' ', ' ', ' '], ['в', ' ', ' ', ' ', ' '], ['у', ' ', ' ', ' ', ' '], ['н', ' ', ' ', ' ', ' ']])
        self.assertEqual(AnCipherArray([['ÿ', '`', '`', '`', '`'], ['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`']], 3),[['U', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])
        self.assertEqual(AnCipherArray([['래', '@', '@', '@', '@'], ['뇖', '@', '@', '@', '@'], ['룢', '@', '@', '@', '@'], ['@', '@', '@', '@', '@'], ['@', '@', '@', '@', '@']] , 2),[['富', ' ', ' ', ' ', ' '], ['士', ' ', ' ', ' ', ' '], ['山', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])


    def test_types(self):
        self.assertRaises(TypeError, AnCipherArray,[],[] )
        self.assertRaises(TypeError, AnCipherArray,[],True)
        self.assertRaises(TypeError, AnCipherArray,[],"")
        self.assertRaises(TypeError, AnCipherArray,1,1 )
        self.assertRaises(TypeError, AnCipherArray,True,1)
        self.assertRaises(TypeError, AnCipherArray,"",1)

if __name__ == '__main__':
    unittest.main()
