from rational import MUL_QQ_Q
from common import num_to_N, num_to_Z


def MUL_PQ_P(polynom, num):
    """
    P-3
    Умножение многочлена на рациональное число
    Мартыненко Александр, 7305
    """
    # Если умножаем на нуль
    if num == [num_to_Z(0), num_to_N(1)]:
        result = [0, [[num_to_Z(0), num_to_N(1)]]]
    # Если умножаем на число, отличное от нуля
    else:
        result = [polynom[0], []]
        #Умножаем каждый коэффициент на это число
        for i in range(result[0] + 1):
            result[1].append(MUL_QQ_Q(polynom[1][i], num))

    # Возвращаем полученный многочлен      
    return result

