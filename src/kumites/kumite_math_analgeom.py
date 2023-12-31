import re


class KumiteMathAnalGeom:
    def __init__(self):
        self.P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

    def binomial_expansion(self, expr):
        a, v, b, e = self.P.findall(expr)[0]

        if e == '0': return '1'

        o = [int(a != '-' and a or a and '-1' or '1'), int(b)]
        e, p = int(e), o[:]

        for _ in range(e - 1):
            p.append(0)
            p = [o[0] * coef + p[i - 1] * o[1] for i, coef in enumerate(p)]

        res = '+'.join(f'{coef}{v}^{e - i}' if i != e else str(coef) for i, coef in enumerate(p) if coef)

        return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-', '-')

class KumiteMathAnalGeomExample:
    def combination(self, k, n):
        if k == 0:
            return 1
        c = 1
        if k + 1 < n - k:
            for i in range(n - k + 1, n + 1):
                c *= i
            for i in range(1, k + 1):
                c /= i
        else:
            for i in range(k + 1, n + 1):
                c *= i
            for i in range(1, n - k + 1):
                c /= i
        return c

    def quick_pow(self, base, power):
        res = 1
        while power:
            if power & 1:
                res *= base
                power -= 1
            else:
                base *= base
                power >>= 1
        return res

    def term_product(self, term_left, term_right, pow_left, pow_right, comb):
        def term_pow(term, power):
            num = ''
            coef = 1
            i = 0
            while i < len(term):
                ch = term[i]
                if ch is None: break
                if not ch.isdigit():
                    if ch == '+':
                        coef = 1
                    elif ch == '-':
                        coef = -1
                    else:
                        break
                else:
                    num += ch
                i += 1
            if num:
                num = int(self.quick_pow(int(num), power))
                if power & 1: num = coef * num
            else:
                num = coef if power & 1 else 1
            var = term[i:] if power != 0 else ''
            return num, var

        num_left, var_left = term_pow(term_left, pow_left)
        num_right, var_right = term_pow(term_right, pow_right)

        final_num = comb * num_left * num_right

        final_pow = ('', '')
        final_var = (var_left, var_right)
        if var_left and var_right:
            if var_left == var_right:
                final_var = (var_left, '')
                if pow_left + pow_right > 1:
                    final_pow = ('^' + str(pow_left + pow_right), '')
            else:
                final_pow = ('^' + str(pow_left), '^' + str(pow_right))
        elif not var_left and var_right:
            if pow_right > 1:
                final_pow = ('', '^' + str(pow_right))
        elif var_left:
            if pow_left > 1:
                final_pow = ('^' + str(pow_left), '')
        if final_var[0] or final_var[1]:
            if final_num == 1 or final_num == 0:
                final_num = ''
            elif final_num == -1:
                final_num = '-'
        if not final_num or final_num != '-' and final_num > 0: final_num = '+' + str(final_num)
        return '{0}{1}{3}{2}{4}'.format(final_num, *final_var, *final_pow)

    def binomial_expansion(self, expr):
        reg = re.compile(
            r'\((?P<term_left>-?.+)(?P<term_right>[+-].+)\)\^(?P<power>\w+)')
        matched = reg.match(expr)
        if not matched:
            return ''
        term_left = matched.group('term_left')
        term_right = matched.group('term_right')
        power = int(matched.group('power'))
        if power == 0:
            return '1'
        expanded = ""
        for k in range(power, -1, -1):
            _comb = int(self.combination(k, power))
            expanded += self.term_product(term_left, term_right, k, power - k, _comb)
        return expanded[1:] if expanded[0] == '+' else expanded

if __name__ == '__main__':
    obj = KumiteMathAnalGeom()
    print(obj.binomial_expansion("(-5m+3)^4"))