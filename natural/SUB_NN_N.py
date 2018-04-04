from natural import COM_NN_D
import common


def SUB_NN_N(number1, number2):
    """
    N-5
    Вычитание из первого большего натурального числа второго
    меньшего или равного
    Томников Роман, 7305
    """
    if COM_NN_D(number1, number2) == 1:
        raise Exception("Первое число должно быть больше второго!")

    # Копируем первое число
    result = common.copy_N(number1)

    # Номер старшего разряда
    i = number2[0] - 1

    while i >= 0:
        # Если цифра уменьшаемого меньше цифры вычитаемого
        if result[1][i] < number2[1][i]:
            result[1][i] += 10 - number2[1][i]
            # Номер следующего разряда
            k = i + 1
            # Пока следующие разряды равны 0 - ставим их равными 9
            while result[1][k] == 0:
                result[1][k] = 9
                k += 1
            # От первого ненулевого разряда вычитаем единицу
            result[1][k] -= 1
        else:
            result[1][i] -= number2[1][i]

        i -= 1

    # Удаляем нулевые старшие разряды
    while result[1][-1] == 0 and result[0] > 1:
        result[0] -= 1
        del result[1][-1]

    return result

