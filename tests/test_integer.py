import integer

import unittest


class TestAbsZ(unittest.TestCase):

    def test_zero(self):
        zero = [0, 1, [0]]
        expect = [1, [0]]
        result = integer.ABS_Z_N(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [0, 3, [3, 4, 2]]
        expect = [3, [3, 4, 2]]
        result = integer.ABS_Z_N(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [1, 3, [3, 4, 2]]
        expect = [3, [3, 4, 2]]
        result = integer.ABS_Z_N(number)
        self.assertEqual(result, expect)


class TestPozZ(unittest.TestCase):

    def test_zero(self):
        zero = [0, 1, [0]]
        expect = 0
        result = integer.POZ_Z_D(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [0, 3, [3, 4, 2]]
        expect = 2
        result = integer.POZ_Z_D(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [1, 3, [3, 4, 2]]
        expect = 1
        result = integer.POZ_Z_D(number)
        self.assertEqual(result, expect)


class TestMulZM(unittest.TestCase):

    def test_zero(self):
        zero = [0, 1, [0]]
        expect = [1, 1, [0]]
        result = integer.MUL_ZM_Z(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [0, 3, [3, 4, 2]]
        expect = [1, 3, [3, 4, 2]]
        result = integer.MUL_ZM_Z(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [1, 3, [3, 4, 2]]
        expect = [0, 3, [3, 4, 2]]
        result = integer.MUL_ZM_Z(number)
        self.assertEqual(result, expect)


class TestMulZZ(unittest.TestCase):

    def test_zeros(self):
        zero = [0, 1, [0]]
        expect = zero
        result = integer.MUL_ZZ_Z(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [0, 3, [3, 5, 2]]
        zero = [0, 1, [0]]
        expect = zero
        result = integer.MUL_ZZ_Z(number, zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [0, 2, [4, 2]]
        number2 = [0, 3, [5, 3, 2]]
        expect = [0, 4, [0, 4, 6, 5]]
        result = integer.MUL_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negative(self):
        number1 = [0, 2, [4, 2]]
        number2 = [1, 3, [5, 3, 2]]
        expect = [1, 4, [0, 4, 6, 5]]
        result = integer.MUL_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negatives(self):
        number1 = [1, 2, [4, 2]]
        number2 = [1, 3, [5, 3, 2]]
        expect = [0, 4, [0, 4, 6, 5]]
        result = integer.MUL_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)


class TestSubZZ(unittest.TestCase):

    def test_zeros(self):
        zero = [0, 1, [0]]
        expect = zero
        result = integer.SUB_ZZ_Z(zero, zero)
        self.assertEqual(result, expect)

    def test_equal_positive(self):
        number = [0, 3, [5, 2, 6]]
        expect = [1, 1, [0]]
        result = integer.SUB_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_equal_negative(self):
        number = [1, 3, [5, 2, 6]]
        expect = [0, 1, [0]]
        result = integer.SUB_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [0, 2, [6, 7]]
        number2 = [0, 2, [8, 2]]
        expect = [0, 2, [8, 4]]
        result = integer.SUB_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negative(self):
        number1 = [1, 2, [6, 7]]
        number2 = [1, 2, [8, 2]]
        expect = [1, 2, [8, 4]]
        result = integer.SUB_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_different_positive(self):
        number1 = [0, 2, [6, 7]]
        number2 = [1, 2, [8, 2]]
        expect = [0, 3, [4, 0, 1]]
        result = integer.SUB_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_different_negative(self):
        number1 = [1, 2, [6, 7]]
        number2 = [0, 2, [8, 2]]
        expect = [1, 3, [4, 0, 1]]
        result = integer.SUB_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)


class TestDivZZ(unittest.TestCase):

    def test_zero(self):
        number = [0, 2, [3, 5]]
        zero = [0, 1, [0]]
        expect = zero
        result = integer.DIV_ZZ_Z(zero, number)
        self.assertEqual(result, expect)

    def test_equal_positive(self):
        number = [0, 3, [4, 2, 5]]
        expect = [0, 1, [1]]
        result = integer.DIV_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_equal_negative(self):
        number = [1, 3, [4, 2, 5]]
        expect = [0, 1, [1]]
        result = integer.DIV_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_one_positive(self):
        number = [1, 3, [4, 2, 5]]
        one = [0, 1, [1]]
        expect = number
        result = integer.DIV_ZZ_Z(number, one)
        self.assertEqual(result, expect)

    def test_one_negative(self):
        number = [1, 3, [4, 2, 5]]
        one = [1, 1, [1]]
        expect = [0, 3, [4, 2, 5]]
        result = integer.DIV_ZZ_Z(number, one)
        self.assertEqual(result, expect)

    def test_normal_positive(self):
        number1 = [0, 3, [4, 2, 5]]
        number2 = [0, 2, [3, 5]]
        expect = [0, 1, [9]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_first(self):
        number1 = [1, 3, [4, 2, 5]]
        number2 = [0, 2, [3, 5]]
        expect = [1, 2, [0, 1]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_second(self):
        number1 = [0, 3, [4, 2, 5]]
        number2 = [1, 2, [3, 5]]
        expect = [1, 1, [9]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_both(self):
        number1 = [1, 3, [4, 2, 5]]
        number2 = [1, 2, [3, 5]]
        expect = [0, 2, [0, 1]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_positive(self):
        number1 = [0, 1, [4]]
        number2 = [0, 2, [1, 2]]
        expect = [0, 1, [0]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_first(self):
        number1 = [1, 1, [4]]
        number2 = [0, 2, [1, 2]]
        expect = [1, 1, [1]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_second(self):
        number1 = [0, 1, [4]]
        number2 = [1, 2, [1, 2]]
        expect = [1, 1, [0]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_both(self):
        number1 = [1, 1, [4]]
        number2 = [1, 2, [1, 2]]
        expect = [0, 1, [1]]
        result = integer.DIV_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [0, 3, [3, 5, 6]]
        zero = [0, 1, [0]]
        self.assertRaises(Exception, integer.DIV_ZZ_Z, number, zero)


class TestAddZZ(unittest.TestCase):

    def test_zeros(self):
        zero = [0, 1, [0]]
        expect = zero
        result = integer.ADD_ZZ_Z(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [1, 2, [3, 5]]
        zero = [0, 1, [0]]
        expect = number
        result = integer.ADD_ZZ_Z(number, zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [0, 2, [4, 5]]
        number2 = [0, 2, [9, 9]]
        expect = [0, 3, [3, 5, 1]]
        result = integer.ADD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_first(self):
        number1 = [1, 2, [4, 5]]
        number2 = [0, 2, [9, 9]]
        expect = [0, 2, [5, 4]]
        result = integer.ADD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_second(self):
        number1 = [0, 2, [4, 5]]
        number2 = [1, 2, [9, 9]]
        expect = [1, 2, [5, 4]]
        result = integer.ADD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_both(self):
        number1 = [1, 2, [4, 5]]
        number2 = [1, 2, [9, 9]]
        expect = [1, 3, [3, 5, 1]]
        result = integer.ADD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)


class TestModZZ(unittest.TestCase):

    def test_zero(self):
        number = [0, 2, [3, 5]]
        zero = [0, 1, [0]]
        expect = zero
        result = integer.MOD_ZZ_Z(zero, number)
        self.assertEqual(result, expect)

    def test_equal_positive(self):
        number = [0, 3, [4, 2, 5]]
        expect = [1, 1, [0]]
        result = integer.MOD_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_equal_negative(self):
        number = [1, 3, [4, 2, 5]]
        expect = [0, 1, [0]]
        result = integer.MOD_ZZ_Z(number, number)
        self.assertEqual(result, expect)

    def test_one_positive(self):
        number = [1, 3, [4, 2, 5]]
        one = [0, 1, [1]]
        expect = [0, 1, [0]]
        result = integer.MOD_ZZ_Z(number, one)
        self.assertEqual(result, expect)

    def test_one_negative(self):
        number = [1, 3, [4, 2, 5]]
        one = [1, 1, [1]]
        expect = [0, 1, [0]]
        result = integer.MOD_ZZ_Z(number, one)
        self.assertEqual(result, expect)

    def test_normal_positive(self):
        number1 = [0, 3, [4, 2, 5]]
        number2 = [0, 2, [3, 5]]
        expect = [0, 2, [7, 4]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_first(self):
        number1 = [1, 3, [4, 2, 5]]
        number2 = [0, 2, [3, 5]]
        expect = [0, 1, [6]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_second(self):
        number1 = [0, 3, [4, 2, 5]]
        number2 = [1, 2, [3, 5]]
        expect = [0, 2, [7, 4]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_normal_negative_both(self):
        number1 = [1, 3, [4, 2, 5]]
        number2 = [1, 2, [3, 5]]
        expect = [0, 1, [6]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_positive(self):
        number1 = [0, 1, [4]]
        number2 = [0, 2, [1, 2]]
        expect = number1
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_first(self):
        number1 = [1, 1, [4]]
        number2 = [0, 2, [1, 2]]
        expect = [0, 2, [7, 1]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_second(self):
        number1 = [0, 1, [4]]
        number2 = [1, 2, [1, 2]]
        expect = [0, 1, [4]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_less_negative_both(self):
        number1 = [1, 1, [4]]
        number2 = [1, 2, [1, 2]]
        expect = [0, 2, [7, 1]]
        result = integer.MOD_ZZ_Z(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [0, 3, [3, 5, 6]]
        zero = [0, 1, [0]]
        self.assertRaises(Exception, integer.MOD_ZZ_Z, number, zero)


class TestTransZ(unittest.TestCase):

    def test_zero(self):
        zero = [0, 1, [0]]
        expect = [1, [0]]
        result = integer.TRANS_Z_N(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [0, 2, [3, 5]]
        expect = [2, [3, 5]]
        result = integer.TRANS_Z_N(number)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [1, 2, [3, 5]]
        self.assertRaises(Exception, integer.TRANS_Z_N, number)


class TestTransN(unittest.TestCase):

    def test_zero(self):
        zero = [1, [0]]
        expect = [0, 1, [0]]
        result = integer.TRANS_N_Z(zero)
        self.assertEqual(result, expect)

    def test_normal(self):
        number = [3, [5, 6, 4]]
        expect = [0, 3, [5, 6, 4]]
        result = integer.TRANS_N_Z(number)
        self.assertEqual(result, expect)

