import common

def MUL_ZM_Z(number):
    """
    Z-3
    Умножение целого на (-1)
    Царёв Александр, 7305
    """
    # Копируем число и меняем знак
    result = common.copy_Z(number)
    result[0] = 0 if result[0] == 1 else 1
    return result

