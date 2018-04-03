import common
from rational import TRANS_Q_Z, INT_Q_B, RED_Q_Q


def rational(Q):
#   if Q[1][0] == 1 and Q[1][1][0] == 1:
#       return str(common.Z_to_num(Q[0]))

    return '%d/%d' % (
            common.Z_to_num(Q[0]),
            common.N_to_num(Q[1]),
            )

def polynom(P):
    result = ''

    for rank in range(P[0] + 1):
        coef = P[1][rank]
        # Если коэффициент не ноль
        if coef[0][1] != 1 or coef[0][2][0] != 0:
            sign = '+'
            elem = ''
            # Если коеффициент - целое
            if INT_Q_B(coef):
                num = common.Z_to_num(TRANS_Q_Z(RED_Q_Q(coef)))
                sign = '+' if num > 0 else '-'
                num = abs(num)
                if num != 1 or rank == 0:
                    elem = '%d' % num
            else:
                if coef[0][0] == 1:
                    sign = '-'
                elem = '%s' % rational([[0, coef[0][1], coef[0][2]], coef[1]])

            if rank:
                elem += 'x'
                if rank > 1:
                    elem += '^%d' % rank

            result = '%s %s %s' % (sign, elem, result)

    result = result.strip()
    if result.startswith('+'):
        result = result[1:]
        result = result.strip()
    return result if result else '0'

