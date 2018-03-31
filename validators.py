from PyQt5 import QtGui


class NaturalValidator(QtGui.QValidator):
    def validate(self, string, pos):
        if not string:
            return 1, string, pos

        result = 2 if string.isdecimal() else 0
        return result, string, pos


class IntegerValidator(QtGui.QValidator):
    nval = NaturalValidator()

    def validate(self, string, pos):
        if not string or string == '-':
            return 1, string, pos

        if string.startswith('-'):
            result = self.nval.validate(string[1:], pos)[0]
        else:
            result = self.nval.validate(string, pos)[0]
        return result, string, pos

    def fixup(self, string):
        if string == '-':
            return '-1'


class RationalValidator(QtGui.QValidator):
    def validate(self, string, pos):
        if not string:
            return 1, string, pos

        parts = string.split('/')
        if len(parts) > 2:
            return 0, string, pos

        result = 2
        if parts[0] == '-' or not parts[0]:
            result = 1
        else:
            try:
                int(parts[0])
            except:
                result = 0
        if len(parts) == 2 and result > 0:
            if parts[1]:
                try:
                    n = int(parts[1])
                    if n < 0:
                        result = 0
                except:
                    result = 0
            else:
                result = 1

        return result, string, pos

    def fixup(self, string):
        tmp = string.strip().replace(' ', '')
        if tmp.startswith('-/'):
            tmp = '-1/' + tmp[2:]
        if tmp.startswith('/'):
            tmp = '1' + tmp
        if tmp.endswith('/'):
            tmp = tmp[:-1]
        if tmp == '-':
            tmp = '-1'
        return tmp



class PolynomValidator(QtGui.QValidator):
    rval = RationalValidator()

    def validate(self, string, pos):
        tmp = string.replace(' ', '').replace('-', '+').split('+')

        result = 2
        for d in tmp:
            if not d:
                result = min(result, 1)
                continue

            if 'x' not in d:
                tmp = self.rval.validate(d, None)
                result = min(tmp[0], result)
                continue

            if d.count('x') > 1:
                result = 0
                break

            coef, deg = d.split('x')
            if coef:
                tmp = self.rval.validate(coef, pos)
                result = min(tmp[0], result)
            else:
                result = 1 if result > 1 else result

            if deg:
                try:
                    n = int(deg)
                except:
                    result = 0
                else:
                    if n < 0:
                        result = 0

        return result, string, pos

