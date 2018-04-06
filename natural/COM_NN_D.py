import common

def COM_NN_D(number1, number2):
    """
    N-1
    Сравнение натуральных чисел: 2 - если первое больше второго,
    0 - если равно, 1 иначе
    Степанова Анастасия, 7305
    """
    # Если первое имеет больше разрядов - оно больше
    if number1[0] > number2[0]:
        result = 2
    # Аналогично для второго
    elif number1[0] < number2[0]:
        result = 1
    # Если количество разрядов одинаковое - проверяем поразрядно
    else:
        result = 0
        # Номер старшего разряда
        i = number1[0] - 1

        # Пока числа равны и есть разряды
        while result == 0 and i >= 0:
            if number1[1][i] > number2[1][i]:
                result = 2
            elif number1[1][i] < number2[1][i]:
                result = 1
            i -= 1

    return result

