import unittest
from src.Program import Mover;

class TestMover(unittest.TestCase):
    def test_mover(self):
        self.assertEqual(Mover([['ၨ', 'Ⴠ', '\u10c8', 'ᄌ', 'ჴ'],
                                ['\x80', '\x80', '\x80', '\x80', '\x80'],
                                ['\x80', '\x80', '\x80', '\x80', '\x80'],
                                ['\x80', '\x80', '\x80', '\x80', '\x80'],
                                ['\x80', '\x80', '\x80', '\x80', '\x80']]),
                                "ၨჀ჈ᄌჴ")

        self.assertEqual(Mover([['ª', '@', '@', '@', '@'],
                                ['@', '@', '@', '@', '@'],
                                ['@', '@', '@', '@', '@'],
                                ['@', '@', '@', '@', '@'],
                                ['@', '@', '@', '@', '@']]),
                                'ª@@@@@@@@@@@@@@@@@@@@@@@@')

        self.assertEqual(Mover([['\U0001cafc', '𛲗', '\U0001ce35', '\xa0', '\xa0'],
                                ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0'],
                                ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0'],
                                ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0'],
                                ['\xa0', '\xa0', '\xa0', '\xa0', '\xa0']]),
                                '𜫼    𛲗    𜸵              ')

    def test_types(self):
        self.assertRaises(TypeError, Mover, 10)
        self.assertRaises(TypeError, Mover, True)
        self.assertRaises(TypeError, Mover, '')

if __name__ == '__main__':
    unittest.main()
