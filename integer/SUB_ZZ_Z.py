from integer import POZ_Z_D, ABS_Z_N, MUL_ZM_Z
from natural import COM_NN_D, ADD_NN_N, SUB_NN_N

import common


def SUB_ZZ_Z(number1, number2):
    """
    Z-7
    Вычитание целых чисел
    Колосюк Владислав, 7305
    """
    # Модули чисел
    m1 = ABS_Z_N(number1)
    m2 = ABS_Z_N(number2)

    # Знаки чисел
    p1 = POZ_Z_D(number1)
    p2 = POZ_Z_D(number2)

    # Если вычитаемое ноль, возвращаем копию уменьшаемое
    if p2 == 0:
        result = common.copy_Z(number1)
    # Если уменьщаемое ноль, результат - вычитаемое, умноженное на -1
    elif p1 == 0:
        result = MUL_ZM_Z(number2)
    # Случай разных знаков
    elif p1 == 2 and p2 == 1 or p1 == 1 and p2 == 2:
        # Модулем числа будет являться сумма модулей, а знаком - знак первого
        # числа
        m = ADD_NN_N(m1, m2)
        p = number1[0]
        result = [p, m[0], m[1]]
    # Одинаковые знаки
    else:
        # Вычитаем из большего модуля меньший. Если первое число имеет больший
        # модуль, то результат будет иметь тот же знак, что и оно.
        if COM_NN_D(m1, m2) == 2:
            m = SUB_NN_N(m1, m2)
            p = number1[0]
        # Иначе - знак меняется
        else:
            m = SUB_NN_N(m2, m1)
            p = 0 if number1[0] == 1 else 1
        result = [p, m[0], m[1]]

    return result

