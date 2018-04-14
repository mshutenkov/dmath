from rational import DIV_QQ_Q
from polynom import DEG_P_N, MUL_Pxk_P, SUB_PP_P, ADD_PP_P, MUL_PQ_P
import common


def DIV_PP_P(polynom1, polynom2):
    """
    P-9
    Частное от деления многочлена на многочлен при делении с остатком
    Хафизов Ильназ, 7305
    """
    # Степень результата = разность степеней исходных многочленов
    result_deg = polynom1[0] - polynom2[0]
    if result_deg < 0:
        result = [0, [common.rat_to_Q(0, 1)]]
    else:
        result = [result_deg, []]
        tmp = common.copy_P(polynom1)

        for i in range(result_deg + 1):
            # Делим i-ый коэффициент остатка на старший коэффициент делителя
            # Получаем i-ый коэффициент частного
            if tmp[0] < polynom1[0] - i:
                result[1].insert(0, common.rat_to_Q(0, 1))
                continue

            coef = DIV_QQ_Q(tmp[1][polynom1[0] - i], polynom2[1][-1])
            result[1].insert(0, coef)

            # Домножаем делитель на 10^(разность степеней - i)
            sub = MUL_Pxk_P(polynom2, result_deg - i)
            # и вычитаем из остатка домножив на коэффициент
            tmp = SUB_PP_P(tmp, MUL_PQ_P(sub, coef))

    return result

