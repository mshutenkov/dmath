from polynom import DEG_P_N, MOD_PP_P, MUL_PQ_P
from rational import DIV_QQ_Q
from integer import POZ_Z_D

import common


def GCF_PP_P(polynom1, polynom2):
    """
    P-11
    НОД многочленов
    Рэшин Даниил, 7305
    """
    one = polynom1
    two = polynom2

    # Алгоритм Евклида
    while DEG_P_N(two) > 0 or POZ_Z_D(two[1][0][0]) != 0:
        two, one = MOD_PP_P(one, two), two

    # Делим на старший коэффициент для получения единицы
    first = common.copy_Q(one[1][-1])
    first = DIV_QQ_Q(common.rat_to_Q(1, 1), first)
    return MUL_PQ_P(one, first)

