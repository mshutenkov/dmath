from natural import DIV_NN_N, MOD_NN_N, ADD_1N_N, NZER_N_B
from integer import ABS_Z_N, POZ_Z_D

import common


def DIV_ZZ_Z(number1, number2):
    """
    Z-9
    Частное от деления большего целого числа на меньшее
    или равное натуральное с остатком (делитель отличен от нуля)
    Власенко Владислав, 7305
    """
    # Определяем модули чисел
    m1 = ABS_Z_N(number1)
    m2 = ABS_Z_N(number2)
    # Частное от деления модулей
    m = DIV_NN_N(m1, m2)
    # Остаток от деления
    mod = MOD_NN_N(m1, m2)

    # Знаки исходных чисел
    p1 = POZ_Z_D(number1)
    p2 = POZ_Z_D(number2)

    # Если знаки одинаковые или одно из чисел ноль - результат положительный
    if p1 == p2 or p1 == 0 or p2 == 0:
        p = 0
    else:
        p = 1

    # Если делимое отрицательное и есть ненулевой остаток -
    # прибавляем к частному единицу
    if NZER_N_B(mod) and p1 == 1:
        m = ADD_1N_N(m)

    return [p, m[0], m[1]]

