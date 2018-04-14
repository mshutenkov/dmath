from natural import DIV_NN_Dk, SUB_NDN_N, MUL_Nk_N
import common


def DIV_NN_N(number1, number2):
    """
    N-11
    Частное от деления большего натурального числа на меньшее
    или равное натуральное с остатком (делитель отличен от нуля)
    Сибиреков Денис, 7305
    """
    n = number1
    i = number1[0] - number2[0]
    if i < 0:
        i = 0
    result = [i + 1, [0] * (i + 1)]

    while i >= 0:
        # Вычисляем первую цифру деления
        k = DIV_NN_Dk(n, number2, i)
        # Домножаем делитель на 10^i
        m = MUL_Nk_N(number2, i)

        # Вычитаем из делимого деитель, домноженный на 10^i и цифру деления
        n = SUB_NDN_N(n, m, k)
        # Сохраняем цифру в результат
        result[1][i] = k

        i -= 1

    # Удаляем нулевые старшие разряды
    while result[1][-1] == 0 and result[0] > 1:
        result[0] -= 1
        del result[1][-1]

    return result

