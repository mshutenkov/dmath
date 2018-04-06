def TRANS_Q_Z(number):
    """
    Q-4
    Преобразование дробного в целое (если знаменатель равен 1)
    Фёдорова Алиса, 7305
    """
    if number[1][0] > 1 or number[1][1][0] != 1:
        raise Exception('Знаменатель не равен единице!')

    return number[0]

