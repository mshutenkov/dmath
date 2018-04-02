import common
from rational import TRANS_Q_Z


def rational(Q):
#   if Q[1][0] == 1 and Q[1][1][0] == 1:
#       return str(common.Z_to_num(Q[0]))

    return '%d/%d' % (
            common.Z_to_num(Q[0]),
            common.N_to_num(Q[1]),
            )

def polynom(P):
    result = ''

    for rank in range(P[0]):
        coef = P[1][rank]
        if coef[0][1] != 0 or coef[0][2][0] != 0:
            elem = '%s' % rational(coef)
            if rank:
                elem += 'x'
                if rank > 1:
                    elem += '^%d' % rank

            result = elem + (' + ' if result else '') + result

    return result if result else '0'

