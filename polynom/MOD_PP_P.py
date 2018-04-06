from polynom import DIV_PP_P, MUL_PP_P, SUB_PP_P
import common


def MOD_PP_P(polynom1, polynom2):
    """
    P-10
    Остаток от деления многочлена на многочлен при делении с остатком
    Хафизов Ильназ, 7305
    """
    # Частное
    div = DIV_PP_P(polynom1, polynom2)
    # Остаток = Делимое - Частное * Делитель
    result = SUB_PP_P(polynom1, MUL_PP_P(div, polynom2))
    return result

