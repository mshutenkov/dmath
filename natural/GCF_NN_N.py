from natural import MOD_NN_N, NZER_N_B


def GCF_NN_N(number1, number2):
    """
    N-13
    НОД натуральных чисел
    Колосюк Влад, 7305
    """
    one = number1
    two = number2

    while NZER_N_B(two):
        two, one = MOD_NN_N(one, two), two

    return one

