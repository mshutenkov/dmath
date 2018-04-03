from rational import MUL_QQ_Q, TRANS_Z_Q
from integer import TRANS_N_Z
from common import num_to_Z


def DER_P_P(polynom):
    """
    P-12
    Производная многочлена
    Хафизов Ильназ, 7305
    """

    result = [polynom[0] - 1, []]
    for i in range(result[0] + 1):
        deg = TRANS_Z_Q(num_to_Z(i + 1))
        result[1].append(MUL_QQ_Q(deg, polynom[1][i + 1]))

    return result

