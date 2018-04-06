from natural import LCM_NN_N, GCF_NN_N, NZER_N_B
from integer import ABS_Z_N, TRANS_Z_N, TRANS_N_Z, DIV_ZZ_Z


def FAC_P_Q(polynom):
    """
    P-7
    Вынесение из многочлена НОК знаменателей коэффициентов
    и НОД числителей
    Ким Артём, 7305
    """

    # Берем модуль числителя и знаменатель старшего коэффициента
    n = ABS_Z_N(polynom[1][-1][0])
    m = polynom[1][-1][1]

    # Для всех остальных ненулевых коэффициентов считаем НОД и НОК
    # с n и m соответственно и сохраняем их обратно в n и m
    for i in range(polynom[0]):
        if NZER_N_B(ABS_Z_N(polynom[1][i][0])):
            n = GCF_NN_N(ABS_Z_N(polynom[1][i][0]), n)
            m = LCM_NN_N(polynom[1][i][1], m)

    # Переводим НОД числителей из натурального в целое
    result = [TRANS_N_Z(n), m]

    return result

