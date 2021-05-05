import unittest
from src.Program import CipherArray;

class TestCipherArray(unittest.TestCase):
    def test_array(self):
        self.assertEqual(CipherArray([['К', 'а', 'в', 'у', 'н'],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' ']],3),"౎````ಐ````ಖ````೉````ಷ````")
        self.assertEqual(CipherArray([['U', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' ']],4),"Ŕ")
        self.assertEqual(CipherArray([['富', '士', '山', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' '],
                                      [' ', ' ', ' ', ' ', ' ']],2),"래@@@@뇖@@@@룢@@@@@@@@@@@@@@")


    def test_types(self):
        self.assertRaises(TypeError, CipherArray,[],[] )
        self.assertRaises(TypeError, CipherArray,[],True)
        self.assertRaises(TypeError, CipherArray,[],"")
        self.assertRaises(TypeError, CipherArray,1,1 )
        self.assertRaises(TypeError, CipherArray,True,1)
        self.assertRaises(TypeError, CipherArray,"",1)

if __name__ == '__main__':
    unittest.main()
