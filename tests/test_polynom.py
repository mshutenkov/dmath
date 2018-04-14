import polynom

import unittest

# x^2 + 2x + 1
p_x2_2x_1 = [2, [
    [ [0, 1, [1]], [1, [1]] ],
    [ [0, 1, [2]], [1, [1]] ],
    [ [0, 1, [1]], [1, [1]] ],
    ]]

# 3/2x^2 + 3x^2 + 3/2
p_3p2x2_3x_3p2 = [2, [
    [ [0, 1, [3]], [1, [2]] ],
    [ [0, 1, [3]], [1, [1]] ],
    [ [0, 1, [3]], [1, [2]] ],
    ]]

# x^2 - 2x + 1
p_x2_n2x_1 = [2, [
    [ [0, 1, [1]], [1, [1]] ],
    [ [1, 1, [2]], [1, [1]] ],
    [ [0, 1, [1]], [1, [1]] ],
    ]]

# x + 1
p_x_1 = [1, [
    [ [0, 1, [1]], [1, [1]] ],
    [ [0, 1, [1]], [1, [1]] ],
    ]]

# x - 1
p_x_n1 = [1, [
    [ [1, 1, [1]], [1, [1]] ],
    [ [0, 1, [1]], [1, [1]] ],
    ]]

# 2x^2 + 2
p_2x2_2 = [2, [
    [ [0, 1, [2]], [1, [1]] ],
    [ [0, 1, [0]], [1, [1]] ],
    [ [0, 1, [2]], [1, [1]] ],
    ]]

# -2x^2 - 2
p_n2x2_n1 = [2, [
    [ [1, 1, [2]], [1, [1]] ],
    [ [0, 1, [0]], [1, [1]] ],
    [ [1, 1, [2]], [1, [1]] ],
    ]]

# 2x + 2
p_2x_2 = [1, [
    [ [0, 1, [2]], [1, [1]] ],
    [ [0, 1, [2]], [1, [1]] ],
    ]]

# 4x
p_4x = [1, [
    [ [0, 1, [0]], [1, [1]] ],
    [ [0, 1, [4]], [1, [1]] ],
    ]]

# -4x
p_n4x = [1, [
    [ [0, 1, [0]], [1, [1]] ],
    [ [1, 1, [4]], [1, [1]] ],
    ]]

p_zero = [0, [
    [ [0, 1, [0]], [1, [1]] ],
    ]]

p_one = [0, [
    [ [0, 1, [1]], [1, [1]] ],
    ]]


class TestSubPP(unittest.TestCase):
    
    def test_zeros(self):
        expect = p_zero
        result = polynom.SUB_PP_P(p_zero, p_zero)
        self.assertEqual(result, expect)
    
    def test_equal(self):
        expect = p_zero
        result = polynom.SUB_PP_P(p_x2_2x_1, p_x2_2x_1)
        self.assertEqual(result, expect)

    def test_normal(self):
        # x^2 - 2x + 1 - (x^2 + 2x + 1) = -4x
        expect = p_n4x
        result = polynom.SUB_PP_P(p_x2_n2x_1, p_x2_2x_1)
        self.assertEqual(result, expect)


class TestAddPP(unittest.TestCase):

    def test_zeros(self):
        expect = p_zero
        result = polynom.ADD_PP_P(p_zero, p_zero)
        self.assertEqual(result, expect)
    
    def test_opposite(self):
        expect = p_zero
        result = polynom.ADD_PP_P(p_n4x, p_4x)
        self.assertEqual(result, expect)

    def test_normal(self):
        # x^2 - 2x + 1 + x^2 + 2x + 1 = 2x^2 + 2
        expect = p_2x2_2
        result = polynom.ADD_PP_P(p_x2_n2x_1, p_x2_2x_1)
        self.assertEqual(result, expect)


class TestMulPxk(unittest.TestCase):

    def test_zero(self):
        expect = p_x2_2x_1
        result = polynom.MUL_Pxk_P(p_x2_2x_1, 0)
        self.assertEqual(result, expect)

    def test_normal(self):
        expect = [10, [
                *([[ [0, 1, [0]], [1, [1]] ]] * 8),
                *(p_x2_2x_1[1]),
                ]]
        result = polynom.MUL_Pxk_P(p_x2_2x_1, 8)
        self.assertEqual(result, expect)


class TestMulPQ(unittest.TestCase):

    def test_zero(self):
        zero = [ [0, 1, [0]], [1, [1]] ]
        expect = p_zero
        result = polynom.MUL_PQ_P(p_x2_2x_1, zero)
        self.assertEqual(result, expect)

    def test_one(self):
        one = [ [0, 1, [1]], [1, [1]] ]
        expect = p_x2_2x_1
        result = polynom.MUL_PQ_P(p_x2_2x_1, one)
        self.assertEqual(result, expect)

    def test_normal(self):
        # (x^2 + 2x + 1) * 3/2 = 3/2x^2 + 3x + 3/2
        number = [ [0, 1, [3]], [1, [2]] ]
        expect = p_3p2x2_3x_3p2
        result = polynom.MUL_PQ_P(p_x2_2x_1, number)
        self.assertEqual(result, expect)


class TestDegP(unittest.TestCase):

    def test_zero(self):
        expect = 0
        result = polynom.DEG_P_N(p_one)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = 1
        result = polynom.DEG_P_N(p_4x)
        self.assertEqual(result, expect)

    def test_two(self):
        expect = 2
        result = polynom.DEG_P_N(p_x2_2x_1)
        self.assertEqual(result, expect)


class TestMulPP(unittest.TestCase):

    def test_zeros(self):
        expect = p_zero
        result = polynom.MUL_PP_P(p_zero, p_zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        expect = p_zero
        result = polynom.MUL_PP_P(p_zero, p_x2_2x_1)
        self.assertEqual(result, expect)

    def test_normal(self):
        # (x - 1) * (x - 1) = x^2 - 2x + 1
        expect = p_x2_n2x_1
        result = polynom.MUL_PP_P(p_x_n1, p_x_n1)
        self.assertEqual(result, expect)


class TestDivPP(unittest.TestCase):

    def test_zero(self):
        expect = p_zero
        result = polynom.DIV_PP_P(p_zero, p_one)
        self.assertEqual(result, expect)

    def test_normal(self):
        expect = p_x_1
        result = polynom.DIV_PP_P(p_x2_2x_1, p_x_1)
        self.assertEqual(result, expect)

    def test_less(self):
        expect = p_zero
        result = polynom.DIV_PP_P(p_x_1, p_x2_2x_1)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = p_one
        result = polynom.DIV_PP_P(p_x2_2x_1, p_x2_n2x_1)
        self.assertEqual(result, expect)

    def test_fail(self):
        self.assertRaises(Exception, polynom.DIV_PP_P, p_x_1, p_zero)


class TestModPP(unittest.TestCase):

    def test_zero(self):
        expect = p_zero
        result = polynom.MOD_PP_P(p_zero, p_4x)
        self.assertEqual(result, expect)

    def test_less(self):
        expect = p_x_1
        result = polynom.MOD_PP_P(p_x_1, p_x2_2x_1)
        self.assertEqual(result, expect)

    def test_none(self):
        expect = p_zero
        result = polynom.MOD_PP_P(p_x2_2x_1, p_x_1)
        self.assertEqual(result, expect)
    
    def test_one(self):
        expect = p_one
        result = polynom.MOD_PP_P(p_x_1, p_n4x)
        self.assertEqual(result, expect)

    def test_fail(self):
        self.assertRaises(Exception, polynom.MOD_PP_P, p_x_1, p_zero)


class TestDerP(unittest.TestCase):

    def test_zero(self):
        expect = p_zero
        result = polynom.DER_P_P(p_zero)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = p_zero
        result = polynom.DER_P_P(p_one)
        self.assertEqual(result, expect)

    def test_two(self):
        expect = p_one
        result = polynom.DER_P_P(p_x_1)
        self.assertEqual(result, expect)

    def test_three(self):
        expect = p_2x_2
        result = polynom.DER_P_P(p_x2_2x_1)
        self.assertEqual(result, expect)


class TestNmrP(unittest.TestCase):

    def test_zero(self):
        expect = p_zero
        result = polynom.NMR_P_P(p_zero)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = p_one
        result = polynom.NMR_P_P(p_one)
        self.assertEqual(result, expect)

    def test_none(self):
        expect = p_2x2_2
        result = polynom.NMR_P_P(p_2x2_2)
        self.assertEqual(result, expect)

    def test_normal(self):
        expect = p_x_1
        result = polynom.NMR_P_P(p_x2_2x_1)
        self.assertEqual(result, expect)


class TestLedP(unittest.TestCase):

    def test_zero(self):
        expect = [ [0, 1, [0]], [1, [1]] ]
        result = polynom.LED_P_Q(p_zero)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = [ [0, 1, [1]], [1, [1]] ]
        result = polynom.LED_P_Q(p_one)
        self.assertEqual(result, expect)

    def test_two(self):
        expect = [ [0, 1, [2]], [1, [1]] ]
        result = polynom.LED_P_Q(p_2x2_2)
        self.assertEqual(result, expect)

    def test_two_neg(self):
        expect = [ [1, 1, [4]], [1, [1]] ]
        result = polynom.LED_P_Q(p_n4x)
        self.assertEqual(result, expect)

    def test_three(self):
        expect = [ [0, 1, [3]], [1, [2]] ]
        result = polynom.LED_P_Q(p_3p2x2_3x_3p2)
        self.assertEqual(result, expect)


class TestFacP(unittest.TestCase):

    def test_zero(self):
        expect = [ [0, 1, [0]], [1, [1]] ]
        result = polynom.FAC_P_Q(p_zero)
        self.assertEqual(result, expect)

    def test_one(self):
        expect = [ [0, 1, [1]], [1, [1]] ]
        result = polynom.FAC_P_Q(p_one)
        self.assertEqual(result, expect)

    def test_normal(self):
        expect = [ [0, 1, [3]], [1, [2]] ]
        result = polynom.FAC_P_Q(p_3p2x2_3x_3p2)
        self.assertEqual(result, expect)

