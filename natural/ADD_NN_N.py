from natural import COM_NN_D
import common


def ADD_NN_N(number1, number2):
    """
    N-4
    Сложение натуральных чисел
    Степанова Анастасия, 7305
    """
    # Перенос
    shift = 0

    com = COM_NN_D(number1, number2)
    # Копируем большее число и запоминаем меньшее
    if com == 2:
        result = common.copy_N(number1)
        less = number2
    else:
        result = common.copy_N(number2)
        less = number1

    # Добавляем разряд для переноса
    result[0] += 1
    result[1].append(0)

    # Складываем цифры
    i = 0
    while i < less[0]:
        s = result[1][i] + less[1][i] + shift
        if s > 9:
            result[1][i] = s - 10
            shift = 1
        else:
            result[1][i] = s
            shift = 0
        i += 1

    # Если перенос остался
    if shift == 1:
        while result[1][i] == 9:
            result[1][i] = 0
            i += 1
        result[1][i] += 1

    # Если старший разряд остался равным нулю - удаляем его
    if result[1][-1] == 0:
        result[0] -= 1
        del result[1][-1]

    return result

