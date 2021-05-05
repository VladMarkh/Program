import unittest
from src.Program import Checker;

class TestCreateArray(unittest.TestCase):

    def test_array(self):
        self.assertEqual(Checker([['К', 'а', 'в', 'у', 'н'], [], [], [], []],4),"ၨჀ჈ᄌჴ")
        self.assertEqual(Checker([['U'], [], [], [], []],5),"Ʃ                        ")
        self.assertEqual(Checker([['富', '士', '山'], [], [], [], []],3), "𑍤````𐫁````𑕓``````````````")


    def test_types(self):
        self.assertRaises(TypeError, Checker,[],[] )
        self.assertRaises(TypeError, Checker,[],True)
        self.assertRaises(TypeError, Checker,[],"")
        self.assertRaises(TypeError, Checker,1,1 )
        self.assertRaises(TypeError, Checker,True,1)
        self.assertRaises(TypeError, Checker,"",1)

if __name__ == '__main__':
    unittest.main()
