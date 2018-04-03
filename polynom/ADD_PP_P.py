from rational import ADD_QQ_Q
from common import copy_P, down_p


def ADD_PP_P(polynom1, polynom2):
    """
    P-1
    Сложение многочленов
    Мартыненко Александр, 7305
    """
    # Копируем больший многочлен и выбираем меньший
    if polynom1[0] >= polynom2[0]:
        result = copy_P(polynom1)
        less = polynom2
    else:
        result = copy_P(polynom2)
        less = polynom1

    # Складываем общие коэффициенты
    i = 0
    while i < less[0] + 1:
        result[1][i] = ADD_QQ_Q(result[1][i], less[1][i])
        i += 1

    # Удалаем нули старших коэффициентов
    down_p(result)

    # Возвращаем полученный многочлен      
    return result

