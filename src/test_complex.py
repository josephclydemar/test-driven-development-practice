import unittest
from complex import Complex

class TestComplex(unittest.TestCase):
    def test_complex_str_return(self):
        self.assertEqual(Complex(2, 2).__str__(), '2+2i')
        self.assertEqual(Complex(1, 2).__str__(), '1+2i')
        self.assertEqual(Complex(2, 1).__str__(), '2+i')
        self.assertEqual(Complex(1, 1).__str__(), '1+i')

        self.assertEqual(Complex(0, 2).__str__(), '+2i')
        self.assertEqual(Complex(2, 0).__str__(), '2')


        self.assertEqual(Complex(0, 1).__str__(), '+i')
        self.assertEqual(Complex(1, 0).__str__(), '1')
        self.assertEqual(Complex(0, 0).__str__(), '')


        self.assertEqual(Complex(0, -1).__str__(), '-i')
        self.assertEqual(Complex(-1, 0).__str__(), '-1')

        self.assertEqual(Complex(0, -2).__str__(), '-2i')
        self.assertEqual(Complex(-2, 0).__str__(), '-2')

        self.assertEqual(Complex(-2, -2).__str__(), '-2-2i')
        self.assertEqual(Complex(-1, 2).__str__(), '-1+2i')
        self.assertEqual(Complex(2, -1).__str__(), '2-i')
        self.assertEqual(Complex(-1, -1).__str__(), '-1-i')

    



    # * Addition tests
    def test_complex_add_return_type(self):
        self.assertEqual(type(Complex(1, 1) + Complex(1, 1)), Complex)
        self.assertEqual(type(Complex(0, 1) + Complex(0, 1)), Complex)
        self.assertEqual(type(Complex(1, 0) + Complex(1, 0)), Complex)
        self.assertEqual(type(Complex(0, 0) + Complex(0, 0)), Complex)
        self.assertEqual(type(Complex(-1, 0) + Complex(-1, 0)), Complex)
        self.assertEqual(type(Complex(0, -1) + Complex(0, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) + Complex(-1, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) + Complex(-1, -1)), Complex)

    def test_complex_add_return_value(self):
        test_case1 = (Complex(1, 1) + Complex(1, 1)).get_value()
        test_case2 = (Complex(0, 1) + Complex(0, 1)).get_value()
        test_case3 = (Complex(1, 0) + Complex(1, 0)).get_value()
        test_case4 = (Complex(0, 0) + Complex(0, 0)).get_value()
        test_case5 = (Complex(-1, 0) + Complex(-1, 0)).get_value()
        test_case6 = (Complex(0, -1) + Complex(0, -1)).get_value()
        test_case7 = (Complex(-1, -1) + Complex(-1, -1)).get_value()
        test_case8 = (Complex(1, -1) + Complex(1, -1)).get_value()

        expected_result1 = (2, 2)
        expected_result2 = (0, 2)
        expected_result3 = (2, 0)
        expected_result4 = (0, 0)
        expected_result5 = (-2, 0)
        expected_result6 = (0, -2) 
        expected_result7 = (-2, -2)
        expected_result8 = (2, -2)

        self.assertEqual(test_case1[0], expected_result1[0])
        self.assertEqual(test_case1[1], expected_result1[1])

        self.assertEqual(test_case2[0], expected_result2[0])
        self.assertEqual(test_case2[1], expected_result2[1])

        self.assertEqual(test_case3[0], expected_result3[0])
        self.assertEqual(test_case3[1], expected_result3[1])

        self.assertEqual(test_case4[0], expected_result4[0])
        self.assertEqual(test_case4[1], expected_result4[1])

        self.assertEqual(test_case5[0], expected_result5[0])
        self.assertEqual(test_case5[1], expected_result5[1])

        self.assertEqual(test_case6[0], expected_result6[0])
        self.assertEqual(test_case6[1], expected_result6[1])

        self.assertEqual(test_case7[0], expected_result7[0])
        self.assertEqual(test_case7[1], expected_result7[1])

        self.assertEqual(test_case8[0], expected_result8[0])
        self.assertEqual(test_case8[1], expected_result8[1])

    


    # * Subtraction tests
    def test_complex_sub_return_type(self):
        self.assertEqual(type(Complex(1, 1) - Complex(1, 1)), Complex)
        self.assertEqual(type(Complex(0, 1) - Complex(0, 1)), Complex)
        self.assertEqual(type(Complex(1, 0) - Complex(1, 0)), Complex)
        self.assertEqual(type(Complex(0, 0) - Complex(0, 0)), Complex)
        self.assertEqual(type(Complex(-1, 0) - Complex(-1, 0)), Complex)
        self.assertEqual(type(Complex(0, -1) - Complex(0, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) - Complex(-1, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) - Complex(-1, -1)), Complex)

    def test_complex_sub_return_value(self):
        test_case1 = (Complex(1, 1) - Complex(1, 1)).get_value()
        test_case2 = (Complex(0, 2) - Complex(0, 1)).get_value()
        test_case3 = (Complex(0, 0) - Complex(1, 0)).get_value()
        test_case4 = (Complex(0, 0) - Complex(0, 0)).get_value()
        test_case5 = (Complex(-1, 0) - Complex(1, 0)).get_value()
        test_case6 = (Complex(0, -1) - Complex(0, -1)).get_value()
        test_case7 = (Complex(0, -1) - Complex(-1, -1)).get_value()
        test_case8 = (Complex(-1, -1) - Complex(1, -1)).get_value()

        expected_result1 = (0, 0)
        expected_result2 = (0, 1)
        expected_result3 = (-1, 0)
        expected_result4 = (0, 0)
        expected_result5 = (-2, 0)
        expected_result6 = (0, 0) 
        expected_result7 = (1, 0)
        expected_result8 = (-2, 0)

        self.assertEqual(test_case1[0], expected_result1[0])
        self.assertEqual(test_case1[1], expected_result1[1])

        self.assertEqual(test_case2[0], expected_result2[0])
        self.assertEqual(test_case2[1], expected_result2[1])

        self.assertEqual(test_case3[0], expected_result3[0])
        self.assertEqual(test_case3[1], expected_result3[1])

        self.assertEqual(test_case4[0], expected_result4[0])
        self.assertEqual(test_case4[1], expected_result4[1])

        self.assertEqual(test_case5[0], expected_result5[0])
        self.assertEqual(test_case5[1], expected_result5[1])

        self.assertEqual(test_case6[0], expected_result6[0])
        self.assertEqual(test_case6[1], expected_result6[1])

        self.assertEqual(test_case7[0], expected_result7[0])
        self.assertEqual(test_case7[1], expected_result7[1])

        self.assertEqual(test_case8[0], expected_result8[0])
        self.assertEqual(test_case8[1], expected_result8[1])

    


    # * Multiplication tests
    def test_complex_mul_return_type(self):
        self.assertEqual(type(Complex(1, 1) * Complex(1, 1)), Complex)
        self.assertEqual(type(Complex(0, 1) * Complex(0, 1)), Complex)
        self.assertEqual(type(Complex(1, 0) * Complex(1, 0)), Complex)
        self.assertEqual(type(Complex(0, 0) * Complex(0, 0)), Complex)
        self.assertEqual(type(Complex(-1, 0) * Complex(-1, 0)), Complex)
        self.assertEqual(type(Complex(0, -1) * Complex(0, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) * Complex(-1, -1)), Complex)
        self.assertEqual(type(Complex(-1, -1) * Complex(-1, -1)), Complex)

    def test_complex_mul_return_value(self):
        test_case1 = (Complex(1, 1) * Complex(1, 1)).get_value() # (1*1 - 1*1) + (1*1 + 1*1)
        test_case2 = (Complex(0, 1) * Complex(0, 1)).get_value()
        test_case3 = (Complex(1, 0) * Complex(1, 0)).get_value()
        test_case4 = (Complex(0, 0) * Complex(0, 0)).get_value()
        test_case5 = (Complex(-1, 0) * Complex(-1, 0)).get_value()
        test_case6 = (Complex(0, -1) * Complex(0, -1)).get_value()
        test_case7 = (Complex(-1, -1) * Complex(-1, -1)).get_value()
        test_case8 = (Complex(1, -1) * Complex(1, -1)).get_value()

        expected_result1 = (0, 2)
        expected_result2 = (-1, 0)
        expected_result3 = (1, 0)
        expected_result4 = (0, 0)
        expected_result5 = (1, 0)
        expected_result6 = (-1, 0) 
        expected_result7 = (0, 2)
        expected_result8 = (0, -2)

        self.assertEqual(test_case1[0], expected_result1[0])
        self.assertEqual(test_case1[1], expected_result1[1])

        self.assertEqual(test_case2[0], expected_result2[0])
        self.assertEqual(test_case2[1], expected_result2[1])

        self.assertEqual(test_case3[0], expected_result3[0])
        self.assertEqual(test_case3[1], expected_result3[1])

        self.assertEqual(test_case4[0], expected_result4[0])
        self.assertEqual(test_case4[1], expected_result4[1])

        self.assertEqual(test_case5[0], expected_result5[0])
        self.assertEqual(test_case5[1], expected_result5[1])

        self.assertEqual(test_case6[0], expected_result6[0])
        self.assertEqual(test_case6[1], expected_result6[1])

        self.assertEqual(test_case7[0], expected_result7[0])
        self.assertEqual(test_case7[1], expected_result7[1])

        self.assertEqual(test_case8[0], expected_result8[0])
        self.assertEqual(test_case8[1], expected_result8[1])


        



if __name__ == '__main__':
    unittest.main()