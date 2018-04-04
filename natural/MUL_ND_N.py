import common


def MUL_ND_N(number, digit):
    """
    N-6
    Умножение натурального числа на цифру
    Томников Роман, 7305
    """

    if digit == 0:
        return [1, [0]]

    result = [number[0], [0] * number[0]]

    i = 0
    shift = 0
    while i < number[0]:
        # Произведение цифр + перенос
        mul = number[1][i] * digit + shift
        # Единицы записываем в результат, десятки - в перенос
        result[1][i] = mul % 10
        shift = mul // 10

        i += 1

    # Если был перенос в новый разряд
    if shift > 0:
        result[0] += 1
        result[1].append(shift)

    return result

