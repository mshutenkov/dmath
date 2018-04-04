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

    def validate_elem(self, string):
        if not string:
            return 1
        if 'x' not in string:
            return self.rval.validate(string, None)[0]
        if string.count('x') > 1:
            return 0
        coef, deg = string.split('x')

        result = 2
        if coef:
            result = min(result, self.rval.validate(coef, None)[0])

        if deg:
            try:
                n = int(deg)
            except:
                result = 0
            else:
                if n < 0:
                    result = 0
        return result


    def validate(self, string, pos):
        tmp = string.replace(' ', '')

        if '--' in tmp or '++' in tmp or '-+' in tmp or '+-' in tmp:
            return 0, string, pos

        tmp = tmp.replace('-', '+').split('+')

        result = 2
        for d in tmp:
            result = min(result, self.validate_elem(d))

        return result, string, pos

