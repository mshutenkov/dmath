from natural import SUB_NN_N, MUL_ND_N, COM_NN_D
import common


def SUB_NDN_N(number1, number2, k):
    """
    N-9
    Вычитание из натурального другого натурального,
    умноженного на цифру для случая с неотрицательным
    результатом
    Сибиреков Денис, 7305
    """

    # Умножаем второе число на k
    m = MUL_ND_N(number2, k)
    # Проверка корректности входных данных
    if COM_NN_D(number1, m) == 1:
        raise Exception(
                'Первое число должно быть меньше второго, умноженного на k!'
                )

    return SUB_NN_N(number1, m)

