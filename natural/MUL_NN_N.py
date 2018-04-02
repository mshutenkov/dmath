from natural import MUL_ND_N, MUL_Nk_N, ADD_NN_N
import common


def MUL_NN_N(number1, number2):
    """
    N-8
    Умножение натуральных чисел
    Власенко Владислав, 7305
    """
    result = common.num_to_N(0)

    for i in range(number2[0]):
        # Умножаем первое число на i цифру второго и на 10^i
        to_add = MUL_ND_N(MUL_Nk_N(number1, number2[1][i]))
        # Добавляем к результату
        result = ADD_NN_N(result, to_add)

    return result

