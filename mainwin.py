from PyQt5 import QtWidgets, QtGui, uic

from validators import NaturalValidator, IntegerValidator, \
        RationalValidator, PolynomValidator
import common
import parser
import pretty

import natural
import integer
import rational
import polynom


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('mainwin.ui', self)

        n_validator = NaturalValidator()
        z_validator = IntegerValidator()
        q_validator = RationalValidator()
        p_validator = PolynomValidator()

        self.line_n_n1.setValidator(n_validator)
        self.line_n_n2.setValidator(n_validator)
        self.line_n_k.setValidator(n_validator)

        self.line_z_z1.setValidator(z_validator)
        self.line_z_z2.setValidator(z_validator)

        self.line_q_q1.setValidator(q_validator)
        self.line_q_q2.setValidator(q_validator)
        self.line_q_z.setValidator(z_validator)

        self.line_p_p1.setValidator(p_validator)
        self.line_p_p2.setValidator(p_validator)
        self.line_p_q.setValidator(q_validator)
        self.line_p_k.setValidator(n_validator)

    def on_exception(self, exception):
        QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                str(exception)
                )

    def add_history_record(self, record):
        self.listWidget.addItem(record)

    def on_btn_history_clear_released(self):
        self.listWidget.clear()


    #############################################
    # Natural
    #############################################

    def get_n_n(self, num):
        if num == 1:
            text = self.line_n_n1.text()
        else:
            text = self.line_n_n2.text()

        if not text:
            raise Exception('N%d не введено' % num)
        return common.num_to_N(int(text))

    def get_n_k(self):
        text = self.line_n_k.text()
        if not text:
            raise Exception('k не введено')
        return int(text)

    def on_btn_n_com_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.COM_NN_D(n1, n2)
            if result == 0:
                sign = '='
            elif result == 1:
                sign = '<'
            else:
                sign = '>'

            self.add_history_record('%d %s %d' % (
                common.N_to_num(n1),
                sign,
                common.N_to_num(n2),
                ))
        except Exception as e:
            self.on_exception(e)


    def on_btn_n_nzer_released(self):
        try:
            n1 = self.get_n_n(1)
            result = natural.NZER_N_B(n1)
            sign = '!=' if result else '='

            self.add_history_record('%d %s 0' % (
                common.N_to_num(n1),
                sign,
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_add1_released(self):
        try:
            n1 = self.get_n_n(1)
            result = natural.ADD_1N_N(n1)
            self.add_history_record('%d + 1 = %d' % (
                common.N_to_num(n1),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_addn_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.ADD_NN_N(n1, n2)
            self.add_history_record('%d + %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_subn_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.SUB_NN_N(n1, n2)
            self.add_history_record('%d - %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_muld_released(self):
        try:
            n1 = self.get_n_n(1)
            k = self.get_n_k()
            result = natural.MUL_ND_N(n1, k)
            self.add_history_record('%d * %d = %d' % (
                common.N_to_num(n1),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_mulk_released(self):
        try:
            n1 = self.get_n_n(1)
            k = self.get_n_k()
            result = natural.MUL_Nk_N(n1, k)
            self.add_history_record('%d * 10^%d = %d' % (
                common.N_to_num(n1),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_muln_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.MUL_NN_N(n1, n2)
            self.add_history_record('%d * %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_subnk_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            k = self.get_n_k()
            result = natural.SUB_NDN_N(n1, n2, k)
            self.add_history_record('%d - %d * %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_divnd_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            k = self.get_n_k()
            result = natural.DIV_NN_Dk(n1, n2, k)
            self.add_history_record('%d / (%d * 10^%d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                k,
                result,
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_divn_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.DIV_NN_N(n1, n2)
            self.add_history_record('%d / %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_modn_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.MOD_NN_N(n1, n2)
            self.add_history_record('%d %% %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_gcf_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.GCF_NN_N(n1, n2)
            self.add_history_record('НОД(%d, %d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_n_lcm_released(self):
        try:
            n1 = self.get_n_n(1)
            n2 = self.get_n_n(2)
            result = natural.LCM_NN_N(n1, n2)
            self.add_history_record('НОК(%d, %d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    #############################################
    # Integer
    #############################################

    def get_z_z(self, num):
        if num == 1:
            text = self.line_z_z1.text()
        else:
            text = self.line_z_z2.text()
        if not text:
            raise Exception('Z%d не введено' % num)
        return common.num_to_Z(int(text))

    def on_btn_z_abs_released(self):
        try:
            z1 = self.get_z_z(1)
            result = integer.ABS_Z_N(z1)
            self.add_history_record('|%d| = %d' % (
                common.Z_to_num(z1),
                common.N_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_poz_released(self):
        try:
            z1 = self.get_z_z(1)
            result = integer.POZ_Z_D(z1)
            if result == 2:
                sign = '>'
            elif result == 0:
                sign = '='
            else:
                sign = '<'

            self.add_history_record('%d %s 0' % (
                common.Z_to_num(z1),
                sign,
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_mulm_released(self):
        try:
            z1 = self.get_z_z(1)
            result = integer.MUL_ZM_Z(z1)
            self.add_history_record('%d * (-1) = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_add_released(self):
        try:
            z1 = self.get_z_z(1)
            z2 = self.get_z_z(2)
            result = integer.ADD_ZZ_Z(z1, z2)
            self.add_history_record('%d + %d = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(z2),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_sub_released(self):
        try:
            z1 = self.get_z_z(1)
            z2 = self.get_z_z(2)
            result = integer.SUB_ZZ_Z(z1, z2)
            self.add_history_record('%d - %d = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(z2),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_mul_released(self):
        try:
            z1 = self.get_z_z(1)
            z2 = self.get_z_z(2)
            result = integer.MUL_ZZ_Z(z1, z2)
            self.add_history_record('%d * %d = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(z2),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_div_released(self):
        try:
            z1 = self.get_z_z(1)
            z2 = self.get_z_z(2)
            result = integer.DIV_ZZ_Z(z1, z2)
            self.add_history_record('%d / %d = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(z2),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_z_mod_released(self):
        try:
            z1 = self.get_z_z(1)
            z2 = self.get_z_z(2)
            result = integer.MOD_ZZ_Z(z1, z2)
            self.add_history_record('%d %% %d = %d' % (
                common.Z_to_num(z1),
                common.Z_to_num(z2),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    #############################################
    # Rational
    #############################################

    def get_q_q(self, num):
        if num == 1:
            text = self.line_q_q1.text()
        else:
            text = self.line_q_q2.text()
        if not text:
            raise Exception('Q%d не введено' % num)
        return parser.rational(text)

    def get_q_z(self):
        text = self.line_q_z.text()
        if not text:
            raise Exception('Z не введено')
        return common.num_to_Z(int(text))

    def on_btn_q_red_released(self):
        try:
            q1 = self.get_q_q(1)
            result = rational.RED_Q_Q(q1)
            self.add_history_record('%s = %s' % (
                pretty.rational(q1),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_q_int_released(self):
        try:
            q1 = self.get_q_q(1)
            result = rational.INT_Q_B(q1)
            self.add_history_record('%s - %sцелое' % (
                pretty.rational(q1),
                '' if result else 'не ',
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_q_transzq_released(self):
        try:
            z = self.get_q_z()
            result = rational.TRANS_Z_Q(z)
            self.add_history_record('%d = %s' % (
                common.Z_to_num(z),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_q_transqz_released(self):
        try:
            q1 = self.get_q_q(1)
            result = rational.TRANS_Q_Z(q1)
            self.add_history_record('%s = %d' % (
                pretty.rational(q1),
                common.Z_to_num(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_q_add_released(self):
        try:
            q1 = self.get_q_q(1)
            q2 = self.get_q_q(2)
            result = rational.ADD_QQ_Q(q1, q2)
            self.add_history_record('%s + %s = %s' % (
                pretty.rational(q1),
                pretty.rational(q2),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_q_sub_released(self):
        try:
            q1 = self.get_q_q(1)
            q2 = self.get_q_q(2)
            result = rational.SUB_QQ_Q(q1, q2)
            self.add_history_record('%s - %s = %s' % (
                pretty.rational(q1),
                pretty.rational(q2),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)
        pass

    def on_btn_q_mul_released(self):
        try:
            q1 = self.get_q_q(1)
            q2 = self.get_q_q(2)
            result = rational.MUL_QQ_Q(q1, q2)
            self.add_history_record('%s * %s = %s' % (
                pretty.rational(q1),
                pretty.rational(q2),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)
        pass

    def on_btn_q_div_released(self):
        try:
            q1 = self.get_q_q(1)
            q2 = self.get_q_q(2)
            result = rational.DIV_QQ_Q(q1, q2)
            self.add_history_record('%s / %s = %s' % (
                pretty.rational(q1),
                pretty.rational(q2),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    #############################################
    # Polynom
    #############################################

    def get_p_p(self, num):
        if num == 1:
            text = self.line_p_p1.text()
        else:
            text = self.line_p_p2.text()
        if not text:
            raise Exception('P%d не введен' % num)
        return parser.polynom(text)

    def get_p_q(self):
        text = self.line_p_q.text()
        if not text:
            raise Exception('Q не введено')
        return parser.rational(text)

    def get_p_k(self):
        text = self.line_p_k.text()
        if not text:
            raise Exception('k не введено')
        return int(text)

    def on_btn_p_add_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.ADD_PP_P(p1, p2)
            self.add_history_record('%s + %s = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_sub_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.SUB_PP_P(p1, p2)
            self.add_history_record('(%s) - (%s) = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_mulq_released(self):
        try:
            p1 = self.get_p_p(1)
            q = self.get_p_q()
            result = polynom.MUL_PQ_P(p1, q)
            self.add_history_record('(%s) * %s = %s' % (
                pretty.polynom(p1),
                pretty.rational(q),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_mulxk_released(self):
        try:
            p1 = self.get_p_p(1)
            k = self.get_p_k()
            result = polynom.MUL_Pxk_P(p1, k)
            self.add_history_record('(%s) * x^%d = %s' % (
                pretty.polynom(p1),
                k,
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_led_released(self):
        try:
            p1 = self.get_p_p(1)
            result = polynom.LED_P_Q(p1)
            self.add_history_record('Led(%s) = %s' % (
                pretty.polynom(p1),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_deg_released(self):
        try:
            p1 = self.get_p_p(1)
            result = polynom.DEG_P_N(p1)
            self.add_history_record('Deg(%s) = %d' % (
                pretty.polynom(p1),
                result,
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_fac_released(self):
        try:
            p1 = self.get_p_p(1)
            result = polynom.FAC_P_N(p1)
            self.add_history_record('Fac(%s) = %s' % (
                pretty.polynom(p1),
                pretty.rational(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_mul_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.MUL_PP_P(p1, p2)
            self.add_history_record('(%s) * (%s) = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_div_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.DIV_PP_P(p1, p2)
            self.add_history_record('(%s) / (%s) = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_mod_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.MOD_PP_P(p1, p2)
            self.add_history_record('(%s) % (%s) = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_gcf_released(self):
        try:
            p1 = self.get_p_p(1)
            p2 = self.get_p_p(2)
            result = polynom.GCF_PP_P(p1, p2)
            self.add_history_record('НОД((%s), (%s)) = %s' % (
                pretty.polynom(p1),
                pretty.polynom(p2),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_der_released(self):
        try:
            p1 = self.get_p_p(1)
            result = polynom.DER_P_P(p1)
            self.add_history_record('(%s)\' = %s' % (
                pretty.polynom(p1),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

    def on_btn_p_nmr_released(self):
        try:
            p1 = self.get_p_p(1)
            result = polynom.NMR_P_P(p1)
            self.add_history_record('%s -> %s' % (
                pretty.polynom(p1),
                pretty.polynom(result),
                ))
        except Exception as e:
            self.on_exception(e)

