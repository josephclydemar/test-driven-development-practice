import sys
import os

parent_dir = os.path.dirname(os.path.realpath('src'))

# Add the parent directory to sys.path
sys.path.append(os.path.join(parent_dir, 'src'))

from imag import Imag


import unittest

class TestImag(unittest.TestCase):
    def test_imag_get_value(self):
        self.assertEqual(Imag(0).get_value(), 0)
        self.assertEqual(Imag(-1).get_value(), -1)
        self.assertEqual(Imag(1).get_value(), 1)
        self.assertEqual(Imag(4).get_value(), 4)
        self.assertEqual(Imag(-4).get_value(), -4)
        
    def test_imag_str_return(self):
        self.assertEqual(Imag(2).__str__(), '+2i')
        self.assertEqual(Imag(-2).__str__(), '-2i')
        self.assertEqual(Imag(1).__str__(), '+i')
        self.assertEqual(Imag(-1).__str__(), '-i')
        self.assertEqual(Imag(0).__str__(), '')


    # * Addition tests
    def test_imag_add_return_type(self):
        self.assertEqual(type(Imag(2) + Imag(2)), Imag)
        self.assertEqual(type(Imag(-2) + Imag(-2)), Imag)
        self.assertEqual(type(Imag(1) + Imag(1)), Imag)
        self.assertEqual(type(Imag(-1) + Imag(-1)), Imag)
        self.assertEqual(type(Imag(0) + Imag(0)), Imag)

    def test_imag_add_return_value(self):
        self.assertEqual((Imag(2) + Imag(2)).get_value(), 4)
        self.assertEqual((Imag(-2) + Imag(-2)).get_value(), -4)
        self.assertEqual((Imag(1) + Imag(1)).get_value(), 2)
        self.assertEqual((Imag(-1) + Imag(-1)).get_value(), -2)
        self.assertEqual((Imag(0) + Imag(0)).get_value(), 0)

    
    # Subtraction tests
    def test_imag_sub_return_type(self):
        self.assertEqual(type(Imag(2) - Imag(2)), Imag)
        self.assertEqual(type(Imag(-2) - Imag(-2)), Imag)
        self.assertEqual(type(Imag(1) - Imag(1)), Imag)
        self.assertEqual(type(Imag(-1) - Imag(-1)), Imag)
        self.assertEqual(type(Imag(0) - Imag(0)), Imag)

    def test_imag_sub_return_value(self):
        self.assertEqual((Imag(2) - Imag(2)).get_value(), 0)
        self.assertEqual((Imag(2) - Imag(-2)).get_value(), 4)
        self.assertEqual((Imag(1) - Imag(-1)).get_value(), 2)
        self.assertEqual((Imag(-1) - Imag(1)).get_value(), -2)
        self.assertEqual((Imag(0) - Imag(0)).get_value(), 0)


    # * Multiplication tests
    def test_imag_mul_return_type(self):
        self.assertEqual(type(Imag(2) * Imag(2)), Imag)
        self.assertEqual(type(Imag(-2) * Imag(-2)), Imag)
        self.assertEqual(type(Imag(1) * Imag(1)), Imag)
        self.assertEqual(type(Imag(-1) * Imag(-1)), Imag)
        self.assertEqual(type(Imag(0) * Imag(0)), Imag)

    def test_imag_mul_return_value(self):
        self.assertEqual((Imag(2) * Imag(2)).get_value(), 4)
        self.assertEqual((Imag(2) * Imag(-2)).get_value(), -4)
        self.assertEqual((Imag(1) * Imag(-1)).get_value(), -1)
        self.assertEqual((Imag(1) * Imag(1)).get_value(), 1)
        self.assertEqual((Imag(0) * Imag(1)).get_value(), 0)



if __name__ == '__main__':
    unittest.main()