from polynom import MUL_PQ_P, MUL_Pxk_P, ADD_PP_P
import common


def MUL_PP_P(polynom1, polynom2):
    """
    P-8
    Умножение многочленов
    Хафизов Ильназ, 7305
    """
    # Нулевой многочлен
    result = common.coef_to_P([(0, 1)])

    for i in range(polynom2[0] + 1):
        # Умножаем первый многочлен на i коэффициент второго и на 10^i
        add = MUL_PQ_P(polynom1, polynom2[1][i])
        add = MUL_Pxk_P(add, i)
        # Прибавляем к результату
        result = ADD_PP_P(result, add)

    return result

