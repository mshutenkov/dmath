from integer import DIV_ZZ_Z, MUL_ZZ_Z, SUB_ZZ_Z, MUL_ZM_Z
import common


def MOD_ZZ_Z(number1, number2):
    """
    Z-10
    Остаток от деления большего целого числа на меньшее
    или равное натуральное с остатком (делитель отличен от нуля)
    Рэшин Даниил, 7305
    """
    # Частное
    d = DIV_ZZ_Z(number1, number2)

    p = MUL_ZZ_Z(number2, d)
    return SUB_ZZ_Z(number1, p)

