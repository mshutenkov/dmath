import natural

import unittest


class TestAdd1N(unittest.TestCase):

    def test_zero(self):
        number = [1, [0]]
        expect = [1, [1]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)

    def test_one(self):
        number = [1, [1]]
        expect = [1, [2]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)

    def test_nine(self):
        number = [1, [9]]
        expect = [2, [0, 1]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)

    def test_simple(self):
        number = [3, [3, 2, 4]]
        expect = [3, [4, 2, 4]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)

    def test_shift(self):
        number = [3, [9, 9, 9]]
        expect = [4, [0, 0, 0, 1]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)

    def test_complex(self):
        number = [5, [9, 9, 9, 3, 5]]
        expect = [5, [0, 0, 0, 4, 5]]
        result = natural.ADD_1N_N(number)
        self.assertEqual(result, expect)


class TestComNN(unittest.TestCase):

    def test_zeros(self):
        one = [1, [0]]
        two = one
        expect = 0
        result = natural.COM_NN_D(one, two)
        self.assertEqual(result, expect)

    def test_equal(self):
        one = [3, [2, 7, 4]]
        two = one
        expect = 0
        result = natural.COM_NN_D(one, two)
        self.assertEqual(result, expect)

    def test_simple(self):
        one = [3, [2, 4, 3]]
        two = [3, [3, 2, 4]]

        result = natural.COM_NN_D(one, two)
        self.assertEqual(result, 1)

        result = natural.COM_NN_D(two, one)
        self.assertEqual(result, 2)

    def test_length(self):
        one = [4, [1, 1, 1, 1]]
        two = [3, [9, 9, 9]]

        result = natural.COM_NN_D(one, two)
        self.assertEqual(result, 2)

        result = natural.COM_NN_D(two, one)
        self.assertEqual(result, 1)


class TestNZerN(unittest.TestCase):

    def test_zero(self):
        number = [1, [0]]
        self.assertFalse(natural.NZER_N_B(number))

    def test_notzero(self):
        number = [1, [4]]
        self.assertTrue(natural.NZER_N_B(number))


class TestMulND(unittest.TestCase):

    def test_zero(self):
        number = [1, [0]]
        digit = 4
        expect = number
        result = natural.MUL_ND_N(number, digit)
        self.assertEqual(result, expect)

    def test_one(self):
        number = [1, [1]]
        digit = 5
        expect = [1, [5]]
        result = natural.MUL_ND_N(number, digit)
        self.assertEqual(result, expect)

    def test_simple(self):
        number = [3, [1, 2, 3]]
        digit = 3
        expect = [3, [3, 6, 9]]
        result = natural.MUL_ND_N(number, digit)
        self.assertEqual(result, expect)

    def test_complex(self):
        number = [6, [9, 9, 9, 9, 9, 9]]
        digit = 9
        expect = [7, [1, 9, 9, 9, 9, 9, 8]]
        result = natural.MUL_ND_N(number, digit)
        self.assertEqual(result, expect)


class TestAddNN(unittest.TestCase):

    def test_zeros(self):
        number = [1, [0]]
        expect = number
        result = natural.ADD_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [4, [3, 5, 3, 2]]
        zero = [1, [0]]
        expect = number
        result = natural.ADD_NN_N(number, zero)
        self.assertEqual(result, expect)

    def test_simple(self):
        number1 = [4, [1, 2, 3, 4]]
        number2 = [3, [4, 3, 2]]
        expect = [4, [5, 5, 5, 4]]
        result = natural.ADD_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_complex(self):
        number1 = [3, [6, 7, 5]]
        number2 = [3, [8, 7, 9]]
        expect = [4, [4, 5, 5, 1]]
        result = natural.ADD_NN_N(number1, number2)
        self.assertEqual(result, expect)


class TestSubNN(unittest.TestCase):

    def test_zeros(self):
        number = [1, [0]]
        expect = number
        result = natural.SUB_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [3, [2, 6, 4]]
        zero = [1, [0]]
        expect = number
        result = natural.SUB_NN_N(number, zero)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [3, [6, 7, 4]]
        number2 = [3, [2, 3, 1]]
        expect = [3, [4, 4, 3]]
        result = natural.SUB_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_equal(self):
        number = [3, [6, 7, 4]]
        expect = [1, [0]]
        result = natural.SUB_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_shift(self):
        number1 = [3, [0, 0, 1]]
        number2 = [1, [3]]
        expect = [2, [7, 9]]
        result = natural.SUB_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number1 = [3, [0, 0, 1]]
        number2 = [3, [1, 0, 1]]
        self.assertRaises(Exception, natural.SUB_NN_N, number1, number2)


class TestMulNk(unittest.TestCase):

    def test_zero(self):
        number = [3, [2, 5, 3]]
        degree = 0
        expect = number
        result = natural.MUL_Nk_N(number, degree)
        self.assertEqual(result, expect)

    def test_one(self):
        number = [3, [2, 5, 3]]
        degree = 1
        expect = [4, [0, 2, 5, 3]]
        result = natural.MUL_Nk_N(number, degree)
        self.assertEqual(result, expect)

    def test_many(self):
        number = [3, [2, 5, 3]]
        degree = 5
        expect = [8, [0, 0, 0, 0, 0, 2, 5, 3]]
        result = natural.MUL_Nk_N(number, degree)
        self.assertEqual(result, expect)


class TestSubNDN(unittest.TestCase):

    def test_zero(self):
        number1 = [3, [6, 4, 2]]
        number2 = [2, [3, 6]]
        digit = 0
        expect = number1
        result = natural.SUB_NDN_N(number1, number2, digit)
        self.assertEqual(result, expect)

    def test_one(self):
        number1 = [3, [6, 4, 2]]
        number2 = [2, [3, 6]]
        digit = 1
        expect = [3, [3, 8, 1]]
        result = natural.SUB_NDN_N(number1, number2, digit)
        self.assertEqual(result, expect)

    def test_many(self):
        number1 = [3, [6, 4, 2]]
        number2 = [2, [3, 6]]
        digit = 3
        expect = [2, [7, 5]]
        result = natural.SUB_NDN_N(number1, number2, digit)
        self.assertEqual(result, expect)

    def test_fail(self):
        number1 = [3, [6, 4, 2]]
        number2 = [2, [3, 6]]
        digit = 4
        self.assertRaises(Exception, natural.SUB_NDN_N, number1, number2, digit)


class TestDivNND(unittest.TestCase):

    def test_zero(self):
        number1 = [1, [0]]
        number2 = [2, [2, 3]]
        degree = 0
        expect = 0
        result = natural.DIV_NN_Dk(number1, number2, degree)
        self.assertEqual(result, expect)

    def test_normal_zero(self):
        number1 = [3, [9, 9, 9]]
        number2 = [3, [5, 4, 3]]
        degree = 0
        expect = 2
        result = natural.DIV_NN_Dk(number1, number2, degree)
        self.assertEqual(result, expect)

    def test_normal_many(self):
        number1 = [3, [9, 9, 9]]
        number2 = [1, [2]]
        degree = 2
        expect = 4
        result = natural.DIV_NN_Dk(number1, number2, degree)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [3, [1, 2, 3]]
        zero = [1, [0]]
        degree = 2
        self.assertRaises(Exception, natural.DIV_NN_Dk, number, zero, degree)


class TestDivNN(unittest.TestCase):

    def test_zero(self):
        zero = [1, [0]]
        number = [3, [6, 2, 6]]
        expect = [1, [0]]
        result = natural.DIV_NN_N(zero, number)
        self.assertEqual(result, expect)

    def test_equal(self):
        number = [3, [6, 2, 6]]
        expect = [1, [1]]
        result = natural.DIV_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_small(self):
        number1 = [2, [1, 2]]
        number2 = [2, [2, 2]]
        expect = [1, [0]]
        result = natural.DIV_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [5, [6, 5, 3, 6, 4]]
        number2 = [2, [8, 4]]
        expect = [3, [5, 6, 9]]
        result = natural.DIV_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [3, [4, 5, 3]]
        zero = [1, [0]]
        self.assertRaises(Exception, natural.DIV_NN_N, number, zero)


class TestModNN(unittest.TestCase):

    def test_zero(self):
        zero = [1, [0]]
        number = [3, [6, 2, 6]]
        expect = [1, [0]]
        result = natural.MOD_NN_N(zero, number)
        self.assertEqual(result, expect)

    def test_equal(self):
        number = [3, [6, 2, 6]]
        expect = [1, [0]]
        result = natural.MOD_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_small(self):
        number1 = [2, [1, 2]]
        number2 = [2, [2, 2]]
        expect = [2, [1, 2]]
        result = natural.MOD_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [5, [6, 5, 3, 6, 4]]
        number2 = [2, [8, 4]]
        expect = [2, [6, 3]]
        result = natural.MOD_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [3, [4, 5, 3]]
        zero = [1, [0]]
        self.assertRaises(Exception, natural.MOD_NN_N, number, zero)


class TestGcfNN(unittest.TestCase):

    def test_zeros(self):
        zero = [1, [0]]
        expect = zero
        result = natural.GCF_NN_N(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [2, [3, 2]]
        zero = [1, [0]]
        expect = number
        result = natural.GCF_NN_N(number, zero)
        self.assertEqual(result, expect)

    def test_equal(self):
        number = [2, [3, 2]]
        expect = number
        result = natural.GCF_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_simple(self):
        number1 = [2, [1, 3]]
        number2 = [2, [5, 1]]
        expect = [1, [1]]
        result = natural.GCF_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [2, [2, 7]]
        number2 = [2, [0, 6]]
        expect = [2, [2, 1]]
        result = natural.GCF_NN_N(number1, number2)
        self.assertEqual(result, expect)


class TestMulNN(unittest.TestCase):

    def test_zero(self):
        number = [2, [2, 5]]
        zero = [1, [0]]
        expect = zero
        result = natural.MUL_NN_N(number, zero)
        self.assertEqual(result, expect)

    def test_one(self):
        number = [3, [6, 4, 5]]
        one = [1, [1]]
        expect = number
        result = natural.MUL_NN_N(number, one)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [3, [6, 4, 5]]
        number2 = [2, [5, 2]]
        expect = [5, [0, 5, 6, 3, 1]]
        result = natural.MUL_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_big(self):
        number1 = [10, [
            5, 4, 3, 2, 1, 3, 5, 2, 4, 7
            ]]
        number2 = [13, [
            3, 1, 2, 5, 4, 6, 4, 2, 7, 4,
            3, 1, 6
            ]]
        expect = [23, [
            5, 8, 4, 4, 5, 0, 4, 3, 8, 5,
            7, 2, 1, 4, 6, 6, 4, 2, 2, 5,
            5, 5, 4
            ]]
        result = natural.MUL_NN_N(number1, number2)
        self.assertEqual(result, expect)


class TestLcmNN(unittest.TestCase):

    def test_ones(self):
        one = [1, [1]]
        expect = one
        result = natural.LCM_NN_N(one, one)
        self.assertEqual(result, expect)

    def test_equal(self):
        number = [3, [2, 5, 4]]
        expect = number
        result = natural.LCM_NN_N(number, number)
        self.assertEqual(result, expect)

    def test_simple(self):
        number1 = [2, [3, 1]]
        number2 = [1, [5]]
        expect = [2, [5, 6]]
        result = natural.LCM_NN_N(number1, number2)
        self.assertEqual(result, expect)

    def test_normal(self):
        number1 = [2, [4, 2]]
        number2 = [2, [6, 3]]
        expect = [2, [2, 7]]
        result = natural.LCM_NN_N(number1, number2)
        self.assertEqual(result, expect)

