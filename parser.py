import common
from rational import ADD_QQ_Q

def rational(string):
    if '/' in string:
        return common.rat_to_Q(
                int(string.split('/')[0]),
                int(string.split('/')[1]),
                )
    if string == '-':
        return common.rat_to_Q(-1, 1)
    if string == '+':
        return common.rat_to_Q(1, 1)
    return common.rat_to_Q(
            int(string),
            1
            )


def polynom(string):
    tmp = string.replace(' ', '').replace('-', '|-').replace('+', '|+')
    tmp = tmp.split('|')
    result = [0, [common.rat_to_Q(0, 1)]]
    for p in tmp:
        if not p:
            continue
        if 'x' not in p:
            coef = rational(p)
            result[1][0] = ADD_QQ_Q(coef, result[1][0])
        else:
            coef, deg = p.split('x')
            if deg:
                deg = int(deg)
            else:
                deg = 1

            if coef:
                coef = rational(coef)
            else:
                coef = rational('1')
            
            while result[0] < deg:
                result[0] += 1
                result[1].append(common.rat_to_Q(0, 1))
            result[1][deg] = ADD_QQ_Q(coef, result[1][deg])

    return result

