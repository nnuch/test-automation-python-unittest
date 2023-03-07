import mycalculator as mc
import unittest


class TestClass(unittest.TestCase):

    def test_add(self):
        #test add function

        self.assertEqual(mc.add(5, 15), 20)
        self.assertEqual(mc.add(10, 20), 30)
        self.assertEqual(mc.add(20, 100), 120)
        self.assertEqual(mc.add(-20, 10), -10)


    def test_substract(self):
        #test substract function

        self.assertEqual(mc.substract(20, 15), 5)
        self.assertEqual(mc.substract(-10, -20), 10)


    def test_multiply(self):
        #test multiply function

        result = mc.multiply(20, 5)
        self.assertEqual(result, 100)


    def test_divide(self):
        #test divide function

        result = mc.multiply(10, 2)
        self.assertEqual(result, 20)


    def test_divide_not_by_zero(self):
        #test a zero number, it should return an error
        
        self.assertRaises(ValueError, mc.divide, 20, 0)


if __name__ == '__main__':
    unittest.main()