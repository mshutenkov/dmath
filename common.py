"""
Вспомогательные функции
"""

def num_to_N(number):
    """
    Перевод числа в натуральное
    """
    if number < 0:
        raise Exception('Отрицательное не может быть натуральным!')

    result = [0, []]
    if number == 0:
        result[0] = 1
        result[1].append(0)
    else:
        while number > 0:
            result[1].append(number % 10)
            result[0] += 1
            number //= 10
    return result


def N_to_num(N):
    """
    Перевод натурального в число
    """
    result = 0
    for digit in reversed(N[1]):
        result = result * 10 + digit
    return result


def copy_N(N):
    """
    Копирование натурального числа
    """
    result = [N[0], []]
    for digit in N[1]:
        result[1].append(digit)
    return result


def num_to_Z(number):
    """
    Перевод числа в целое
    """
    if number < 0:
        N = num_to_N(-number)
        result = [1]
    else:
        N = num_to_N(number)
        result = [0]
    result += N
    return result


def Z_to_num(Z):
    """
    Перевод целого в число
    """
    N = [Z[1], Z[2]]
    result = N_to_num(N)
    return result if Z[0] == 0 else -result


def copy_Z(Z):
    """
    Копирование целого числа
    """
    N = copy_N([Z[1], Z[2]])
    return [Z[0], N[0], N[1]]


def rat_to_Q(n, m):
    """
    Перевод пары чисел (числитель,знаменатель) в рациональное
    """
    return [num_to_Z(n), num_to_N(m)]


def Q_to_rat(Q):
    """
    Перевод рационального в пару (числитель,знаменатель)
    """
    return [Z_to_num(Q[0]), N_to_num(Q[1])]


def copy_Q(Q):
    """
    Копирование рационального числа
    """
    return [copy_Z(Q[0]), copy_N(Q[1])]


def coef_to_P(coefs):
    """
    Перевод набора коеффициентов вида (числитель,знаменатель)
    в многочлен. Коэффициенты в прямом порядке
    [ (1, 1), (2, 1), (3, 1) ]  ->  x^2 + 2x + 3
    """
    result = [-1, []]
    for c in reversed(coefs):
        q = rat_to_Q(*c)
        result[1].append(q)
        result[0] += 1
    return result


def P_to_coef(P):
    """
    Перевод многочлена в набор коэффициентов вида [числитель, знаменатель]
    """
    result = []
    for q in P[1]:
        result.insert(0, Q_to_rat(q))
    return result


def copy_P(P):
    """
    Копирование многочлена
    """
    result = [P[0], []]
    for q in P[1]:
        result[1].append(copy_Q(q))
    return result

def down_p(polynom):
    """
    Удаление нулевых старших коэффициентов
    Пока старший коэффициент равен нулю, то удаляет его и понижает степень.
    """
    while polynom[1][-1][0][1] == 1 \
            and polynom[1][-1][0][2][0] == 0 \
            and polynom[0] > 0:
        polynom[0] -= 1
        del polynom[1][-1]

