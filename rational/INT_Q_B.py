from integer import ABS_Z_N
from natural import GCF_NN_N, COM_NN_D

def INT_Q_B(number):
    """
    Q-2
    Проверка на целое, если число является целым, то True, иначе False
    Власенко Владислав, 7305
    """
    # НОД числителя и знаменателя
    gcf = GCF_NN_N(number[1], ABS_Z_N(number[0]))
    # Если НОД равен знаменателю - число целое
    result = COM_NN_D(gcf, number[1]) == 0

    return result

