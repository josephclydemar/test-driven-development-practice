import sys
import os
parent_dir = os.path.dirname(os.path.realpath('src'))
sys.path.append(os.path.join(parent_dir, 'src')) # * Add the parent directory to sys.path
import unittest
from real import Real

class TestReal(unittest.TestCase):
    def test_real_get_value(self):
        self.assertEqual(Real(0).get_value(), 0)
        self.assertEqual(Real(-1).get_value(), -1)
        self.assertEqual(Real(1).get_value(), 1)
        self.assertEqual(Real(4).get_value(), 4)
        self.assertEqual(Real(-4).get_value(), -4)
        
    def test_real_str_return(self):
        self.assertEqual(Real(2).__str__(), '2')
        self.assertEqual(Real(-2).__str__(), '-2')
        self.assertEqual(Real(1).__str__(), '1')
        self.assertEqual(Real(-1).__str__(), '-1')
        self.assertEqual(Real(0).__str__(), '')


    def test_real_add_return_type(self):
        self.assertEqual(type(Real(2) + Real(2)), Real)
        self.assertEqual(type(Real(-2) + Real(-2)), Real)
        self.assertEqual(type(Real(1) + Real(1)), Real)
        self.assertEqual(type(Real(-1) + Real(-1)), Real)
        self.assertEqual(type(Real(0) + Real(0)), Real)

    def test_real_add_return_value(self):
        self.assertEqual((Real(2) + Real(2)).get_value(), 4)
        self.assertEqual((Real(-2) + Real(-2)).get_value(), -4)
        self.assertEqual((Real(1) + Real(1)).get_value(), 2)
        self.assertEqual((Real(-1) + Real(-1)).get_value(), -2)
        self.assertEqual((Real(0) + Real(0)).get_value(), 0)
    

    def test_real_sub_return_type(self):
        self.assertEqual(type(Real(2) - Real(2)), Real)
        self.assertEqual(type(Real(-2) - Real(-2)), Real)
        self.assertEqual(type(Real(1) - Real(1)), Real)
        self.assertEqual(type(Real(-1) - Real(-1)), Real)
        self.assertEqual(type(Real(0) - Real(0)), Real)

    def test_real_sub_return_value(self):
        self.assertEqual((Real(2) - Real(2)).get_value(), 0)
        self.assertEqual((Real(2) - Real(-2)).get_value(), 4)
        self.assertEqual((Real(1) - Real(-1)).get_value(), 2)
        self.assertEqual((Real(-1) - Real(1)).get_value(), -2)
        self.assertEqual((Real(0) - Real(0)).get_value(), 0)


    
    # * Multiplication tests
    def test_real_mul_return_type(self):
        self.assertEqual(type(Real(2) * Real(2)), Real)
        self.assertEqual(type(Real(-2) * Real(-2)), Real)
        self.assertEqual(type(Real(1) * Real(1)), Real)
        self.assertEqual(type(Real(-1) * Real(-1)), Real)
        self.assertEqual(type(Real(0) * Real(0)), Real)

    def test_real_mul_return_value(self):
        self.assertEqual((Real(2) * Real(2)).get_value(), 4)
        self.assertEqual((Real(2) * Real(-2)).get_value(), -4)
        self.assertEqual((Real(1) * Real(-1)).get_value(), -1)
        self.assertEqual((Real(1) * Real(1)).get_value(), 1)
        self.assertEqual((Real(0) * Real(1)).get_value(), 0)


if __name__ == '__main__':
    unittest.main()