from PyQt5 import QtWidgets, QtGui, uic

from validators import NaturalValidator, IntegerValidator, \
        RationalValidator, PolynomValidator
import common

import natural
import integer
import rational
import polynom


def on_exception(win, exception):
    QtWidgets.QMessageBox.critical(
            win,
            "Ошибка",
            str(exception)
            )


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

    def add_history_record(self, record):
        self.listWidget.addItem(record)

    def on_btn_history_clear_released(self):
        self.listWidget.clear()


    #############################################
    # Natural
    #############################################

    def on_btn_n_com_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
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
            on_exception(self, e)


    def on_btn_n_nzer_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            result = natural.NZER_N_B(n1)
            sign = '!=' if result else '='

            self.add_history_record('%d %s 0' % (
                common.N_to_num(n1),
                sign,
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_add1_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            result = natural.ADD_1N_N(n1)
            self.add_history_record('%d + 1 = %d' % (
                common.N_to_num(n1),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_addn_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.ADD_NN_N(n1, n2)
            self.add_history_record('%d + %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_subn_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.SUB_NN_N(n1, n2)
            self.add_history_record('%d - %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_muld_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            k = int(self.line_n_k.text())
            result = natural.MUL_ND_N(n1, k)
            self.add_history_record('%d * %d = %d' % (
                common.N_to_num(n1),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_mulk_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            k = int(self.line_n_k.text())
            result = natural.MUL_Nk_N(n1, k)
            self.add_history_record('%d * 10^%d = %d' % (
                common.N_to_num(n1),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_muln_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.MUL_NN_N(n1, n2)
            self.add_history_record('%d * %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_subnk_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            k = int(self.line_n_k.text())
            result = natural.SUB_NDN_N(n1, n2, k)
            self.add_history_record('%d - %d * %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                k,
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_divnd_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            k = int(self.line_n_k.text())
            result = natural.DIV_NN_Dk(n1, n2, k)
            self.add_history_record('%d / (%d * 10^%d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                k,
                result,
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_divn_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.DIV_NN_N(n1, n2)
            self.add_history_record('%d / %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_modn_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.MOD_NN_N(n1, n2)
            self.add_history_record('%d %% %d = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_gcf_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.GCF_NN_N(n1, n2)
            self.add_history_record('НОД(%d, %d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    def on_btn_n_lcm_released(self):
        try:
            n1 = common.num_to_N(int(self.line_n_n1.text()))
            n2 = common.num_to_N(int(self.line_n_n2.text()))
            result = natural.LCM_NN_N(n1, n2)
            self.add_history_record('НОК(%d, %d) = %d' % (
                common.N_to_num(n1),
                common.N_to_num(n2),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    #############################################
    # Integer
    #############################################

    def on_btn_z_abs_released(self):
        try:
            z1 = common.num_to_Z(int(self.line_z_z1.text()))
            result = integer.ABS_Z_N(z1)
            self.add_history_record('|%d| = %d' % (
                common.Z_to_num(z1),
                common.N_to_num(result),
                ))
        except Exception as e:
            on_exception(self, e)

    #############################################
    # Rational
    #############################################

    #############################################
    # Polynom
    #############################################

