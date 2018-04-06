from integer import POZ_Z_D, ABS_Z_N, MUL_ZM_Z
from natural import COM_NN_D, ADD_NN_N, SUB_NN_N
import common


def ADD_ZZ_Z(number1, number2):
    """
    Z-6
    Сложение целых чисел
    Царёв Александр, 7305
    """
    # Модули чисел
    m1 = ABS_Z_N(number1)
    m2 = ABS_Z_N(number2)

    # Знаки чисел
    p1 = POZ_Z_D(number1)
    p2 = POZ_Z_D(number2)

    # Если одно из слогаемых равно нулю, то результат - второе слогаемое
    if p1 == 0:
        result = common.copy_Z(number2)
    elif p2 == 0:
        result = common.copy_Z(number1)
    # Если знаки одинаковые, складываем модули, сохраняем знак
    elif p1 == 2 and p2 == 2 or p1 == 1 and p2 == 1:
        m = ADD_NN_N(m1, m2)
        p = 0 if p1 == 2 else 1
        result = [p, m[0], m[1]]
    # Разные знаки - из большего модуля вычитаем меньший и оставляем
    # знак числа с наибольшим модулем
    else:
        if COM_NN_D(m1, m2) == 2:
            m = SUB_NN_N(m1, m2)
            p = number1[0]
        else:
            m = SUB_NN_N(m2, m1)
            p = number2[0]
        result = [p, m[0], m[1]]

    return result

