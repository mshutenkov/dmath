from rational import SUB_QQ_Q
from common import copy_P, rat_to_Q, down_p


def SUB_PP_P(polynom1, polynom2):
    """
    P-2
    Вычитание многочленов
    Мартыненко Александр, 7305
    """
    # Копируем первый многочлен
    result = copy_P(polynom1)
    # Увеличиваем степень, если необходимо, добавляя
    # нулевые коэффициенты
    while result[0] < polynom2[0]:
        result[0] += 1
        result[1].append(rat_to_Q(0, 1))

    # Вычитаем коэффициенты
    i = 0
    while i < polynom2[0] + 1:
        result[1][i] = SUB_QQ_Q(result[1][i], polynom2[1][i])
        i+=1

    # Пока старший коэффициент равен нулю,
    # понижаем степень и удаляем коэффициент
    down_p(result)

    # Возвращаем полученный многочлен      
    return result

