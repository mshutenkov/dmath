from PyQt5 import QtWidgets, QtGui, uic

from validators import NaturalValidator, IntegerValidator, \
        RationalValidator, PolynomValidator
import natural
import integer
import rational
import polynom
import common


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


