import unittest
from src.Program import CreateArray;

class TestCreateArray(unittest.TestCase):
    def test_array(self):
        self.assertEqual(CreateArray("Кавун"),[['К', 'а', 'в', 'у', 'н'], [], [], [], []])
        self.assertEqual(CreateArray("U"),[['U'], [], [], [], []])
        self.assertEqual(CreateArray("富士山"), [['富', '士', '山'], [], [], [], []])
    def test_value(self):
        self.assertRaises(ValueError,CreateArray,"Жебракують філософи при ґанку церкви в Гадячі, ще й шатро їхнє п’яне знаємо.")
        self.assertRaises(ValueError, CreateArray,"")
    def test_types(self):
        self.assertRaises(TypeError, CreateArray, 10)
        self.assertRaises(TypeError, CreateArray, True)
        self.assertRaises(TypeError, CreateArray, [])

if __name__ == '__main__':
    unittest.main()
