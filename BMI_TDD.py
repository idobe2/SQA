import unittest
from BMI_calc import test_input


class BMI_TDD(unittest.TestCase):
    def test_num(self):
        ex_h, ex_w = 0, 0
        self.assertEqual((test_input(0, 0)), (ex_h, ex_w))
        self.assertEqual((test_input(-175, 80)), (ex_h, ex_w))
        self.assertEqual((test_input(165, -70)), (ex_h, ex_w))
        self.assertEqual((test_input(-169, -72)), (ex_h, ex_w))
        self.assertEqual((test_input(179, 85)), (179, 85))

    def test_type(self):
        with self.assertRaises(TypeError):
            res_h, res_w = (test_input('T', 'd'))
        with self.assertRaises(TypeError):
            res_h, res_w = (test_input(':', '/'))
        with self.assertRaises(TypeError):
            res_h, res_w = (test_input('12ab', 'cd34'))

    if __name__ == '__main__':
        unittest.main()
