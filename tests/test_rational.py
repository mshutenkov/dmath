import rational

import unittest


class TestRedQ(unittest.TestCase):

    def test_zero(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.RED_Q_Q(zero)
        self.assertEqual(result, expect)

    def test_one(self):
        number = [
                [0, 2, [1, 3]],
                [2, [1, 3]],
                ]
        expect = [
                [0, 1, [1]],
                [1, [1]],
                ]
        result = rational.RED_Q_Q(number)
        self.assertEqual(result, expect)

    def test_simple(self):
        number = [
                [0, 2, [1, 3]],
                [2, [1, 2]],
                ]
        expect = number
        result = rational.RED_Q_Q(number)
        self.assertEqual(result, expect)

    def test_normal(self):
        number = [
                [0, 2, [4, 2]],
                [2, [6, 3]],
                ]
        expect = [
                [0, 1, [2]],
                [1, [3]],
                ]
        result = rational.RED_Q_Q(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [
                [1, 2, [4, 2]],
                [2, [6, 3]],
                ]
        expect = [
                [1, 1, [2]],
                [1, [3]],
                ]
        result = rational.RED_Q_Q(number)
        self.assertEqual(result, expect)


class TestAddQQ(unittest.TestCase):

    def test_zeros(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.ADD_QQ_Q(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [
                [0, 3, [5, 6, 3]],
                [2, [3, 1]],
                ]
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = number
        result = rational.ADD_QQ_Q(number, zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [1, 4]],
                [2, [1, 2]],
                ]
        result = rational.ADD_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_first(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [9, 2]],
                [2, [1, 2]],
                ]
        result = rational.ADD_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_second(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [9, 2]],
                [2, [1, 2]],
                ]
        result = rational.ADD_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_both(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [1, 4]],
                [2, [1, 2]],
                ]
        result = rational.ADD_QQ_Q(number1, number2)
        self.assertEqual(result, expect)


class TestSubQQ(unittest.TestCase):

    def test_zeros(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.SUB_QQ_Q(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [
                [0, 3, [5, 6, 3]],
                [2, [3, 1]],
                ]
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = number
        result = rational.SUB_QQ_Q(number, zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [9, 2]],
                [2, [1, 2]],
                ]
        result = rational.SUB_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_first(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [1, 4]],
                [2, [1, 2]],
                ]
        result = rational.SUB_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_second(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [1, 4]],
                [2, [1, 2]],
                ]
        result = rational.SUB_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_both(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [9, 2]],
                [2, [1, 2]],
                ]
        result = rational.SUB_QQ_Q(number1, number2)
        self.assertEqual(result, expect)


class TestMulQQ(unittest.TestCase):

    def test_zeros(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.MUL_QQ_Q(zero, zero)
        self.assertEqual(result, expect)

    def test_zero(self):
        number = [
                [0, 2, [5, 3]],
                [1, [2]],
                ]
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.MUL_QQ_Q(number, zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [0, 1]],
                [2, [1, 2]],
                ]
        result = rational.MUL_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_first(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [0, 1]],
                [2, [1, 2]],
                ]
        result = rational.MUL_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_second(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [0, 1]],
                [2, [1, 2]],
                ]
        result = rational.MUL_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_both(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [0, 1]],
                [2, [1, 2]],
                ]
        result = rational.MUL_QQ_Q(number1, number2)
        self.assertEqual(result, expect)


class TestDivQQ(unittest.TestCase):

    def test_zero(self):
        number = [
                [0, 2, [5, 3]],
                [1, [2]],
                ]
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = zero
        result = rational.DIV_QQ_Q(zero, number)
        self.assertEqual(result, expect)

    def test_positive(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [5, 3]],
                [1, [6]],
                ]
        result = rational.DIV_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_first(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [0, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [5, 3]],
                [1, [6]],
                ]
        result = rational.DIV_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_second(self):
        number1 = [
                [0, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [1, 2, [5, 3]],
                [1, [6]],
                ]
        result = rational.DIV_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_negative_both(self):
        number1 = [
                [1, 1, [5]],
                [1, [3]],
                ]
        number2 = [
                [1, 1, [2]],
                [1, [7]],
                ]
        expect = [
                [0, 2, [5, 3]],
                [1, [6]],
                ]
        result = rational.DIV_QQ_Q(number1, number2)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [
                [1, 1, [5]],
                [1, [3]],
                ]
        zero = [
                [0, 1, [0]],
                [1, [3]],
                ]
        self.assertRaises(Exception, rational.DIV_QQ_Q, number, zero)


class TestTransZ(unittest.TestCase):

    def test_zero(self):
        zero = [0, 1, [0]]
        expect = [
                [0, 1, [0]],
                [1, [1]],
                ]
        result = rational.TRANS_Z_Q(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [0, 3, [4, 6, 7]]
        expect = [
                [0, 3, [4, 6, 7]],
                [1, [1]],
                ]
        result = rational.TRANS_Z_Q(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [1, 3, [4, 6, 7]]
        expect = [
                [1, 3, [4, 6, 7]],
                [1, [1]],
                ]
        result = rational.TRANS_Z_Q(number)
        self.assertEqual(result, expect)


class TestTransQ(unittest.TestCase):

    def test_zero(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = [0, 1, [0]]
        result = rational.TRANS_Q_Z(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [
                [0, 3, [4, 6, 7]],
                [1, [1]],
                ]
        expect = [0, 3, [4, 6, 7]]
        result = rational.TRANS_Q_Z(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [
                [1, 3, [4, 6, 7]],
                [1, [1]],
                ]
        expect = [1, 3, [4, 6, 7]]
        result = rational.TRANS_Q_Z(number)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [
                [1, 3, [4, 6, 7]],
                [1, [3]],
                ]
        self.assertRaises(Exception, rational.TRANS_Q_Z, number)


class TestIntQ(unittest.TestCase):

    def test_zero(self):
        zero = [
                [0, 1, [0]],
                [1, [1]],
                ]
        expect = True
        result = rational.INT_Q_B(zero)
        self.assertEqual(result, expect)

    def test_positive(self):
        number = [
                [0, 3, [4, 6, 7]],
                [1, [1]],
                ]
        expect = True
        result = rational.INT_Q_B(number)
        self.assertEqual(result, expect)

    def test_negative(self):
        number = [
                [1, 3, [4, 6, 7]],
                [1, [1]],
                ]
        expect = True
        result = rational.INT_Q_B(number)
        self.assertEqual(result, expect)

    def test_fail(self):
        number = [
                [1, 3, [4, 6, 7]],
                [1, [3]],
                ]
        expect = False
        result = rational.INT_Q_B(number)
        self.assertEqual(result, expect)

