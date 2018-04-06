from natural import LCM_NN_N, NZER_N_B
from integer import MUL_ZZ_Z, ADD_ZZ_Z, TRANS_N_Z, DIV_ZZ_Z
from rational import RED_Q_Q


def ADD_QQ_Q(number1, number2):
    """
    Q-5
    Сложение дробей
    Фёдоров Семён, 7305
    """
    # N1/M1 + N2/M2 = (N1*lcm/M1 + N2*lcm/M2) / lcm = (N1*k1 + N2*k2) / lcm
    # где k1 = lcm/M1, k2 = lcm/M2
    lcm = LCM_NN_N(number1[1], number2[1])

    k1 = DIV_ZZ_Z(TRANS_N_Z(lcm), TRANS_N_Z(number1[1]))
    k2 = DIV_ZZ_Z(TRANS_N_Z(lcm), TRANS_N_Z(number2[1]))
    n = ADD_ZZ_Z(
            MUL_ZZ_Z(k1, number1[0]),
            MUL_ZZ_Z(k2, number2[0]),
            )

    return RED_Q_Q([n, lcm])

