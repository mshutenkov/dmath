import common

def MUL_Nk_N(number, k):
    """
    N-7
    Умножение натурального числа на 10^k
    Томников Роман, 7305
    """
    # Копируем число
    result = common.copy_N(number)

    # Увеличиваем количество разрядов, добавляя нулевые младшие
    result[0] += k
    for i in range(k):
        result[1].insert(0, 0)

    return result

