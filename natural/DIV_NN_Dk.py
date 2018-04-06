from natural import MUL_Nk_N, COM_NN_D, SUB_NN_N, NZER_N_B
import common


def DIV_NN_Dk(number1, number2, k):
    """
    N-10
    Вычисление первой цифры деления большего натурального на меньшее,
    домноженное на 10^k, где k - номер позиции этой цифры
    (номер считается с нуля)
    Сибиреков Денис, 7305
    """
    if not NZER_N_B(number2):
        raise Exception('Попытка деления на 0!')

    n = common.copy_N(number1)
    m = MUL_Nk_N(number2, k)
    result = 0
    while COM_NN_D(n, m) != 1:
        result += 1
        n = SUB_NN_N(n, m)

    return result % 10


