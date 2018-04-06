from natural import MUL_NN_N
from integer import POZ_Z_D, ABS_Z_N, MUL_ZM_Z
import common


def MUL_ZZ_Z(number1, number2):
    """
    Z-8
    Умножение целых чисел
    Царёв Александр, 7305
    """
    # Умножаем модули
    m1 = ABS_Z_N(number1)
    m2 = ABS_Z_N(number2)
    m = MUL_NN_N(m1, m2)

    # Если знаки одинаковые или одно из чисел ноль, то результат
    # неотрицательный
    p1 = POZ_Z_D(number1)
    p2 = POZ_Z_D(number2)
    if p1 == p2 or p1 == 0 or p2 == 0:
        p = 0
    else:
        p = 1
    
    return [p, m[0], m[1]]


