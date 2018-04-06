from integer import MUL_ZZ_Z
from natural import MUL_NN_N
from rational import RED_Q_Q


def MUL_QQ_Q(number1, number2):
    """
    Q-7
    Умножение дробей
    Фёдоров Семён, 7305
    """
    # Умножаем числитель на числитель, знаменатель на знаменатель
    n = MUL_ZZ_Z(number1[0], number2[0])
    m = MUL_NN_N(number1[1], number2[1])
    return RED_Q_Q([n, m])

