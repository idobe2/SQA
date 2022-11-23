import unittest
from Text_Encryption import test_input


class BMI_TDD(unittest.TestCase):
    def test_num(self):
        ex_res = False
        self.assertEqual((test_input("AbCd1234")), False)
        self.assertEqual((test_input("5678EfGh")), False)
        self.assertEqual((test_input("a@1b#4c$5")), False)

    def test_type(self):
        with self.assertRaises(TypeError):
            res = (test_input(0))
        with self.assertRaises(TypeError):
            res = (test_input(100))
        with self.assertRaises(TypeError):
            res = (test_input(123.456))

    if __name__ == '__main__':
        unittest.main()
