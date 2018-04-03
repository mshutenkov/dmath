from natural import DIV_NN_N, GCF_NN_N, MUL_NN_N


def LCM_NN_N(number1, number2):
    """
    N-14
    НОК двух натуральных чисел
    Копылов Петр, 7305
    """

    # НОК(A, B) = A * B / НОД(A, B)
    return DIV_NN_N(MUL_NN_N(number1, number2), GCF_NN_N(number1,number2))

