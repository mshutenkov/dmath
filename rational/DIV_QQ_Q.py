from integer import MUL_ZZ_Z, TRANS_N_Z, ABS_Z_N, MUL_ZM_Z, POZ_Z_D
from rational import RED_Q_Q


def DIV_QQ_Q(number1, number2):
    """
    Q-8
    Деление дробей
    Фёдорова Алиса, 7305
    """
    # Числитель - произведение числителя первой дроби и знаменателя второй
    n = MUL_ZZ_Z(number1[0], TRANS_N_Z(number2[1]))
    # Знаменатель - произведение числителя второй дроби и знаменателя первой
    m = MUL_ZZ_Z(TRANS_N_Z(number1[1]), number2[0])

    if POZ_Z_D(m) == 0:
        raise Exception('Попытка деления на 0')

    # Если знаменатель отрицательный - домножаем числитель на -1
    if POZ_Z_D(m) == 1:
        n = MUL_ZM_Z(n)
    # В знаменатель - модуль
    result = [n, ABS_Z_N(m)]

    return RED_Q_Q(result)

