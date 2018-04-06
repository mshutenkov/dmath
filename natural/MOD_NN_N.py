from natural import DIV_NN_N, SUB_NDN_N, MUL_Nk_N

import common


def MOD_NN_N(number1, number2):
    """
    N-12
    Остаток от деления большего натурального числа на меньшее
    или равное натуральное с остатком (делитель отличен от нуля)
    Сибиреков Денис, 7305
    """
    # Вычисляем частное и копируем в результат делимое
    p = DIV_NN_N(number1, number2)
    result = common.copy_N(number1)

    # Вычитаем из результата делитель, умноженный на 10^k и k-ую
    # цифру частного
    for i in range(p[0]):
        result = SUB_NDN_N(result, MUL_Nk_N(number2, i), p[1][i])

    # Убираем нули старших разрядов
    while result[1][-1] == 0 and result[0] > 1:
        result[0] -= 1
        del result[1][-1]

    return result

