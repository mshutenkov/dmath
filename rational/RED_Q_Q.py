from natural import GCF_NN_N
from integer import ABS_Z_N, DIV_ZZ_Z, TRANS_N_Z, TRANS_Z_N


def RED_Q_Q(number):
    """
    Q-1
    Сокращение дроби
    Королев Андрей, 7305
    """
    result = []
    
    # Определяется модуль числителя
    n = ABS_Z_N(number[0])
    # Находится НОД
    a = GCF_NN_N(n, number[1])

    # Числитель и знаменятель делятся на найденый ранее НОД
    # Перед делением НОД и знаменатель преобразуется из натурального в целое
    gcf = TRANS_N_Z(a)
    N = DIV_ZZ_Z(number[0], gfc)
    M = DIV_ZZ_Z(TRANS_N_Z(number[1]), gfc)

    # В результате новый знаменатель преобразуется из целого в натураьное
    result = [N, TRANS_Z_N(M)]
    return result

